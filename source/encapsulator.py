"""
This code defines a class which handles the encapsulation of a LaTeX verse
snippet into a full .tex file.
"""

# Standard imports.
import re
from pathlib import Path

# Local imports.
from .configs import PATH_OBJ_TO_PACKAGE_LOADOUTS

# Local constants.
DEFAULT_LOADOUT = "main"
DEFAULT_PATH_TO_OUTPUT = "current.tex"
MAX_WIDTH = 100
FALLBACK_WIDTH_STR = "0.8\\textwidth"
DEFAULT_POEM_LINES = 5

##############
# MAIN CLASS #
##############

class Encapsulator:
    """ The class in question. """
    def __init__(
            self,
            snippet,
            loadout=DEFAULT_LOADOUT,
            path_to_output=DEFAULT_PATH_TO_OUTPUT
        ):
        self.original = snippet
        self.loadout = loadout
        self.path_to_output = path_to_output
        self.output_str = self.build_output_str()

    def build_output_str(self):
        """ Build the contents of the file we're going to make. """
        loadout = get_loadout(self.loadout)
        mini = MiniEncapsulator(self.original)
        verse = mini.out
        result = ("\\documentclass{amsart}\n\n"+
                  loadout+"\n\n"+
                  "\\begin{document}\n\n"+
                  verse+"\n\n"+
                  "\\end{document}")
        return result

    def save(self):
        """ Save the output to a file. """
        with open(self.path_to_output, "w") as output_file:
            output_file.write(self.output_str)

################################
# HELPER FUNCTIONS AND CLASSES #
################################

class MiniEncapsulator:
    """ Sandwich a snippet of .tex code into a verse environment. """
    def __init__(self, snippet, notes=None, poem_lines=DEFAULT_POEM_LINES):
        self.original = snippet
        self.notes = notes
        self.poem_lines = poem_lines
        self.body = self.make_body()
        self.out = self.build_output()

    def make_body(self):
        """ Ronseal. """
        result = self.original
        if self.notes:
            note_string = "\\footnotetext{"+self.notes+"}"
            if "\n" in result:
                result = result.replace("\n", note_string+"\n", 1)
            else:
                result = result+note_string
        return result

    def build_output(self):
        """ Ronseal. """
        components = []
        second_longest_line = find_second_longest_line(self.original)
        if len_line_of_latex(second_longest_line) <= MAX_WIDTH:
            components.append(
                "\\settowidth{\\versewidth}{"+second_longest_line+"}"
            )
            components.append("\\begin{verse}[\\versewidth]")
        else:
            components.append("\\begin{verse}["+FALLBACK_WIDTH_STR+"]")
        if self.poem_lines:
            components.append("\\poemlines{"+str(self.poem_lines)+"}")
        components.append(self.body)
        components.append("\\end{verse}")
        result = "\n".join(components)
        return result

    def digest(self):
        """ Deprecated. """
        return self.out

def remove_line_endings(line):
    """ Remove any line-ending syntax. """
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

def detect_unpaired_braces(line):
    """ Ronseal. """
    n = 0
    for i in range(len(line)):
        if line[i] == "{":
            n = n+1
        elif line[i] == "}":
            n = n-1
    return n

def remove_unpaired_braces(line):
    """ Ronseal. """
    while line.startswith("{") and (detect_unpaired_braces(line) > 0):
        line = line[1:len(line)-1]
    while line.endswith("}") and (detect_unpaired_braces(line) < 0):
        line = line[0:len(line)-2]
    return line

def get_loadout(loadout_name):
    """ Gets the list of packages (and related) from the database. """
    filename = loadout_name+".tex"
    path_to_loadout = str(PATH_OBJ_TO_PACKAGE_LOADOUTS/filename)
    with open(path_to_loadout, "r") as loadout_file:
        result = loadout_file.read()
    return result

def len_line_of_latex(line):
    """ Find the printed length of a line of LaTeX. """
    line = re.sub(r"\\\w*{([^}]*)}", "\\1", line)
    result = len(line)
    return result

def find_second_longest_line(snippet):
    """ Ronseal. """
    lines = snippet.split("\n")
    longest_line = lines[0]
    second_longest_line = lines[0]
    for line in lines:
        if len_line_of_latex(line) > len_line_of_latex(longest_line):
            second_longest_line = longest_line
            longest_line = line
        elif len_line_of_latex(line) > len_line_of_latex(second_longest_line):
            second_longest_line = line
    second_longest_line = remove_line_endings(second_longest_line)
    second_longest_line = remove_unpaired_braces(second_longest_line)
    return second_longest_line
