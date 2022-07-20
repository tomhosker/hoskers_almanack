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
from almanack_utils import fetch_to_dict
from encapsulator import MiniEncapsulator
from notes_builder import NotesBuilder
from hpml_compiler import HPMLCompiler
from preprocessor import Preprocessor

# Local constants.
PATH_TO_ARTICLE_DEMO_OUTPUT = "article_demo_output.tex"

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
        self.notes = None
        self.fill_attributes()

    def fill_attributes(self):
        """ Fetches the required data from the database. """
        row = fetch_article(self.idno)
        if not row:
            raise Exception("No article with id="+str(self.idno)+".")
        self.hpml = row["content"]
        self.tune = row["tune"]
        if row["christFlag"]:
            self.christ_flag = True
        self.preprocess()
        self.build_notes()

    def preprocess(self):
        """ Carries out any mods. """
        if not self.mods:
            return
        preprocessor = Preprocessor(self.hpml, self.mods)
        self.hpml = preprocessor.hpml

    def build_notes(self):
        """ Ronseal. """
        builder = NotesBuilder(self.idno, self.fullness)
        self.notes = builder.out

    def digest(self):
        """ Sews the class's fields together. """
        latex = to_latex(self.hpml)
        if self.christ_flag:
            latex = "{\\color{red} "+latex+"}"
        if self.tune:
            latex = (
                "\\begin{center}\n"+
                "\\textit{Tune: "+self.tune+"}\n"+
                "\\end{center}\n\n"+
                latex
            )
        if self.notes:
            footnote = "\\footnotetext{"+self.notes+"}"
            result = footnote+latex
        else:
            result = latex
        return result

####################
# HELPER FUNCTIONS #
####################

def fetch_article(idno, path_to_db=constants.PATH_TO_DB):
    """ Extract a list of article IDs from a select statement. """
    select = ("SELECT content, tune, christFlag "+
              "FROM article WHERE id = ?;")
    extract = fetch_to_dict(select, (idno,))
    result = extract[0]
    return result

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

def demo(path_to_output=PATH_TO_ARTICLE_DEMO_OUTPUT):
    """ Run a demo. """
    article = Article(95, fullness="full")
    with open(path_to_output, "w") as output_file:
        output_file.write(article.digest())

###################
# RUN AND WRAP UP #
###################

def run():
    demo()

if __name__ == "__main__":
    run()
