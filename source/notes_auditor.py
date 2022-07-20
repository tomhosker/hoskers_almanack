"""
This code defines a class which conducts an audit of the notes to the
articles in the database.
"""

# Standard imports.
import multiprocessing
import os
import sqlite3
import sys

# Local imports.
import configs
from notes_builder import NotesBuilder

##############
# MAIN CLASS #
##############

class NotesAuditor:
    """ The class in question. """
    def __init__(self):
        self.idnos = None
        self.collect_idnos()
        self.loadout = None
        self.fill_loadout()
        self.reset_report()
        self.screentext = ""

    def reset_report(self):
        """ Scrub the report. """
        with open("audit.txt", "w") as audit_file:
            audit_file.write("")

    def write_to_report(self, line):
        """ Ronseal. """
        with open("audit.txt", "a") as audit_file:
            audit_file.write(line+"\n")

    def collect_idnos(self):
        """ Collect the ID nos of all articles on the database. """
        conn = sqlite3.connect(configs.PATH_TO_DB)
        cursor = conn.cursor()
        select = "SELECT id FROM article;"
        cursor.execute(select)
        readout = cursor.fetchall()
        idnos = []
        for item in readout:
            idnos.append(item[0])
        idnos.sort()
        self.idnos = idnos
        conn.close()

    def fill_loadout(self):
        """ Fetch the correct loadout from the database. """
        conn = sqlite3.connect(configs.PATH_TO_DB)
        cursor = conn.cursor()
        select = "SELECT latex FROM package_loadout WHERE name = 'main';"
        cursor.execute(select)
        readout = cursor.fetchone()
        self.loadout = readout[0]
        conn.close()

    def run_xelatex(self):
        """ Ronseal. """
        self.screentext = os.popen("xelatex current.tex").read()

    def attempt_to_compile(self):
        """ Attempt to compile an article, and kill the process if
        necessary. """
        process = multiprocessing.Process(target=self.run_xelatex(),
                                          name="run_xelatex", args=tuple())
        process.start()
        process.join(3)
        if process.is_alive():
            process.terminate()
            process.join()
            return False
        return True

    def audit(self, idno):
        """ Audit one article. """
        notes = NotesBuilder(idno, "full").out
        tex = ("\\documentclass{amsart}\n\n"+self.loadout+"\n\n"+
               "\\begin{document}\n\n"+notes+"\n\n"+"\\end{document}")
        with open("current.tex", "w") as current_file:
            current_file.write(tex)
        if not self.attempt_to_compile():
            self.write_to_report(str(idno)+": Would not compile.")
        elif "!" in self.screentext:
            self.write_to_report(str(idno)+": ERROR.")
        elif (("Runaway argument?" in self.screentext) or
              ("Underfull" in self.screentext) or
              ("Overfull" in self.screentext) or
              ("Warning" in self.screentext)):
            self.write_to_report(str(idno)+": warning.")

    def run_me(self):
        """ Ronseal. """
        for idno in self.idnos:
            print("Auditing notes on article with id="+str(idno)+"...")
            self.audit(idno)

###################
# RUN AND WRAP UP #
###################

def run():
    auditor = NotesAuditor()
    if "--test" not in sys.argv:
        auditor.run_me()

if __name__ == "__main__":
    run()
