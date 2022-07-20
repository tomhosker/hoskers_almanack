"""
This code defines a script which compiles a specific article in the database
into a PDF.
"""

# Standard imports.
import sqlite3, os, sys

# Local imports.
import configs
from article import Article
from bib_builder import build_bib

#############
# FUNCTIONS #
#############

def fetch_loadout():
    """ Fetches the package loadout from the database. """
    conn = sqlite3.connect(configs.PATH_TO_DB)
    c = conn.cursor()
    select = "SELECT latex FROM package_loadout WHERE name = 'main';"
    c.execute(select)
    row = c.fetchone()
    result = row[0]
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
    current = ("\\documentclass{amsart}\n\n"+
               loadout+"\n\n"+
               "\\begin{document}\n\n"+
               article+"\n"
               "\\end{document}")
    with open("current.tex", "w") as current_fileobj:
        current_fileobj.write(current)
    os.system("xelatex current.tex")
    os.system("bibtex current.aux")
    os.system("xelatex current.tex")
    os.system("cp current.pdf "+str(idno)+".pdf")
    os.system("rm -rf current*")
    os.system("rm sources.bib")
    return True

###################
# RUN AND WRAP UP #
###################

def run():
    if len(sys.argv) <= 1:
        print("Please specify which article to compile (by its ID).")
        return
    try:
        idno = int(sys.argv[1])
    except:
        print("Please specify an article by its ID *number*.")
    else:
        compile_article(idno)

if __name__ == "__main__":
    run()
