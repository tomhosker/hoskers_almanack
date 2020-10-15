"""
This code defines a class which constructs the LaTeX for a given article.
"""

# Path voodoo.
import sys
sys.path.append("hpml")

# Standard imports.
import sqlite3

# Local imports.
import constants
from encapsulator import MiniEncapsulator
from hpml_compiler import HPMLCompiler
from preprocessor import Preprocessor
from notes_builder import NotesBuilder

##############
# MAIN CLASS #
##############

# The class in question.
class Article:
    def __init__(self, idno, fullness="full", mods=None):
        self.idno = idno
        self.fullness = fullness
        self.mods = mods
        self.hpml = None
        self.tune = None
        self.christ_flag = False
        self.notes = None
        self.article = None
        self.not_on_db = False
        self.fetch_fields()
        if self.not_on_db:
            return
        self.preprocess()
        self.notes = NotesBuilder(self.idno, self.fullness).out
        self.out = self.build_article()

    def fetch_fields(self):
        """ Fetches the required data from the database. """
        conn = sqlite3.connect(constants.db)
        cursor = conn.cursor()
        select = ("SELECT content, tune, christFlag "+
                  "FROM article WHERE id = ?;")
        cursor.execute(select, (self.idno,))
        row = cursor.fetchone()
        conn.close()
        if not row:
            raise Exception("No article with that ID in the database.")
        elif len(row) == 3:
            self.hpml = row[0]
            self.tune = row[1]
            if row[2] == 1:
                self.christ_flag = True
        else:
            self.not_on_db = True

    def preprocess(self):
        """ Carries out any mods. """
        if not self.mods:
            return
        preprocessor = Preprocessor(self.hpml, self.mods)
        result = preprocessor.hpml
        return result

    def build_article(self):
        """ Sews the class's fields together. """
        latex = to_latex(self.hpml)
        if self.christ_flag:
            latex = "{\\color{red} "+latex+"}"
        if self.tune:
            latex = ("\\begin{center}\n"+
                     "\\textit{Tune: "+self.tune+"}\n"+
                     "\\end{center}\n\n")+latex
        footnote = "\\footnotetext{"+self.notes+"}"
        result = footnote+latex
        return result

    def digest(self):
        """ Deprecated. """
        return self.out

####################
# HELPER FUNCTIONS #
####################

def to_latex(hpml):
    """ Converts a snippet of HPML into (encapsulated) LaTeX code. """
    compiler = HPMLCompiler(source_string=hpml)
    latex = compiler.out
    mini_encapsulator = MiniEncapsulator(latex)
    result = mini_encapsulator.out
    return result

###########
# TESTING #
###########

def demo():
    """ Run a demo. """
    article = Article(95, fullness="full")
    print(article.out)

###################
# RUN AND WRAP UP #
###################

def run():
    if "--test" not in sys.argv:
        demo()

if __name__ == "__main__":
    run()
