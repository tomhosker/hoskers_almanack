"""
This code defines a class which builds the contents of a given month.
"""

# Standard imports.
from dataclasses import dataclass

# Local imports.
from .utils import fetch_to_dict
from .article import Article
from .configs import (
    DEFAULT_SEPARATOR,
    INTER_DAY_SEPARATOR
)
from .constants import ColumnNames, Fullnesses

##############
# MAIN CLASS #
##############

@dataclass
class MonthBuilder:
    """ The class in question. """
    num: str
    public_name: str
    fullness: Fullnesses = Fullnesses.FULL
    mods: list = None
    songs: list = None
    sonnets: list = None
    proverbs: list = None

    def __post_init__(self):
        self.songs = self.fetch_articles(1)
        self.sonnets = self.fetch_articles(2)
        self.proverbs = self.fetch_articles(3)

    def fetch_articles(self, article_type: int) -> str:
        """ Fetch a given set of articles from the database. """
        select = (
            "SELECT * "+
            "FROM Article "+
            f"WHERE type = {article_type} AND month = {self.num} "+
            "ORDER BY day ASC;"
        )
        result = fetch_to_dict(select)
        return result

    def digest(self):
        """ Condense the month into a single string. """
        min_count = \
            min([len(self.songs), len(self.sonnets), len(self.proverbs)])
        components = []
        for index in range(min_count):
            song_obj = \
                Article(
                    self.songs[index][ColumnNames.ID.value],
                    fullness=self.fullness,
                    mods=self.mods
                )
            sonnet_obj = \
                Article(
                    self.sonnets[index][ColumnNames.ID.value],
                    fullness=self.fullness,
                    mods=self.mods
                )
            proverb_obj = \
                Article(
                    self.proverbs[index][ColumnNames.ID.value],
                    fullness=self.fullness,
                    mods=self.mods
                )
            section_digest = \
                make_section_digest(
                    song_obj.digest(),
                    sonnet_obj.digest(),
                    proverb_obj.digest()
                )
            components.append(section_digest)
        result = INTER_DAY_SEPARATOR.join(components)
        result = f"\\chapter{{{self.public_name}}}\n\n{result}"
        return result

####################
# HELPER FUNCTIONS #
####################

def dress_article(content: str) -> str:
    """
    Get the latex for a given song, sonnet or proverb, including the heading
    code, etc.
    """
    components = [
        "\\subsection{}",
        "\\nopagebreak",
        content
    ]
    result = DEFAULT_SEPARATOR.join(components)
    return result

def make_section_digest(
    song_digest: str,
    sonnet_digest: str,
    proverb_digest: str
) -> str:
    """ Construct a string giving the full code for a given section. """
    components = [
        "\\section{}",
        dress_article(song_digest),
        "\\Needspace{5\\baselineskip}",
        dress_article(sonnet_digest),
        dress_article(proverb_digest),
    ]
    result = DEFAULT_SEPARATOR.join(components)
    return result