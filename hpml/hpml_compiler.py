"""
This code defines a class which compiles HPML into LaTeX.
"""

# Standard imports.
import sys

# Local imports.
from lexicon import lexicon, fractions

##############
# MAIN CLASS #
##############

class HPMLCompiler:
    """ The class in question. """
    def __init__(self, source_file=None, source_string=None):
        self.source_file = source_file
        self.source_string = source_string
        if source_string is None:
            with open(self.source_file, "r") as the_file:
                self.source_string = the_file.read()
        self.lines = self.source_string.split("\n")
        self.out = self.build_out()

    def purge_whitespace(self):
        """ Ronseal. """
        for line in self.lines:
            i = self.lines.index(line)
            # Remove whitespace from line ends.
            while line.endswith(" "):
                line = line[0:len(line)]
            self.lines[i] = line
        # Remove any remaining blank lines.
        while(self.lines[len(self.lines)-1] == ""):
            self.lines = self.lines[0:-1]

    def add_endings(self):
        """ Adds "\\", "\\*" or "\\!" to each line, as appropriate. """
        for line in self.lines:
            i = self.lines.index(line)
            if ((line == "") or (line == "{\itshape ") or
                (i == len(self.lines)-1)):
                continue
            if (i != len(self.lines)-1) and (self.lines[i+1] == ""):
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
            elif (i < len(self.lines)-2) and (self.lines[i+2] == ""):
                line = line+"\\\\*"
                self.lines[i] = line
                continue
            line = line+"\\\\"
            self.lines[i] = line

    def process_syntactics(self):
        """ Translate those clusters for which clear equivalents exist. """
        for line in self.lines:
            i = self.lines.index(line)
            for entry in lexicon.keys():
                while entry in line:
                    line = line.replace(entry, lexicon[entry])
            self.lines[i] = line

    def process_places(self):
        """ Ronseal. """
        for line in self.lines:
            i = self.lines.index(line)
            while "#PLACE{" in line:
                line = line.replace("#PLACE{", "\\textsc{")
            self.lines[i] = line

    def process_persons(self):
        """ Ronseal. """
        for line in self.lines:
            i = self.lines.index(line)
            while "#PERSON{" in line:
                line = line.replace("#PERSON{", "\\textit{")
            self.lines[i] = line

    def process_publications(self):
        """ Ronseal. """
        for line in self.lines:
            i = self.lines.index(line)
            while "#PUBLICATION{" in line:
                line = line.replace("#PUBLICATION{", "{\\hoskeroe ")
            self.lines[i] = line

    def process_foreign_strings(self):
        """ Ronseal. """
        for line in self.lines:
            i = self.lines.index(line)
            while "#FOREIGN{" in line:
                line = line.replace("#FOREIGN{", "{\\hoskeroe ")
            self.lines[i] = line

    def process_fractions(self):
        """ Ronseal. """
        for line in self.lines:
            i = self.lines.index(line)
            for entry in fractions.keys():
                while entry in line:
                    line = line.replace(entry, fractions[entry]["latex"])
                self.lines[i] = line

    def process_ampersands(self):
        """ Ronseal. """
        for line in self.lines:
            i = self.lines.index(line)
            while "#ADD" in line:
                line = line.replace("#ADD", "\&")
            self.lines[i] = line

    def process_stress(self):
        """ Handles stressed syllables. """
        for line in self.lines:
            i = self.lines.index(line)
            while "#STRESS{" in line:
                line = line.replace("#STRESS{", "\\'{")
            self.lines[i] = line

    def process_choruses(self):
        """ Handles choruses and inscriptions. """
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

    def process_minichoruses(self):
        """ Handles mini-choruses and mini-inscriptions. """
        for line in self.lines:
            i = self.lines.index(line)
            if ("##MINICHORUS" in line) or ("##MINIINSCRIPTION" in line):
                line = line.replace("##MINICHORUS ", "\\vin \\textit{")
                line = line.replace("##MINIINSCRIPTION ", "\\textit{")
                line = line+"}"
                self.lines[i] = line

    def process_flagverses(self):
        """ Adds mini-titles to particular verses. """
        for line in self.lines:
            i = self.lines.index(line)
            line = line.replace("##FLAGVERSE{",
                                "\\flagverse{\\footnotesize ")
            self.lines[i] = line

    def process_subscript(self):
        """ Ronseal. """
        for line in self.lines:
            i = self.lines.index(line)
            while "#SUB{" in line:
                line = line.replace("#SUB{", "\\textsubscript{")
            self.lines[i] = line

    def process_whitespace(self):
        """ Ronseal. """
        for line in self.lines:
            i = self.lines.index(line)
            while "#WHITESPACE{" in line:
                line = line.replace("#WHITESPACE{", "\\textcolor{white}{")
            self.lines[i] = line

    def process_semantics(self):
        """ Ronseal. """
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

    def build_out(self):
        """ Ronseal. """
        result = ""
        self.purge_whitespace()
        self.process_choruses()
        self.process_minichoruses()
        self.add_endings()
        self.process_syntactics()
        self.process_semantics()
        for line in self.lines:
            if self.lines.index(line) == len(self.lines)-1:
                result = result+line
            else:
                result = result+line+"\n"
        return result

    def digest(self):
        """ Returns a string containing the compilation. """
        return self.out

    def save(self, filename=None):
        """ Ronseal. """
        if filename is None:
            if self.source_file is None:
                filename = "compilation.tex"
            else:
                if self.source_file.endswith(".hpml"):
                    terminus = self.source_file.index(".hpml")
                    filename = self.source_file[0:terminus]+".tex"
                else:
                    filename = self.source_file+".tex"
        with open(filename, "w") as fileobj:
            fileobj.write(self.out)

###########
# TESTING #
###########

def demo():
    """ Run a demo. """
    test_obj = HPMLCompiler(source_file="test2.hpml")
    print(test_obj.out)

###################
# RUN AND WRAP UP #
###################

def run():
    if "--test" not in sys.argv:
        demo()

if __name__ == "__main__":
    run()
