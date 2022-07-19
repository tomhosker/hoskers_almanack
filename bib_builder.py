"""
This code builds a BibTeX bibliography from the database.
"""

# Standard imports.
import os
import sqlite3
import sys

# Local imports.
import constants
import almanack_utils

# Local constants.
PATH_TO_BIB = "sources.bib"

#############
# FUNCTIONS #
#############

def fetch_sources():
    """ Ronseal. """
    select = "SELECT * FROM source ORDER BY code;"
    sources = almanack_utils.fetch_to_dict(select, tuple())
    return sources

def wipe_bib():
    """ Ronseal. """
    if os.path.exists(PATH_TO_BIB):
        os.remove(PATH_TO_BIB)
    os.system("touch "+PATH_TO_BIB)

def build_bib():
    """ Builds our .bib file. """
    sources = fetch_sources()
    wipe_bib()
    with open("sources.bib", "a") as fileobj:
        for source in sources:
            code = source["code"]
            keywords = source["keywords"]
            if source["author"] is None:
                author = ""
            else:
                author = source["author"]
            title = source["title"]
            if source["year"] is None:
                year = ""
            else:
                year = str(source["year"])
            if source["editor"] is None:
                editor = ""
            else:
                editor = source["editor"]
            if source["translator"] is None:
                translator = ""
            else:
                translator = source["translator"]
            fileobj.write("@book{"+code+",\n")
            fileobj.write("    keywords = \""+keywords+"\",\n")
            fileobj.write("    author = \""+author+"\",\n")
            fileobj.write("    title = \""+title+"\",\n")
            fileobj.write("    year = \""+year+"\",\n")
            fileobj.write("    editor = \""+editor+"\",\n")
            fileobj.write("    translator = \""+translator+"\"\n")
            fileobj.write("}\n\n")

###################
# RUN AND WRAP UP #
###################

def run():
    if "--test" not in sys.argv:
        build_bib()

if __name__ == "__main__":
    run()
