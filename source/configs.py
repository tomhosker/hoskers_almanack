"""
This code defines a number of configs used by the project as a whole.
"""

# Local imports.
from .constants import MONTH_NAMES_ENGLISH, Fullnesses

###########
# CONFIGS #
###########

CHAPTER_SEPARATOR = "\n\n"
COMMENT_SEPARATOR = "\\ell"
COMPONENT_SEPARATOR = "~\\textperiodcentered~"
FULLNESS = Fullnesses.FULL
LOADOUT_ID = "main"
MODS = None # For HPML.
PRE_ARTICLE_NEEDSPACE = "\\Needspace{9\\baselineskip}"
PUBLIC_MONTH_NAMES = MONTH_NAMES_ENGLISH
SECTION_SEPARATOR = "\n\n"
SUBSECTION_SEPARATOR = "\n"
VERSION = "First Proof"
DEFAULT_FONT = "CMU Serif"
PRINT_FONT = "Junicode"
REDACTED_MARKER = "$\\mathbb{R}$"
REMARKS_SYMBOL = "\\hspace{0.2em}\\lilyGlyph[raise=0.6]{scripts.segno}"