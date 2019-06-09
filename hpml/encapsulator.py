# A class to handle the encapsulation of a LaTeX verse snippet into an
# autonomous, compilable .tex file.

# Constants.
max_width = 100
slim = (
  "\\usepackage{microtype,mathtools,verse,xcolor,xfrac,fourier-orns}\n"+
  "\\usepackage{fontspec}\n"+
  "\\newfontfamily\\hoskeroe{English Towne}\n"+
  "\\usepackage[T1]{fontenc}")

### Helper functions.
# Remove any line-ending syntax.
def remove_line_endings(line):
  if line.endswith("\\"):
    line = line[0:len(line)-len("\\")-1]
  elif line.endswith("\\*"):
    line = line[0:len(line)-len("\\*")-1]
  elif line.endswith("\\!"):
    line = line[0:len(line)-len("\\!")-1]
  elif line.endswith("\\}"):
    line = line[0:len(line)-len("\\}")-1]
  elif line.endswith("\\*}"):
    line = line[0:len(line)-len("\\*}")-1]
  elif line.endswith("\\!}"):
    line = line[0:len(line)-len("\\!}")-1]
  return line

# Ronseal.
def detect_unpaired_braces(line):
  n = 0
  for i in range(len(line)):
    if line[i] == "{":
      n = n+1
    elif line[i] == "}":
      n = n-1
  return n

# Ronseal.
def remove_unpaired_braces(line):
  while line.startswith("{") and (detect_unpaired_braces(line) > 0):
    line = line[1:len(line)-1]
  while line.endswith("}") and (detect_unpaired_braces(line) < 0):
    line = line[0:len(line)-2]
  return line

### The class in question.
class Encapsulator:
  def __init__(self, snippet, loadout_name):
    documentclass = "\\documentclass{amsart}"
    title = "\\title{Current}"
    loadout = slim
    begin = "\\begin{document}\n\n\\begin{verse}"
    end = "\\end{verse}\n\n\\end{document}"
    second_longest_line = self.find_second_longest_line(snippet)
    if len(second_longest_line) < max_width:
      begin = begin.replace("\\begin{verse}",
                "\\settowidth{\\versewidth}{"+second_longest_line+"}\n"+
                "\\begin{verse}[\\versewidth]")
    self.doc = (documentclass+"\n\n"+title+"\n\n"+loadout+"\n\n"+begin+"\n"+
                snippet+"\n"+end)

  # Ronseal.
  def find_second_longest_line(self, snippet):
    lines = snippet.split("\n")
    longest_line = lines[0]
    second_longest_line = lines[0]
    for line in lines:
      if len(line) > len(longest_line):
        second_longest_line = longest_line
        longest_line = line
      elif len(line) > len(second_longest_line):
        second_longest_line = line
    second_longest_line = remove_line_endings(second_longest_line)
    second_longest_line = remove_unpaired_braces(second_longest_line)
    return second_longest_line

  # Return the result as a string.
  def digest(self):
    return self.doc

  # Save the result to a file.
  def save(self):
    f = open("current.tex", "w")
    f.write(self.doc)
    f.close()
