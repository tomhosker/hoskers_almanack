"""
This code builds a BibTeX bibliography from the database.
"""

# Standard imports.
from pathlib import Path

# Local imports.
from .utils import fetch_to_dict
from .constants import Paths

# Local constants.
BOOK_ATTRIBUTES = (
    "keywords",
    "author",
    "title",
    "year",
    "editor",
    "translator"
)

#############
# FUNCTIONS #
#############

def fetch_sources():
    """ Ronseal. """
    sources = fetch_to_dict("SELECT * FROM source ORDER BY code;")
    return sources

def wipe_bib(path_to_bib=Paths.PATH_TO_BIB.value):
    """ Ronseal. """
    Path(path_to_bib).unlink(missing_ok=True)

def none_to_empty(input_var):
    """ Convert a None to an empty string, and everything else to its string
    equivalent. """
    if input_var is None:
        return ""
    return str(input_var)

def get_book_summary(data):
    """ Get the portion of our .bib file corresponding to a given book. """
    result = "@book{"+data["code"]+",\n"
    for attribute in BOOK_ATTRIBUTES:
        result = (
            result+
            "    "+
            attribute+
            " = \""+
            none_to_empty(data[attribute])+
            "\",\n"
        )
    result = result+"}\n\n"
    return result

def build_bib():
    """ Build our .bib file. """
    sources = fetch_sources()
    wipe_bib()
    with open(Paths.PATH_TO_BIB.value, "a") as fileobj:
        for source in sources:
            fileobj.write(get_book_summary(source))
