### This code holds a class which conducts an audit of the NOTES to the
### articles in the database.

# Imports.
import sqlite3, os, multiprocessing

# Local imports.
from notes_builder import Notes_builder

# The class in question.
class Notes_auditor:
  def __init__(self):
    self.idnos = None
    self.collect_idnos()
    self.loadout = None
    self.fill_loadout()
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

  # Fetch the correct loadout from the database.
  def fill_loadout(self):
    conn = sqlite3.connect("almanack.db")
    c = conn.cursor()
    select = "SELECT latex FROM package_loadout WHERE name = 'main';"
    c.execute(select)
    readout = c.fetchone()
    self.loadout = readout[0]

  # Ronseal.
  def run_xelatex(self):
    self.screentext = os.popen("xelatex current.tex").read()

  # Attempt to compile an article, and kill the process if necessary.
  def attempt_to_compile(self):
    p = multiprocessing.Process(target=self.run_xelatex(),
                                name="run_xelatex",
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
    notes = Notes_builder(idno).digest()
    tex = ("\\documentclass{amsart}\n\n"+self.loadout+"\n\n"+
           "\\begin{document}\n\n"+notes+"\n\n"+"\\end{document}")
    f = open("current.tex", "w")
    f.write(tex)
    f.close()
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

Notes_auditor()
