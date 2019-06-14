### This file holds a class which constructs the LaTeX for a given article.

# Imports.
import sqlite3

# Local imports.
from encapsulator import Mini_encapsulator
from hpml.hpml_compiler import HPML_compiler
from notes_builder import Notes_builder

# Converts a snippet of HPML into (encapsulated) LaTeX code.
def to_latex(hpml):
  compiler = HPML_compiler(None, hpml)
  latex = compiler.digest()
  mini_encapsulator = Mini_encapsulator(latex)
  result = mini_encapsulator.digest()
  return result

# The class in question.
class Article:
  # Class variables.
  db = "almanack.db"

  def __init__(self, idno, fullness):
    self.idno = idno
    self.fullness = fullness
    self.hpml = self.fetch_hpml()
    self.christ_flag = self.fetch_christ_flag()
    self.notes = Notes_builder(self.idno, self.fullness).digest()
    self.article = self.build_article()

  # Fetches HPML from the database.
  def fetch_hpml(self):
    conn = sqlite3.connect(Article.db)
    c = conn.cursor()
    select = "SELECT content FROM article WHERE id = ?;"
    c.execute(select, (self.idno,))
    row = c.fetchone()
    result = row[0]
    return result

  # Ronseal.
  def fetch_christ_flag(self):
    conn = sqlite3.connect(Article.db)
    c = conn.cursor()
    select = "SELECT christFlag FROM article WHERE id = ?;"
    c.execute(select, (self.idno,))
    row = c.fetchone()
    flag = row[0]
    if flag == 1:
      return True
    else:
      return False

  # Sews the class's fields together.
  def build_article(self):
    latex = to_latex(self.hpml)
    if self.christ_flag:
      latex = "{\\color{red} "+latex+"}"
    footnote = "\\footnotetext{"+self.notes+"}"
    result = footnote+latex
    return result

  # Returns the class's product as a string.
  def digest(self):
    return self.article

# Run a demo.
def demo():
  print(Article(1, "full").digest())

# Run and wrap up.
def run():
  demo()
#run()
