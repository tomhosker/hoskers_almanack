"""
This code builds a BibTeX bibliography from the database.
"""

# Standard imports.
import os
from pathlib import Path

# Local imports.
if __package__:
    from . import configs
else:
    import configs
from .almanack_utils import fetch_to_dict

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
    select = "SELECT * FROM source ORDER BY code;"
    sources = fetch_to_dict(select, tuple())
    return sources

def wipe_bib(path_to_bib=configs.PATH_TO_BIB):
    """ Ronseal. """
    if Path(path_to_bib).exists():
        os.remove(path_to_bib)

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
    with open(configs.PATH_TO_BIB, "a") as fileobj:
        for source in sources:
            fileobj.write(get_book_summary(source))

###################
# RUN AND WRAP UP #
###################

def run():
    build_bib()

if __name__ == "__main__":
    run()
