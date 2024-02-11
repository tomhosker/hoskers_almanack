"""
This code defines a class which builds the contents of a given month.
"""

# Local imports.
from .almanack_utils import fetch_to_dict
from .article import Article
from .configs import SECTION_SEPARATOR
from .constants import ColumnNames, Fullnesses
from .monthly_selects import SELECTS

##############
# MAIN CLASS #
##############

class MonthBuilder:
    """ The class in question. """
    def __init__(self, name, fullness=Fullnesses.FULL, mods=None):
        self.name = name
        self.fullness = fullness
        self.mods = mods
        self.songs = fetch_to_dict(SELECTS[self.name].songs)
        self.sonnets = fetch_to_dict(SELECTS[self.name].sonnets)
        self.proverbs = fetch_to_dict(SELECTS[self.name].proverbs)

    def digest(self):
        """ Condense the month into a single string. """
        min_count = \
            min([len(self.songs), len(self.sonnets), len(self.proverbs)])
        components = ["\\chapter{"+self.name+"}"]
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
            components.append("\\section{}")
            components.append("\\subsection{}")
            components.append(song_obj.digest())
            components.append("\\subsection{}")
            components.append(sonnet_obj.digest())
            components.append("\\subsection{}")
            components.append(proverb_obj.digest())
        result = SECTION_SEPARATOR.join(components)
        return result
