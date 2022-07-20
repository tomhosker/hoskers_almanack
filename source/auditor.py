"""
This code defines a class which conducts an audit of the articles in the
database.
"""

# Standard imports.
import os
import sqlite3
from subprocess import Popen, PIPE
from threading import Thread

# Local imports.
import configs
from hpml.hpml_compiler import HPMLCompiler
from encapsulator import Encapsulator

##############
# MAIN CLASS #
##############

class Auditor:
    """ The class in question. """
    def __init__(self, report_filename="audit.txt"):
        self.report_filename = report_filename
        self.idnos = self.collect_idnos()
        self.hpml = ""
        self.reset_report()
        self.latex_process = None
        self.screentext = ""

    def reset_report(self):
        """ Scrub the report. """
        if os.path.exists(self.report_filename):
            os.remove(self.report_filename)
        os.system("touch "+self.report_filename)

    def write_to_report(self, line):
        """ Ronseal. """
        with open(self.report_filename, "a") as fileobj:
            fileobj.write(line+"\n")

    def collect_idnos(self):
        """ Collect the ID nos of all articles on the database. """
        conn = sqlite3.connect(configs.PATH_TO_DB)
        cursor = conn.cursor()
        select = "SELECT id FROM article;"
        cursor.execute(select)
        readout = cursor.fetchall()
        conn.close()
        result = []
        for item in readout:
            result.append(item[0])
        result.sort()
        return result

    def fetch_hpml(self, idno):
        """ Fetch a numbered article from the database. """
        conn = sqlite3.connect(configs.PATH_TO_DB)
        cursor = conn.cursor()
        select = "SELECT content FROM article WHERE id = ?"
        cursor.execute(select, (idno,))
        readout = cursor.fetchone()
        conn.close()
        self.hpml = readout[0]

    def run_xelatex(self):
        """ Ronseal. """
        args = ["xelatex", "-interaction=nonstopmode", "current.tex"]
        self.latex_process = Popen(args, stdout=PIPE)
        lines = self.latex_process.stdout.readlines()
        for line in self.latex_process.stdout:
            self.screentext = self.screentext+line.decode("utf-8")+"\n"

    def attempt_to_compile(self):
        """ Attempt to compile an article, and kill the process if
        necessary. """
        thread = Thread(target=self.run_xelatex())
        thread.start()
        thread.join(3)
        if thread.is_alive():
            self.latex_process.kill()
            thread.join()
            return False
        return True

    def audit(self, idno):
        """ Audit one article. """
        self.fetch_hpml(idno)
        compiler = HPMLCompiler(source_string=self.hpml)
        latex = compiler.out
        if "#" in latex:
            self.write_to_report(str(idno)+": Untranslated HPML.")
            return
        encapsulator = Encapsulator(latex)
        encapsulator.save()
        if not self.attempt_to_compile():
            self.write_to_report(str(idno)+": WOULD NOT COMPILE.")
        elif "!" in self.screentext:
            self.write_to_report(str(idno)+": ERROR.")
        elif (("Runaway argument?" in self.screentext) or
              ("Underfull" in self.screentext) or
              ("Overfull" in self.screentext) or
              ("Warning" in self.screentext)):
            self.write_to_report(str(idno)+": warning.")

    def run_me(self):
        """ Ronseal. """
        print("Conducting audit...")
        for idno in self.idnos:
            print("Auditing article with id="+str(idno)+"...")
            self.audit(idno)
        print("Audit complete!")

###################
# RUN AND WRAP UP #
###################

def run():
    auditor = Auditor()
    if "--test" not in sys.argv:
        auditor.run_me()

if __name__ == "__main__":
    run()
