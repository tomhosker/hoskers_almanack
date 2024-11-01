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

class ArticleType(Enum):
    """ Ronseal. """
    SONG = 1
    SONNET = 2
    PROVERB = 3

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
    PATH_TO_ARTICLE_BASE = str(PATH_OBJ_TO_TEX/"article_base.tex")

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
    TYPE = "type"
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
    TITLE_PAGE = "#TITLE_PAGE"
    FRONTMATTER = "#FRONTMATTER"
    MAINMATTER = "#MAINMATTER"
    BACKMATTER = "#BACKMATTER"
    PRINCIPLES = "#PRINCIPLES"

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

INTERNAL_MONTH_NAMES = MONTH_NAMES_LATIN

MONTH_NAMES_ENGLISH = (
    "Sore Eyes",  # alias Worm, Crow, Sap, Sugar. 25 Mar 2024.
    "Egg",  # alias Pink, Fish. 24 Apr 2024.
    "Milk",  # alias Flower. 23 May 2024.
    "Flower",  # alias Strawberry. 22 Jun 2024.
    "Hay",  # alias Buck, Thunder, Ripe Corn. 21 Jul 2024.
    "Grain",  # alias Sturgeon. 19 Aug 2024.
    "Harvest",  # 18 Sep 2024.
    "Hunters",  # 17 Oct 2024
    "Frost",  # alias Blood, Beaver. 15 Nov 2024.
    "Long Night",  # alias Cold. 15 Dec 2024.
    "Wolf",  # 25 Jan 2024.
    "Snow",  # alias Hunger. 24 Feb 2024.
    "Blue"
)

########
# MISC #
########

POETIC_PROVERB_GIVEAWAYS = ("#", "\n")
