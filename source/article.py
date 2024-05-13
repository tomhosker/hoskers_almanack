"""
This code defines a class which constructs the LaTeX for a given article.
"""

# Standard imports.
from dataclasses import dataclass

# Bespoke imports.
from hpml import HPMLCompiler

# Local imports.
from .utils import AlmanackError, fetch_to_dict
from .constants import ColumnNames, Fullnesses
from .notes_builder import NotesBuilder

##############
# MAIN CLASS #
##############

@dataclass
class Article:
    """ The class in question. """
    record_id: int
    fullness: Fullnesses = Fullnesses.FULL
    mods: list[str] = None
    hpml: str = None
    tune: str = None
    is_prose_poem: bool = False
    christ_flag: bool = False
    compiled_hpml: str = None
    notes: str = None

    def __post_init__(self):
        self.fill_attributes()

    def fill_attributes(self):
        """ Fetches the required data from the database. """
        row = fetch_article(self.record_id)
        if not row:
            raise AlmanackError("No article with id: "+str(self.record_id))
        self.hpml = row[ColumnNames.CONTENT.value]
        self.tune = row[ColumnNames.TUNE.value]
        self.is_prose_poem = bool(row[ColumnNames.IS_PROSE_POEM.value])
        self.christ_flag = bool(row[ColumnNames.CHRIST_FLAG.value])
        self.compiled_hpml = self.compile_hpml()
        self.notes = self.build_notes()

    def compile_hpml(self):
        """ Convert a snippet of HPML into (encapsulated) LaTeX code. """
        compiler = \
            HPMLCompiler(
                input_string=self.hpml,
                is_prose_poem=self.is_prose_poem
            )
        result = compiler.compile()
        return result

    def build_notes(self):
        """ Ronseal. """
        builder = NotesBuilder(self.record_id, self.fullness)
        result = builder.digest()
        return result

    def digest(self):
        """ Return a LaTeX representation of the whole article. """
        result = self.compiled_hpml
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
        result = "\\footnote{"+self.notes+"}"+result
        return result

####################
# HELPER FUNCTIONS #
####################

def fetch_article(record_id):
    """ Return the record for a given article. """
    select = "SELECT * FROM Article WHERE id = ?;"
    extract = fetch_to_dict(select, (record_id,))
    if extract:
        result = extract[0]
        return result
    return None
