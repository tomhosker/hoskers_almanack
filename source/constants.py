"""
This code defines a number of constants used by the project as a whole.
"""

# Standard imports.
from enum import Enum
from pathlib import Path

# Local constants.
MAIN_STEM = "main"
# Path objects.
PATH_OBJ_TO_BASE_DIR = Path.home()/"hoskers_almanack"
PATH_OBJ_TO_TEX = Path(__file__).parent/"tex"

#########
# ENUMS #
#########

class Filenames(Enum):
    """ Ronseal. """
    MAIN_TEX = MAIN_STEM+".tex"
    MAIN_AUX = MAIN_STEM+".aux"
    MAIN_PDF = MAIN_STEM+".pdf"
    MAIN_BLX = MAIN_STEM+"-blx.bib"
    OUTPUT_FN = "almanack.pdf"

class Paths(Enum):
    """ Ronseal. """
    PATH_TO_DB = str(PATH_OBJ_TO_BASE_DIR/"almanack.db")
    PATH_TO_OUTPUT = str(PATH_OBJ_TO_BASE_DIR/"almanack.pdf")
    PATH_TO_BIB = str(PATH_OBJ_TO_BASE_DIR/"sources.bib")
    PATH_TO_BASE = str(PATH_OBJ_TO_TEX/"base.tex")
    PATH_TO_PACKAGE_LOADOUTS = str(PATH_OBJ_TO_TEX/"package_loadouts")

class ShellCommands(Enum):
    """ Ronseal. """
    BIBTEX_COMMAND = "bibtex"
    LATEX_COMMAND = "xelatex"

class Fullnesses(Enum):
    """ Indicates how many footnotes, etc will be included. """
    FULL = "full"
    SLENDER = "slender"
    MINIMAL = "minimal"

class ColumnNames(Enum):
    """ Column names of the Article table. """
    ID = "id"
    TITLE = "title"
    CHRIST_FLAG = "christ_flag"
    CONTENT = "content"
    IS_PROSE_POEM = "is_prose_poem"
    TUNE = "tune"
    SOURCE = "source"
    NON_TITLE = "non_title"
    REMARKS = "remarks"
    REDACTED = "redacted"
    AUTHOR = "author"
    NON_AUTHOR = "non_author"

class Markers(Enum):
    """ These signpost places in a LaTeX base file in which additional syntax
    is to be injected. """
    VERSION = "#VERSION_STRING"
    LOADOUT = "#PACKAGE_LOADOUT"
    FRONTMATTER = "#FRONTMATTER"
    MAINMATTER = "#MAINMATTER"
    BACKMATTER = "#BACKMATTER"

###############
# MONTH NAMES #
###############

MONTH_NAMES_LATIN = (
    "Primilis",
    "Sectilis",
    "Tertilis",
    "Quartilis",
    "Quintilis",
    "Sextilis",
    "September",
    "October",
    "November",
    "December",
    "Unodecember",
    "Duodecember",
    "Intercalaris"
)
