"""
This code defines a class which builds the contents of a given month.
"""

# Standard imports.
import sqlite3

# Local imports.
from .almanack_utils import fetch_to_dict
from .article import Article
from .monthly_selects import DEFAULT_SELECTS

##############
# MAIN CLASS #
##############

class MonthBuilder:
    """ The class in question. """
    def __init__(
            self, name, selects=DEFAULT_SELECTS, fullness="full", mods=None
        ):
        self.name = name
        self.selects = selects
        self.fullness = fullness
        self.mods = mods
        self.songs = fetch_to_dict(selects[self.name]["songs"], tuple())
        self.sonnets = fetch_to_dict(selects[self.name]["sonnets"], tuple())
        self.proverbs = fetch_to_dict(selects[self.name]["proverbs"], tuple())

    def digest(self):
        """ Condense the month into a single string. """
        min_count = \
            min([len(self.songs), len(self.sonnets), len(self.proverbs)])
        result = "\\chapter{"+self.name+"}\n\n"
        for index in range(min_count):
            song_obj = \
                Article(
                    self.songs[index]["id"],
                    fullness=self.fullness,
                    mods=self.mods
                )
            sonnet_obj = \
                Article(
                    self.sonnets[index]["id"],
                    fullness=self.fullness,
                    mods=self.mods
                )
            proverb_obj = \
                Article(
                    self.proverbs[index]["id"],
                    fullness=self.fullness,
                    mods=self.mods
                )
            song = song_obj.digest()
            sonnet = sonnet_obj.digest()
            proverb = proverb_obj.digest()
            result = (
                result+
                "\\bigskip\n\\bigskip\n\\section{}\n\n"+
                "\\subsection{}\n\n"+song+"\n\n"+
                "\\subsection{}\n\n"+sonnet+"\n\n"+
                "\\subsection{}\n\n"+proverb+"\n\n"
            )
        return result
