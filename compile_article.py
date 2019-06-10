### This code compiles a specific article in the database into a PDF.

# Imports.
import sqlite3, os, sys

# Local imports.
from hpml.hpml_compiler import HPML_compiler
from encapsulator import Encapsulator

# The function in question.
def compile_article(idno):
  conn = sqlite3.connect("almanack.db")
  c = conn.cursor()
  select = "SELECT content FROM article WHERE id = ?;"
  c.execute(select, (idno,))
  extract = c.fetchone()
  hpml = extract[0]
  compiler = HPML_compiler(None, hpml)
  latex = compiler.digest()
  encapsulator = Encapsulator(latex, "slim")
  encapsulator.save()
  os.system("xelatex current.tex")
  os.system("cp current.pdf "+str(idno)+".pdf")
  os.system("rm -rf current*")

# Run and wrap up.
if len(sys.argv) <= 1:
  print("Please specify which article to compile (by its ID).")
else:
  idno = int(sys.argv[1])
  compile_article(idno)
