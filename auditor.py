### This code holds a class which conducts an audit of the articles in the
### database.

# Imports.
import sqlite3, os, multiprocessing

# Local imports.
from hpml.hpml_compiler import HPML_compiler
from hpml.encapsulator import Encapsulator

# The class in question.
class Auditor:
  def __init__(self):
    self.idnos = None
    self.collect_idnos()
    self.hpml = ""
    self.reset_report()
    self.screentext = ""
    self.run_class()

  # Scrub the report.
  def reset_report(self):
    f = open("audit.txt", "w")
    f.write("")
    f.close()

  # Ronseal.
  def write_to_report(self, line):
    f = open("audit.txt", "a")
    f.write(line+"\n")
    f.close()

  # Collect the ID nos of all articles on the database.
  def collect_idnos(self):
    conn = sqlite3.connect("almanack.db")
    c = conn.cursor()
    select = "SELECT id FROM article;"
    c.execute(select)
    readout = c.fetchall()
    idnos = []
    for item in readout:
      idnos.append(item[0])
    idnos.sort()
    self.idnos = idnos
    conn.close()

  # Fetch a numbered article from the database.
  def fetch_hpml(self, idno):
    conn = sqlite3.connect("almanack.db")
    c = conn.cursor()
    select = "SELECT content FROM article WHERE id = ?"
    c.execute(select, (idno,))
    readout = c.fetchone()
    self.hpml = readout[0]
    conn.close()

  # Ronseal.
  def run_pdflatex(self):
    self.screentext = os.popen("xelatex current.tex").read()

  # Attempt to compile an article, and kill the process if necessary.
  def attempt_to_compile(self):
    p = multiprocessing.Process(target=self.run_pdflatex(),
                                name="run_pdflatex",
                                args=tuple())
    p.start()
    p.join(3)
    if p.is_alive():
      p.terminate()
      p.join()
      return False
    return True

  # Audit one article.
  def audit(self, idno):
    self.fetch_hpml(idno)
    compiler = HPML_compiler(None, self.hpml)
    latex = compiler.digest()
    if "#" in latex:
      self.write_to_report(str(idno)+": Untranslated HPML.")
      return
    encapsulator = Encapsulator(latex, "slim")
    encapsulator.save()
    if self.attempt_to_compile() == False:
      self.write_to_report(str(idno)+": Would not compile.")
    elif "!" in self.screentext:
      self.write_to_report(str(idno)+": ERROR.")
    elif (("Runaway argument?" in self.screentext) or
          ("Underfull" in self.screentext) or
          ("Overfull" in self.screentext) or
          ("Warning" in self.screentext)):
      self.write_to_report(str(idno)+": warning.")

  # Ronseal.
  def run_class(self):
    for idno in self.idnos:
      print(idno)
      self.audit(idno)

Auditor()
