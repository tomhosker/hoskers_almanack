"""
This code provides a concise entry-point for the using the PDFBuilder class.
"""

# Standard imports.
import sys

# Local imports.
from pdf_builder import PDFBuilder

# Configurations.
FULLNESS = "full" # Options: full, slender.
MODS = [] # See hpml/preprocessor.py for strings you can put in this list.

#############
# FUNCTIONS #
#############

def compile_almanack(quiet=False):
    """ Compile the Almanack with the above configurations. """
    builder = PDFBuilder(fullness=FULLNESS, mods=MODS, quiet=quiet)
    builder.build()

###################
# RUN AND WRAP UP #
###################

def run():
    if "--test" in sys.argv:
        compile_almanack(quiet=True)
    else:
        compile_almanack()

if __name__ == "__main__":
    run()
