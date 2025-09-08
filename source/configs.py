"""
This code defines a number of configs used by the project as a whole.
"""

# Local imports.
from .constants import MONTH_NAMES_ENGLISH, Fullnesses

###########
# CONFIGS #
###########

# Big handfuls.
FULLNESS = Fullnesses.FULL
LOADOUT_ID = "main"
MODS = None # For HPML.
PUBLIC_MONTH_NAMES = MONTH_NAMES_ENGLISH
VERSION = "First Proof"
#DEFAULT_FONT = "Linux Libertine O"
DEFAULT_FONT = "Junicode"
PRINT_FONT = "Junicode"

# Separators.
CHAPTER_SEPARATOR = "\n\n"
DEFAULT_SEPARATOR = "\n\n"
INTER_DAY_SEPARATOR = "\n\n\\pagebreak[4]\n\n"
COMPONENT_SEPARATOR = "~\\textperiodcentered~"

# Symbols.
REDACTED_MARKER = "$\\mathbb{R}$"
REMARKS_SYMBOL = "\\P~"

# Misc.
LINE_NUMBERS = 5  # Set to None to switch them off.