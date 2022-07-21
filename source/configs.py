"""
This code defines a number of constants used by the project as a whole.
"""

# Standard imports.
from pathlib import Path

###########
# CONFIGS #
###########

# Paths.
PATH_OBJ_TO_REPO = Path.home()/"hoskers_almanack"
PATH_TO_DB = str(PATH_OBJ_TO_REPO/"almanack.db")
PATH_TO_OUTPUT = str(PATH_OBJ_TO_REPO/"almanack.pdf")
PATH_TO_BIB = str(PATH_OBJ_TO_REPO/"sources.bib")

# Other.
VERSION = "First Proof"
FULLNESS = "full" # Options: full, slender.
MODS = [] # See hpml/preprocessor.py for strings you can put in this list.
MONTH_NAMES = (
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
SPECIAL_RANKINGS = {
    101: "Assigned to the second most senior month.",
    102: "Assigned to the least senior month.",
    200: "Shortlisted.",
    999: "Not listed."
}
