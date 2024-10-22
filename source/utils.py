"""
This is a place to store some useful functions for use across this
repository.
"""

# Standard imports.
import sqlite3
import subprocess
from pathlib import Path

# Local imports.
from .constants import ArticleType, Paths, ShellCommands

# Local constants.
PATH_OBJ_TO_BACKMATTER = Path(__file__).parent.parent/"backmatter"
PATH_OBJ_TO_FRONTMATTER = Path(__file__).parent.parent/"frontmatter"

###########
# CLASSES #
###########

class AlmanackError(Exception):
    """ A custom exception. """

#############
# FUNCTIONS #
#############

def fetch_to_dict(select, parameters=None, path_to_db=Paths.PATH_TO_DB.value):
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

def get_loadout(loadout_name):
    """ Gets the list of packages (and related) from the database. """
    filename = loadout_name+".tex"
    path_to_loadout = str(Path(Paths.PATH_TO_PACKAGE_LOADOUTS.value)/filename)
    with open(path_to_loadout, "r") as loadout_file:
        result = loadout_file.read()
    return result

def compile_latex(path_to_tex, quiet=False):
    """ Compile a given file of LaTeX code into a PDF. """
    commands = [ShellCommands.LATEX_COMMAND.value, path_to_tex]
    if quiet:
        try:
            subprocess.run(commands, stdout=subprocess.DEVNULL, check=True)
        except subprocess.CalledProcessError:
            return False
    else:
        try:
            subprocess.run(commands, check=True)
        except subprocess.CalledProcessError:
            return False
    return True

def run_bibtex(path_to_aux, quiet=False):
    """ Generate the bibliography. """
    commands = [ShellCommands.BIBTEX_COMMAND.value, path_to_aux]
    if quiet:
        try:
            subprocess.run(commands, stdout=subprocess.DEVNULL, check=True)
        except subprocess.CalledProcessError:
            return False
    else:
        try:
            subprocess.run(commands, check=True)
        except subprocess.CalledProcessError:
            return False
    return True

def decode_article_type(type_int: int) -> ArticleType:
    """ Match a type-indicating integer to a type. """
    for type_obj in ArticleType:
        if type_obj.value == type_int:
            return type_obj
    raise AlmanackError("Unable to decode article type int: {type_int}")
