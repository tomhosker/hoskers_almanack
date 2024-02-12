"""
This code defines a class which, for testing purposes, encapsulates some LaTeX
syntax, itself compiled from some HPML code, into a compilable form.
"""

# Standard imports.
from enum import Enum
from pathlib import Path

# Bespoke imports.
from hpml import HPMLCompiler, PACKAGE_CODE

# Local constants.
PATH_OBJ_TO_INTEGRATION_TEST_DATA = \
    Path(__file__).parent/"integration_test_data"

#########
# ENUMS #
#########

class Markers(Enum):
    """ Markers used in base.tex. """
    PACKAGES = "#PACKAGES"
    CONTENT = "#CONTENT"

##############
# MAIN CLASS #
##############

class CheckEncapsulator:
    """ The class in question. """
    def __init__(self, hpml, is_prose_poem=False):
        self.hpml = hpml
        self.is_prose_poem = is_prose_poem
        self.latex = None

    def initialise_latex(self):
        """ Ronseal. """
        self.latex = get_base()
        self.latex = self.latex.replace(Markers.PACKAGES.value, PACKAGE_CODE)

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
    path_to_base = str(PATH_OBJ_TO_INTEGRATION_TEST_DATA/"base.tex")
    with open(path_to_base, "r") as base_file:
        result = base_file.read()
    return result
