"""
This code defines a class which constructs the LaTeX for a given article.
"""

# Standard imports.
from dataclasses import dataclass, field

# Bespoke imports.
from hpml import HPMLCompiler

# Local imports.
from .utils import AlmanackError, decode_article_type, fetch_to_dict
from .constants import (
    ArticleType,
    ColumnNames,
    Fullnesses,
    POETIC_PROVERB_GIVEAWAYS
)
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
    article_type: ArticleType = field(init=False, default=None)
    content: str = field(init=False, default=None)
    tune: str = field(init=False, default=None)
    is_prose_poem: bool = field(init=False, default=False)
    christ_flag: bool = field(init=False, default=False)
    formatted_content: str = field(init=False, default=None)
    notes: str = field(init=False, default=None)

    def __post_init__(self):
        self.fill_attributes()

    def fill_attributes(self):
        """ Fetches the required data from the database. """
        row = fetch_article(self.record_id)
        if not row:
            raise AlmanackError(f"No article with id: {self.record_id}")
        self.article_type = decode_article_type(row[ColumnNames.TYPE.value])
        self.content = row[ColumnNames.CONTENT.value]
        self.tune = row[ColumnNames.TUNE.value]
        self.is_prose_poem = bool(row[ColumnNames.IS_PROSE_POEM.value])
        self.christ_flag = bool(row[ColumnNames.CHRIST_FLAG.value])
        self.formatted_content = self.get_formatted_content()
        self.notes = self.build_notes()

    def get_formatted_content(self) -> str:
        """ Compile content as necessary. """
        if (
            is_prose_proverb(self.content) and
            self.article_type == ArticleType.PROVERB
        ):
            return self.content
        return self.compile_hpml()

    def compile_hpml(self) -> str:
        """ Convert a snippet of HPML into (encapsulated) LaTeX code. """
        compiler = \
            HPMLCompiler(
                input_string=self.content,
                is_prose_poem=self.is_prose_poem
            )
        result = compiler.compile()
        return result

    def build_notes(self) -> str:
        """ Ronseal. """
        builder = NotesBuilder(self.record_id, self.fullness)
        result = builder.digest()
        return result

    def digest(self) -> str:
        """ Return a LaTeX representation of the whole article. """
        result = self.formatted_content
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
        result = "\\footnotetext{"+self.notes+"}"+result
        return result

####################
# HELPER FUNCTIONS #
####################

def fetch_article(record_id: int) -> dict|None:
    """ Return the record for a given article. """
    select = "SELECT * FROM Article WHERE id = ?;"
    extract = fetch_to_dict(select, (record_id,))
    if extract:
        result = extract[0]
        return result
    return None

def is_prose_proverb(syntax: str) -> bool:
    """ Decide whether a given proverb is in prose or poetry. """
    for giveaway in POETIC_PROVERB_GIVEAWAYS:
        if giveaway in syntax:
            return False
    return True
