"""
This code defines a class which, for testing purposes, encapsulates some LaTeX
syntax, itself compiled from some HPML code, into a compilable form.
"""

# Standard imports.
from enum import Enum

# Bespoke imports.
from hpml import HPMLCompiler, PACKAGE_CODE

# Local imports.
from .constants import Paths

#########
# ENUMS #
#########

class Markers(Enum):
    """ Markers used in base.tex. """
    PACKAGES = "#PACKAGES"
    CONTENT = "#CONTENT"
    TITLE = "#TITLE"

##############
# MAIN CLASS #
##############

class CheckEncapsulator:
    """ The class in question. """
    def __init__(self, hpml, is_prose_poem=False, title="Test"):
        self.hpml = hpml
        self.is_prose_poem = is_prose_poem
        self.title = title
        self.latex = None

    def initialise_latex(self):
        """ Ronseal. """
        self.latex = get_base()
        self.latex = self.latex.replace(Markers.PACKAGES.value, PACKAGE_CODE)
        self.latex = self.latex.replace(Markers.TITLE.value, self.title)

    def inject_poem(self):
        """ Compile the HPML, and introduce the resulting LaTeX into our
        output. """
        hpml_compiler = \
            HPMLCompiler(
                input_string=self.hpml,
                is_prose_poem=self.is_prose_poem
            )
        compiled_hpml = hpml_compiler.compile()
        self.latex = self.latex.replace(Markers.CONTENT.value, compiled_hpml)

    def digest(self):
        """ Return the string giving the content of the LaTeX file. """
        self.initialise_latex()
        self.inject_poem()
        return self.latex

####################
# HELPER FUNCTIONS #
####################

def get_base():
    """ Return a string giving the template into which we will insert other
    snippets of LaTeX. """
    path_to_base = str(Paths.PATH_TO_ARTICLE_BASE.value)
    with open(path_to_base, "r") as base_file:
        result = base_file.read()
    return result
