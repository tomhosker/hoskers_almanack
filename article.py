### This file holds a class which constructs the LaTeX for a given article.

# Imports.
import sqlite3

# Local imports.
import constants
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
  def __init__(self, idno, fullness):
    self.idno = idno
    self.fullness = fullness
    self.hpml = None
    self.tune = None
    self.christ_flag = False
    self.notes = None
    self.article = None
    self.not_on_db = False
    self.fetch_fields()
    if self.not_on_db == False:
      self.notes = Notes_builder(self.idno, self.fullness).digest()
      self.article = self.build_article()

  # Fetches the required data from the database.
  def fetch_fields(self):
    conn = sqlite3.connect(constants.db)
    c = conn.cursor()
    select = "SELECT content, tune, christFlag FROM article WHERE id = ?;"
    c.execute(select, (self.idno,))
    row = c.fetchone()
    if len(row) == 3:
      self.hpml = row[0]
      self.tune = row[1]
      if row[2] == 1:
        self.christ_flag = True
    else:
      self.not_on_db = True

  # Sews the class's fields together.
  def build_article(self):
    latex = to_latex(self.hpml)
    if self.christ_flag:
      latex = "{\\color{red} "+latex+"}"
    if self.tune != None:
      latex = ("\\begin{center}\n"+
               "\\textit{Tune: "+self.tune+"}\n"+
               "\\end{center}\n\n")+latex
    footnote = "\\footnotetext{"+self.notes+"}"
    result = footnote+latex
    return result

  # Returns the class's product as a string.
  def digest(self):
    return self.article

# Run a demo.
def demo():
  print(Article(95, "full").digest())

# Run and wrap up.
def run():
  demo()
#run()
