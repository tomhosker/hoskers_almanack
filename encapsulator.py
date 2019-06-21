### A class to handle the encapsulation of a LaTeX verse snippet into a
### "\begin{verse}", "\end{verse}" sandwich.

# Imports.
import sqlite3

# Local imports.
import constants

# Constants.
max_width = 100

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

# Gets the list of packages (and related) from the database.
def get_loadout(loadout_name):
  select = "SELECT latex FROM package_loadout WHERE name = ?;"
  conn = sqlite3.connect(constants.db)
  c = conn.cursor()
  c.execute(select, (loadout_name,))
  extract = c.fetchone()
  result = extract[0]
  return result

# Ronseal.
def find_second_longest_line(snippet):
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

### A class to add the "\begin{verse}..." and "\end{verse}" to the LaTeX for
### a given article.
class Mini_encapsulator:
  def __init__(self, snippet):
    second_longest_line = find_second_longest_line(snippet)
    if len(second_longest_line) < max_width:
      begin = ("\\settowidth{\\versewidth}{"+second_longest_line+"}\n"+
               "\\begin{verse}[\\versewidth]")
    else:
      begin = "\\begin{verse}"
    end = "\\end{verse}"
    self.result = begin+"\n"+snippet+"\n"+end

  # Return the result as a string.
  def digest(self):
    return self.result
