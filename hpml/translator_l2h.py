"""
This code defines a class which can translate LaTeX back into HPML.
"""

# Local imports.
from lexicon import lexicon

##############
# MAIN CLASS #
##############

class TranslatorL2H:
    """ The class in question. """
    def __init__(self, source_file=None, source_string=None):
        self.source_file = source_file
        self.source_string = source_string
        if self.source_string is None:
            with open(self.source_file, "r") as fileobj:
                self.source_s = f.read()
        self.lines = self.source_string.split("\n")
        self.out = self.build_out()

    def purge_endings(self):
        """ Purge LaTeX line endings from each line. """
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

    def translate_equivalents(self):
        """ Translate those clusters for which clear equivalents exist. """
        for line in self.lines:
            i = self.lines.index(line)
            for entry in lexicon:
                while entry[0] in line:
                    line = line.replace(entry[0], entry[1])
            self.lines[i] = line

    def build_out(self):
        """ Ronseal. """
        result = ""
        self.purge_endings()
        self.translate_equivalents()
        for line in self.lines:
            if self.lines.index(line) == len(self.lines)-1:
                result = result+line
            else:
                result = result+line+"\n"
        return result

    def return_translation(self):
        """ Return a string containing the translation. """
        return self.out

    def save_translation(self, filename=None):
        """ Ronseal. """
        if not filename:
            if not self.source_file:
                filename = "translation.hpml"
            elif self.source_f.endswith(".tex"):
                index = self.source_file.index(".tex")
                filename = self.source_file[0:index]+".hpml"
            else:
                filename = self.source_file+".hpml"
        with open(filename, "w") as fileobj:
            fileobj.write(self.out)

def demo():
    """ Run unit tests. """
    t = Translator_L2H("test1.tex", None)
    t.save_translation(None)
    print(t.return_translation())

# Run and wrap up.
def run():
    demo()
#run()
