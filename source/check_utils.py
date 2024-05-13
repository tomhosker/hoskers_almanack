"""
This code defines some utility functions.
"""

# Standard imports.
import subprocess

# Local imports.
from .constants import ShellCommands

# Local constants.
TIMEOUT = 10 # seconds
TEMP_TEX_FN = "temp.tex"
TEMP_PDF_FN = "temp.pdf"

#############
# FUNCTIONS #
#############

def check_compile_latex(path_to_tex, quiet=False):
    """ Compile a given file of LaTeX code into a PDF. """
    commands = [ShellCommands.LATEX_COMMAND.value, path_to_tex]
    if quiet:
        try:
            subprocess.run(
                commands,
                stdout=subprocess.DEVNULL,
                check=True,
                timeout=TIMEOUT
            )
        except subprocess.CalledProcessError:
            return False
    else:
        try:
            subprocess.run(commands, check=True)
        except subprocess.CalledProcessError:
            return False
    return True
