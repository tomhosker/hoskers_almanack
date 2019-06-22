### This code holds a class which can compile HPML into LaTeX.

# Local imports.
from hpml.constants import lexicon
from hpml.constants import fractions

# The class in question.
class HPML_compiler:
  def __init__(self, source_f, source_s):
    self.source_f = source_f
    self.source_s = source_s
    if source_s == None:
      f = open(self.source_f, "r")
      self.source_s = f.read()
      f.close()
    self.lines = self.source_s.split("\n")
    self.out = ""
    self.build_out()

  # Ronseal.
  def purge_whitespace(self):
    for line in self.lines:
      i = self.lines.index(line)
      # Remove whitespace from line ends.
      while line.endswith(" "):
        line = line[0:len(line)]
      self.lines[i] = line
    # Remove any remaining blank lines.
    while(self.lines[len(self.lines)-1] == ""):
      self.lines = self.lines[0:-1]

  # Adds "\\", "\\*" or "\\!" to each line, as appropriate.
  def add_endings(self):
    for line in self.lines:
      i = self.lines.index(line)
      if ((line == "") or (line == "{\itshape ") or
          (i == len(self.lines)-1)):
        continue
      if i != len(self.lines)-1:
        if self.lines[i+1] == "":
          line = line+"\\\\!"
          self.lines[i] = line
          continue
      if (i == 0) or (i == len(self.lines)-2):
        line = line+"\\\\*"
        self.lines[i] = line
        continue
      elif self.lines[i-1] == "":
        line = line+"\\\\*"
        self.lines[i] = line
        continue
      elif i < len(self.lines)-2:
        if self.lines[i+2] == "":
          line = line+"\\\\*"
          self.lines[i] = line
          continue
      line = line+"\\\\"
      self.lines[i] = line

  # Translate those clusters for which clear equivalents exist.
  def process_syntactics(self):
    for line in self.lines:
      i = self.lines.index(line)
      for entry in lexicon.keys():
        while entry in line:
          line = line.replace(entry, lexicon[entry])
      self.lines[i] = line

  # Ronseal.
  def process_places(self):
    for line in self.lines:
      i = self.lines.index(line)
      while "#PLACE{" in line:
        line = line.replace("#PLACE{", "\\textsc{")
      self.lines[i] = line

  # Ronseal.
  def process_persons(self):
    for line in self.lines:
      i = self.lines.index(line)
      while "#PERSON{" in line:
        line = line.replace("#PERSON{", "\\textit{")
      self.lines[i] = line

  # Ronseal.
  def process_publications(self):
    for line in self.lines:
      i = self.lines.index(line)
      while "#PUBLICATION{" in line:
        line = line.replace("#PUBLICATION{", "{\\hoskeroe ")
      self.lines[i] = line

  # Ronseal.
  def process_foreign_strings(self):
    for line in self.lines:
      i = self.lines.index(line)
      while "#FOREIGN{" in line:
        line = line.replace("#FOREIGN{", "{\\hoskeroe ")
      self.lines[i] = line

  # Ronseal.
  def process_fractions(self):
    for line in self.lines:
      i = self.lines.index(line)
      for entry in fractions.keys():
        while entry in line:
          line = line.replace(entry, fractions[entry]["latex"])
        self.lines[i] = line

  # Ronseal.
  def process_ampersands(self):
    for line in self.lines:
      i = self.lines.index(line)
      while "#ADD" in line:
        line = line.replace("#ADD", "\&")
      self.lines[i] = line

  # Handles stressed syllables.
  def process_stress(self):
    for line in self.lines:
      i = self.lines.index(line)
      while "#STRESS{" in line:
        line = line.replace("#STRESS{", "\\'{")
      self.lines[i] = line

  # Handles choruses and inscriptions.
  def process_choruses(self):
    for line in self.lines:
      i = self.lines.index(line)
      if ("###CHORUS" in line) or ("###INSCRIPTION" in line):
        line = "{\\itshape "
        for j in range(i+1, len(self.lines)):
          if j == len(self.lines)-1:
            self.lines[j] = self.lines[j]+"}"
          elif self.lines[j] == "":
            self.lines[j-1] = self.lines[j-1]+"}"
            break
        self.lines[i] = line

  # Handles mini-choruses and mini-inscriptions.
  def process_minichoruses(self):
    for line in self.lines:
      i = self.lines.index(line)
      if ("##MINICHORUS" in line) or ("##MINIINSCRIPTION" in line):
        line = line.replace("##MINICHORUS ", "\\vin \\textit{")
        line = line.replace("##MINIINSCRIPTION ", "\\textit{")
        line = line+"}"
        self.lines[i] = line

  # Adds mini-titles to particular verses.
  def process_flagverses(self):
    for line in self.lines:
      i = self.lines.index(line)
      line = line.replace("##FLAGVERSE{", "\\flagverse{\\footnotesize ")
      self.lines[i] = line

  # Ronseal.
  def process_subscript(self):
    for line in self.lines:
      i = self.lines.index(line)
      while "#SUB{" in line:
        line = line.replace("#SUB{", "\\textsubscript{")
      self.lines[i] = line

  # Ronseal.
  def process_whitespace(self):
    for line in self.lines:
      i = self.lines.index(line)
      while "#WHITESPACE{" in line:
        line = line.replace("#WHITESPACE{", "\\textcolor{white}{")
      self.lines[i] = line

  # Ronseal.
  def process_semantics(self):
    self.process_places()
    self.process_persons()
    self.process_publications()
    self.process_foreign_strings()
    self.process_fractions()
    self.process_ampersands()
    self.process_stress()
    self.process_flagverses()
    self.process_subscript()
    self.process_whitespace()

  # Ronseal.
  def build_out(self):
    self.purge_whitespace()
    self.process_choruses()
    self.process_minichoruses()
    self.add_endings()
    self.process_syntactics()
    self.process_semantics()
    for line in self.lines:
      if self.lines.index(line) == len(self.lines)-1:
        self.out = self.out+line
      else:
        self.out = self.out+line+"\n"

  # Returns a string containing the compilation.
  def digest(self):
    return self.out

  # Ronseal.
  def save(self, filename):
    if filename == None:
      if self.source_f == None:
        filename = "compilation.tex"
      else:
        if self.source_f.endswith(".hpml"):
          filename = self.source_f[0:self.source_f.index(".hpml")]+".tex"
        else:
          filename = self.source_f+".tex"
    f = open(filename, "w")
    f.write(self.out)
    f.close()

# Run unit tests.
def demo():
  t = HPML_compiler("test2.hpml", None)
  t.save_compilation(None)
  print(t.return_compilation())

# Run and wrap up.
def run():
  demo()
#run()
