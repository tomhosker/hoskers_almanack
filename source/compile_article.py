"""
This code defines a script which compiles a specific article in the database
into a PDF.
"""

# Standard imports.
import argparse
import os
import subprocess

# Local imports.
from .almanack_utils import fetch_to_dict
from .article import Article
from .bib_builder import build_bib

#############
# FUNCTIONS #
#############

def fetch_loadout(loadout_name="main"):
    """ Fetches the package loadout from the database. """
    select = "SELECT latex FROM package_loadout WHERE name = ?;"
    readout = fetch_to_dict(select, (loadout_name,))
    result = readout[0]["latex"]
    return result

def compile_article(idno):
    """ The function in question. """
    build_bib()
    loadout = fetch_loadout()
    article_object = Article(idno, "full", None)
    if article_object.not_on_db:
        print("No article with ID "+str(idno)+" on the database.")
        return False
    article = article_object.digest()
    current = (
        "\\documentclass{amsart}\n\n"+
        loadout+"\n\n"+
        "\\begin{document}\n\n"+
        article+"\n\n"+
        "\\end{document}"
    )
    with open("current.tex", "w") as current_fileobj:
        current_fileobj.write(current)
    subprocess.run(["xelatex", "current.tex"], check=True)
    subprocess.run(["bibtex", "current.aux"], check=True)
    subprocess.run(["xelatex", "current.tex"], check=True)
    os.rename("current.pdf", str(idno)+".pdf")
    for path_obj in Path.cwd().glob("current.*"):
        os.remove(str(path_obj))
    os.remove("sources.bib")
    return True

###################
# RUN AND WRAP UP #
###################

def run():
    """ Run this file. """
    parser = argparse.ArgumentParser(description="Compile a given article.")
    parser.add_argument("id-num", type=int, default=None, dest="id_num")
    arguments = parser.parse_args()
    if arguments.id_num is None:
        print("Please specify an article by its ID number.")
    else:
        compile_article(arguments.id_num)

if __name__ == "__main__":
    run()
