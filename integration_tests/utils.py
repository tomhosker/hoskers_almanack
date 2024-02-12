"""
This code defines some utility functions.
"""

# Standard imports.
import sqlite3
import subprocess
from pathlib import Path

# Local constants.
PATH_TO_DB = str(Path(__file__).parent.parent/"almanack.db")
LATEX_COMMAND = "xelatex"
TIMEOUT = 10 # seconds

#############
# FUNCTIONS #
#############

def fetch_to_dict(select, parameters=None, path_to_db=PATH_TO_DB):
    """ Runs a "SELECT" query, and wraps the results into a dictionary. """
    if not parameters:
        parameters = []
    connection = sqlite3.connect(path_to_db)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute(select, parameters)
    extract = cursor.fetchall()
    connection.close()
    rows = []
    for item in extract:
        row = dict(item)
        rows.append(row)
    return rows

def compile_latex(path_to_tex, quiet=False):
    """ Compile a given file of LaTeX code into a PDF. """
    commands = [LATEX_COMMAND, path_to_tex]
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
