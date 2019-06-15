### This code compiles a specific article in the database into a PDF.

# Imports.
import sqlite3, os, sys

# Local imports.
import constants
from article import Article

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
  loadout = fetch_loadout()
  article = Article(idno, "full").digest()
  current = ("\\documentclass{amsart}\n\n"+
             loadout+"\n\n"+
             "\\begin{document}\n"+
             article+
             "\\end{document}")
  f = open("current.tex", "w")
  f.write(current)
  f.close()
  os.system("xelatex current.tex")
  os.system("cp current.pdf "+str(idno)+".pdf")
  os.system("rm -rf current*")

# Run and wrap up.
if len(sys.argv) <= 1:
  print("Please specify which article to compile (by its ID).")
else:
  idno = int(sys.argv[1])
  compile_article(idno)
