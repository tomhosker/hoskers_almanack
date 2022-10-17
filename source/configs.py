"""
This code defines a number of constants used by the project as a whole.
"""

# Standard imports.
from pathlib import Path

###########
# CONFIGS #
###########

# Filenames.
BASE_TEX = "base.tex"
MAIN_STEM = "main"
MAIN_TEX = MAIN_STEM+".tex"
MAIN_AUX = MAIN_STEM+".aux"
MAIN_PDF = MAIN_STEM+".pdf"
MAIN_BLX = MAIN_STEM+"-blx.bib"
OUTPUT_FN = "almanack.pdf"

# Paths.
PATH_OBJ_TO_BASE_DIR = Path.home()/"hoskers_almanack"
PATH_TO_DB = str(PATH_OBJ_TO_BASE_DIR/"almanack.db")
PATH_TO_OUTPUT = str(PATH_OBJ_TO_BASE_DIR/"almanack.pdf")
PATH_TO_BIB = str(PATH_OBJ_TO_BASE_DIR/"sources.bib")
PATH_OBJ_TO_TEX = Path(__file__).parent/"tex"
PATH_OBJ_TO_PACKAGE_LOADOUTS = PATH_OBJ_TO_TEX/"package_loadouts"

# Fullness.
FULL = "full"
SLENDER = "slender"
MINIMAL = "minimal"
FULLNESS = FULL

# Column keys.
CHRIST_FLAG_KEY = "christ_flag"
CONTENT_KEY = "content"
ID_KEY = "id"
IS_PROSE_POEM_KEY = "is_prose_poem"
NAME_KEY = "name"
PROVERB_KEY = "proverb"
PROVERBS_KEY = "proverbs"
SONG_KEY = "song"
SONGS_KEY = "songs"
SONNET_KEY = "sonnet"
SONNETS_KEY = "sonnets"
TUNE_KEY = "tune"

# Month names.
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
MONTH_NAMES = MONTH_NAMES_LATIN

# Other.
LOADOUT_ID = "main"
MODS = None # See hpml/preprocessor.py for strings you can put in here.
SPECIAL_RANKINGS = {
    101: "Assigned to the second most senior month.",
    102: "Assigned to the least senior month.",
    200: "Shortlisted.",
    999: "Not listed."
}
VERSION = "First Proof"
