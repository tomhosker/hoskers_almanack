### This code holds a class which can translate LaTeX into HPML.

# Local imports.
from hpml.constants import lexicon

# The class in question.
class Translator_L2H:
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

  # Purge LaTeX line endings from each line.
  def purge_endings(self):
    for line in self.lines:
      i = self.lines.index(line)
      # Remove whitespace from line ends.
      while line.endswith(" ") or line.endswith("\t"):
        line = line[0:len(line)-1]
      # Handle line ending with a brace.
      ends_with_a_brace = False
      if line.endswith("}"):
        line = line[0:len(line)-1]
        ends_with_a_brace = True
      if line.endswith("\\\\*"):
        line = line[0:len(line)-len("\\\\*")]
      elif line.endswith("\\\\!"):
        line = line[0:len(line)-len("\\\\!")]
        if (i != len(self.lines)-1) and (self.lines[i+1] != ""):
          raise Exception("No blank line between verses: "+
                          str(i)+". \""+line+"\".")
      elif line.endswith("\\\\"):
        line = line[0:len(line)-len("\\\\")]
      if "\\\\" in line:
        raise Exception("Two line endings in one line:"+
                        str(i)+". \""+line+"\".")
      if ends_with_a_brace:
        line = line+"}"
      self.lines[i] = line
    # Remove any remaining blank lines.
    while(self.lines[len(self.lines)-1] == ""):
      self.lines = self.lines[0:-1]

  # Translate those clusters for which clear equivalents exist.
  def translate_equivalents(self):
    for line in self.lines:
      i = self.lines.index(line)
      for entry in lexicon:
        while entry[0] in line:
          line = line.replace(entry[0], entry[1])
      self.lines[i] = line

  # Ronseal.
  def build_out(self):
    self.purge_endings()
    self.translate_equivalents()
    for line in self.lines:
      if self.lines.index(line) == len(self.lines)-1:
        self.out = self.out+line
      else:
        self.out = self.out+line+"\n"

  # Returns a string containing the translation.
  def return_translation(self):
    return self.out

  # Ronseal.
  def save_translation(self, filename):
    if filename == None:
      if self.source_f == None:
        filename = "translation.hpml"
      else:
        if self.source_f.endswith(".tex"):
          filename = self.source_f[0:self.source_f.index(".tex")]+".hpml"
        else:
          filename = self.source_f+".hpml"
    f = open(filename, "w")
    f.write(self.out)
    f.close()

# Run unit tests.
def demo():
  t = Translator_L2H("test1.tex", None)
  t.save_translation(None)
  print(t.return_translation())

# Run and wrap up.
def run():
  demo()
#run()
