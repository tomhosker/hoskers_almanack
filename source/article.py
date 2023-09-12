"""
This code defines a class which constructs the LaTeX for a given article.
"""

# Standard imports.
import sqlite3

# Local imports.
from .almanack_utils import fetch_to_dict
from .configs import (
    CONTENT_KEY,
    TUNE_KEY,
    IS_PROSE_POEM_KEY,
    CHRIST_FLAG_KEY,
    FULL
)
from .encapsulator import MiniEncapsulator
from .notes_builder import NotesBuilder
from .hpml.hpml_compiler import HPMLCompiler
from .hpml.preprocessor import Preprocessor

##############
# MAIN CLASS #
##############

class Article:
    """ The class in question. """
    def __init__(self, idno, fullness=FULL, mods=None):
        self.idno = idno
        self.fullness = fullness
        self.mods = mods
        self.hpml = None
        self.tune = None
        self.is_prose_poem = False
        self.christ_flag = False
        self.notes = None
        self.article = None
        self.fill_attributes()

    def fill_attributes(self):
        """ Fetches the required data from the database. """
        row = fetch_article(self.idno)
        if not row:
            raise Exception("No article with id="+str(self.idno)+".")
        self.hpml = row[CONTENT_KEY]
        self.tune = row[TUNE_KEY]
        self.is_prose_poem = bool(row[IS_PROSE_POEM_KEY])
        self.christ_flag = bool(row[CHRIST_FLAG_KEY])
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

    def get_latex(self):
        """ Convert a snippet of HPML into (encapsulated) LaTeX code. """
        compiler = \
            HPMLCompiler(
                source_string=self.hpml,
                is_prose_poem=self.is_prose_poem
            )
        result = compiler.out
        mini_encapsulator = \
            MiniEncapsulator(
                result,
                notes=self.notes,
                is_prose_poem=self.is_prose_poem
            )
        result = mini_encapsulator.out
        return result

    def digest(self):
        """ Sews the class's fields together. """
        encapsulate = not self.is_prose_poem
        result = self.get_latex()
        if self.christ_flag:
            result = "{\\color{red} "+result+"}"
        if self.tune:
            result = (
                "\\begin{center}\n"+
                "\\textit{Tune: "+self.tune+"}\n"+
                "\\end{center}\n"+
                "\n"+
                result
            )
        return result

####################
# HELPER FUNCTIONS #
####################

def fetch_article(idno):
    """ Extract a list of article IDs from a select statement. """
    select = "SELECT * FROM Article WHERE id = ?;"
    extract = fetch_to_dict(select, (idno,))
    result = extract[0]
    return result
