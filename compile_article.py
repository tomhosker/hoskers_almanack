### This code compiles a specific article in the database into a PDF.

# Imports.
import sqlite3, os, sys

# Local imports.
import constants
from article import Article
from bib_builder import build_bib

# Fetches the package loadout from the database.
def fetch_loadout():
  conn = sqlite3.connect(constants.db)
  c = conn.cursor()
  select = "SELECT latex FROM package_loadout WHERE name = 'main';"
  c.execute(select)
  row = c.fetchone()
  result = row[0]
  return result

# The function in question.
def compile_article(idno):
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
  f = open("current.tex", "w")
  f.write(current)
  f.close()
  os.system("xelatex current.tex")
  os.system("bibtex current.aux")
  os.system("xelatex current.tex")
  os.system("cp current.pdf "+str(idno)+".pdf")
  os.system("rm -rf current*")
  os.system("rm sources.bib")
  return True

# Run and wrap up.
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
run()
