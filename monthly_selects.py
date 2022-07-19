"""
This code defines a class which builds a SELECT query for the songs, sonnets or
proverbs for a given month.

Example:

    SELECT id
    FROM article
    WHERE type = 1
        AND humour = 'yellow-bile'
        AND aux_type = 'n'
        AND ranking BETWEEN 1 AND 30
    ORDER BY ranking;
"""

# Local constants.
TOP_PRECEDENCE_INT = 0
MID_PRECEDENCE_INT = 1
BOTTOM_PRECEDENCE_INT = 2
MID_PRECEDENCE_CONDITION = "= 101"
BOTTOM_PRECEDENCE_CONDITION = "= 102"
STANDARD_ORDER_BY = "ORDER BY ranking, author, non_author, content"

##############
# MAIN CLASS #
##############

class MonthlySelect:
    """ The class in question. """
    def __init__(self, humour, article_type, precedence, days, override=None):
        self.humour = humour
        self.article_type = article_type
        self.precedence = precedence
        self.days = days
        self.override = override
        self.ranking_condition = self.get_ranking_condition()
        self.query = self.get_query()

    def get_ranking_condition(self):
        """ Return the ranking condition portion of the query. """
        if self.precedence == TOP_PRECEDENCE_INT:
            return "BETWEEN 1 AND "+str(self.days)
        if self.precedence == MID_PRECEDENCE_INT:
            return MID_PRECEDENCE_CONDITION
        if self.precedence == BOTTOM_PRECEDENCE_INT:
            return BOTTOM_PRECEDENCE_CONDITION
        raise Exception("Bad precedence int: "+str(self.precedence))

    def get_query(self):
        """ Return a string giving the SQL query in question. """
        if self.override:
            return self.override
        result = (
            "SELECT id "+
            "FROM article "+
            "WHERE type = "+str(self.article_type)+" "+
            "AND humour = '"+self.humour+"' "+
            "AND aux_type = 'n' "+
            "AND ranking "+self.ranking_condition+" "+
            STANDARD_ORDER_BY+";"
        )
        return result

#######################
# ONES I MADE EARLIER #
#######################

PRI_SONGS = (
    "SELECT id FROM article "+
    "WHERE type = 1 "+
        "AND humour = \"yellow-bile\" "+
        "AND aux_type = \"n\" "+
        "AND ranking BETWEEN 1 AND 30 "+
    "ORDER BY ranking;"
)
PRI_SONNETS = (
    "SELECT id FROM article "+
    "WHERE type = 2 "+
        "AND humour = \"yellow-bile\" "+
        "AND aux_type = \"n\" "+
        "AND ranking BETWEEN 1 AND 30 "+
    "ORDER BY ranking;"
)
PRI_PROVERBS = (
    "SELECT id FROM article "+
    "WHERE type = 3 "+
        "AND humour = \"yellow-bile\" "+
        "AND aux_type = \"n\" "+
        "AND ranking BETWEEN 1 AND 30 "+
    "ORDER BY ranking;"
)
SEC_SONGS = (
    "SELECT id FROM article "+
    "WHERE type = 1 "+
        "AND humour = \"yellow-bile\" "+
        "AND aux_type = \"n\" "+
        "AND ranking BETWEEN 31 AND 59 "+
    "ORDER BY ranking ;"
)
SEC_SONNETS = (
    "SELECT id FROM article "+
    "WHERE type = 2 "+
        "AND humour = \"yellow-bile\" "+
        "AND aux_type = \"n\" "+
        "AND ranking BETWEEN 31 AND 59 "+
    "ORDER BY ranking;"
)
SEC_PROVERBS = (
    "SELECT id FROM article "+
    "WHERE type = 3 "+
        "AND humour = \"yellow-bile\" "+
        "AND aux_type = \"n\" "+
        "AND ranking BETWEEN 31 AND 59 "+
    "ORDER BY ranking;"
)
TER_SONGS = (
    "SELECT id FROM article "+
    "WHERE type = 1 "+
        "AND humour = \"yellow-bile\" "+
        "AND aux_type = \"n\" "+
        "AND ranking BETWEEN 60 AND 89 "+
    "ORDER BY ranking;"
)
TER_SONNETS = (
    "SELECT id FROM article "+
    "WHERE type = 2 "+
        "AND humour = \"yellow-bile\" "+
        "AND aux_type = \"n\" "+
        "AND ranking BETWEEN 60 AND 89 "+
    "ORDER BY ranking;"
)
TER_PROVERBS = (
    "SELECT id FROM article "+
    "WHERE type = 3 "+
        "AND humour = \"yellow-bile\" "+
        "AND aux_type = \"n\" "+
        "AND ranking BETWEEN 60 AND 89 "+
    "ORDER BY ranking;"
)
QUA_SONGS = (
    "SELECT id FROM article "+
    "WHERE type = 1 "+
        "AND humour = \"blood\" "+
        "AND aux_type = \"english folk\" "+
        "AND ranking BETWEEN 1 AND 29 "+
    "ORDER BY ranking DESC;"
)
QUA_SONNETS = (
    "SELECT id FROM article "+
    "WHERE type = 2 "+
        "AND humour = \"blood\" "+
        "AND aux_type = \"n\" "+
        "AND ranking BETWEEN 30 AND 58 "+
    "ORDER BY ranking DESC;"
)
QUA_PROVERBS = (
    "SELECT id FROM article "+
    "WHERE type = 3 "+
        "AND humour = \"blood\" "+
        "AND aux_type = \"n\" "+
        "AND ranking BETWEEN 60 AND 88 "+
    "ORDER BY ranking DESC;"
)
QUI_SONGS = (
    "SELECT id FROM article "+
    "WHERE type = 1 "+
        "AND humour = \"blood\" "+
        "AND aux_type = \"scots-irish folk\" "+
        "AND ranking BETWEEN 1 AND 30 "+
    "ORDER BY ranking DESC;"
)
QUI_SONNETS = (
    "SELECT id FROM article "+
    "WHERE type = 2 "+
        "AND humour = \"blood\" "+
        "AND aux_type = \"shanty\" "+
        "AND ranking BETWEEN 1 AND 30 "+
    "ORDER BY ranking DESC;"
)
QUI_PROVERBS = (
    "SELECT id FROM article "+
    "WHERE type = 3 "+
        "AND humour = \"blood\" "+
        "AND aux_type = \"n\" "+
        "AND ranking BETWEEN 1 AND 30 "+
    "ORDER BY ranking DESC;"
)
SEX_SONGS = (
    "SELECT id FROM article "+
    "WHERE (type = 1 "+
        "AND humour = \"blood\" "+
        "AND aux_type = \"imperial folk\" "+
        "AND ranking BETWEEN 1 AND 19) "+
    "OR (type = 1 "+
        "AND humour = \"blood\" "+
        "AND aux_type = \"hymn\" "+
        "AND ranking BETWEEN 1 AND 10) "+
    "ORDER BY aux_type, ranking DESC;"
)
SEX_SONNETS = (
    "SELECT id FROM article "+
    "WHERE type = 2 "+
        "AND humour = \"blood\" "+
        "AND aux_type = \"n\" "+
        "AND ranking BETWEEN 1 AND 29 "+
    "ORDER BY ranking DESC;"
)
SEX_PROVERBS = (
    "SELECT id FROM article "+
    "WHERE type = 3 "+
        "AND humour = \"blood\" "+
        "AND aux_type = \"n\" "+
        "AND ranking BETWEEN 31 AND 59 "+
    "ORDER BY ranking DESC;"
)
SEP_SONGS = (
    "SELECT id FROM article "+
    "WHERE type = 1 "+
        "AND humour = \"phlegm\" "+
        "AND aux_type = \"n\" "+
        "AND ranking BETWEEN 1 AND 30 "+
    "ORDER BY ranking;"
)
SEP_SONNETS = (
    "SELECT id FROM article "+
    "WHERE type = 2 "+
        "AND humour = \"phlegm\" "+
        "AND aux_type = \"n\" "+
        "AND ranking BETWEEN 1 AND 30 "+
    "ORDER BY ranking;"
)
SEP_PROVERBS = (
    "SELECT id FROM article "+
    "WHERE type = 3 "+
        "AND humour = \"phlegm\" "+
        "AND aux_type = \"n\" "+
        "AND ranking BETWEEN 1 AND 30 "+
    "ORDER BY ranking;"
)
OCT_SONGS = (
    "SELECT id FROM article "+
    "WHERE type = 1 "+
        "AND humour = \"phlegm\" "+
        "AND aux_type = \"october\" "+
        "AND ranking BETWEEN 1 AND 29 "+
    "ORDER BY ranking;"
)
OCT_SONNETS = (
    "SELECT id FROM article "+
    "WHERE type = 2 "+
        "AND humour = \"phlegm\" "+
        "AND aux_type = \"october\" "+
        "AND ranking BETWEEN 1 AND 29 "+
    "ORDER BY ranking;"
)
OCT_PROVERBS = (
    "SELECT id FROM article "+
    "WHERE type = 3 "+
        "AND humour = \"phlegm\" "+
        "AND aux_type = \"october\" "+
        "AND ranking BETWEEN 1 AND 29 "+
    "ORDER BY ranking;"
)
NOV_SONGS = (
    "SELECT id FROM article "+
    "WHERE type = 1 "+
        "AND humour = \"phlegm\" "+
        "AND aux_type = \"n\" "+
        "AND ranking BETWEEN 31 AND 60 "+
    "ORDER BY ranking;"
)
NOV_SONNETS = (
    "SELECT id FROM article "+
    "WHERE type = 2 "+
        "AND humour = \"phlegm\" "+
        "AND aux_type = \"n\" "+
        "AND ranking BETWEEN 31 AND 60 "+
    "ORDER BY ranking;"
)
NOV_PROVERBS = (
    "SELECT id FROM article "+
    "WHERE type = 3 "+
        "AND humour = \"phlegm\" "+
        "AND aux_type = \"n\" "+
        "AND ranking BETWEEN 31 AND 60 "+
    "ORDER BY ranking;"
)
DEC_SONGS = (
    "SELECT id FROM article "+
    "WHERE type = 1 "+
        "AND humour = \"black-bile\" "+
        "AND aux_type = \"n\" "+
        "AND ranking BETWEEN 60 AND 88 "+
    "ORDER BY ranking DESC;"
)
DEC_SONNETS = (
    "SELECT id FROM article "+
    "WHERE type = 2 "+
        "AND humour = \"black-bile\" "+
        "AND aux_type = \"n\" "+
        "AND ranking BETWEEN 60 AND 88 "+
    "ORDER BY ranking DESC;"
)
DEC_PROVERBS = (
    "SELECT id FROM article "+
    "WHERE type = 3 "+
        "AND humour = \"black-bile\" "+
        "AND aux_type = \"n\" "+
        "AND ranking BETWEEN 60 AND 88 "+
    "ORDER BY ranking DESC;"
)
UNO_SONGS = (
    "SELECT id FROM article "+
    "WHERE type = 1 "+
        "AND humour = \"black-bile\" "+
        "AND aux_type = \"n\" "+
        "AND ranking BETWEEN 30 AND 59 "+
    "ORDER BY ranking DESC;"
)
UNO_SONNETS = (
    "SELECT id FROM article "+
    "WHERE type = 2 "+
        "AND humour = \"black-bile\" "+
        "AND aux_type = \"n\" "+
        "AND ranking BETWEEN 30 AND 59 "+
    "ORDER BY ranking DESC;"
)
UNO_PROVERBS = (
    "SELECT id FROM article "+
    "WHERE type = 3 "+
        "AND humour = \"black-bile\" "+
        "AND aux_type = \"n\" "+
        "AND ranking BETWEEN 30 AND 59 "+
    "ORDER BY ranking DESC;"
)
DUO_SONGS = (
    "SELECT id FROM article "+
    "WHERE type = 1 "+
        "AND humour = \"black-bile\" "+
        "AND aux_type = \"n\" "+
        "AND ranking BETWEEN 1 AND 29 "+
    "ORDER BY ranking DESC;"
)
DUO_SONNETS = (
    "SELECT id FROM article "+
    "WHERE type = 2 "+
        "AND humour = \"black-bile\" "+
        "AND aux_type = \"n\" "+
        "AND ranking BETWEEN 1 AND 29 "+
    "ORDER BY ranking DESC;"
)
DUO_PROVERBS = (
    "SELECT id FROM article "+
    "WHERE type = 3 "+
        "AND humour = \"black-bile\" "+
        "AND aux_type = \"n\" "+
        "AND ranking BETWEEN 1 AND 29 "+
    "ORDER BY ranking DESC;"
)
INT_SONGS = (
    "SELECT id FROM article "+
    "WHERE type = 1 "+
        "AND humour = \"intercalaris\" "+
        "AND aux_type = \"n\" "+
        "AND ranking = 200 "+
    "ORDER BY ranking DESC;"
)
INT_SONNETS = (
    "SELECT id FROM article "+
    "WHERE type = 2 "+
        "AND humour = \"intercalaris\" "+
        "AND aux_type = \"n\" "+
        "AND ranking = 200 "+
    "ORDER BY ranking DESC;"
)
INT_PROVERBS = (
    "SELECT id FROM article "+
    "WHERE type = 3 "+
        "AND humour = \"intercalaris\" "+
        "AND aux_type = \"n\" "+
        "AND ranking = 200 "+
    "ORDER BY ranking DESC;"
)

DEFAULT_SELECTS = {
    "Primilis": {
        "songs": MonthlySelect("yellow-bile", 1, 0, 30).query,
        "sonnets": MonthlySelect("yellow-bile", 2, 0, 30).query,
        "proverbs": MonthlySelect("yellow-bile", 3, 0, 30).query
    },
    "Sectilis": {
        "songs": MonthlySelect("yellow-bile", 1, 1, 29).query,
        "sonnets": MonthlySelect("yellow-bile", 2, 1, 29).query,
        "proverbs": MonthlySelect("yellow-bile", 3, 1, 29).query
    },
    "Tertilis": {
        "songs": MonthlySelect("yellow-bile", 1, 2, 30).query,
        "sonnets": MonthlySelect("yellow-bile", 2, 2, 30).query,
        "proverbs": MonthlySelect("yellow-bile", 3, 2, 30).query
    },
    "Quartilis": {
        "songs": QUA_SONGS,
        "sonnets": MonthlySelect("blood", 2, 2, 29).query,
        "proverbs": MonthlySelect("blood", 3, 2, 29).query
    },
    "Quintilis": {
        "songs": QUI_SONGS,
        "sonnets": QUI_SONNETS,
        "proverbs": QUI_PROVERBS
    },
    "Sextilis": {
        "songs": SEX_SONGS,
        "sonnets": MonthlySelect("blood", 2, 1, 29).query,
        "proverbs": MonthlySelect("blood", 3, 1, 29).query
    },
    "September": {
        "songs": MonthlySelect("phlegm", 1, 0, 30).query,
        "sonnets": MonthlySelect("phlegm", 2, 0, 30).query,
        "proverbs": MonthlySelect("phlegm", 3, 0, 30).query
    },
    "October": {
        "songs": OCT_SONGS,
        "sonnets": OCT_SONNETS,
        "proverbs": OCT_PROVERBS
    },
    "November": {
        "songs": MonthlySelect("phlegm", 1, 2, 30).query,
        "sonnets": MonthlySelect("phlegm", 2, 2, 30).query,
        "proverbs": MonthlySelect("phlegm", 3, 2, 30).query
    },
    "December": {
        "songs": MonthlySelect("black-bile", 1, 2, 29).query,
        "sonnets": MonthlySelect("black-bile", 2, 2, 29).query,
        "proverbs": MonthlySelect("black-bile", 3, 2, 29).query
    },
    "Unodecember": {
        "songs": MonthlySelect("black-bile", 1, 1, 30).query,
        "sonnets": MonthlySelect("black-bile", 2, 1, 30).query,
        "proverbs": MonthlySelect("black-bile", 3, 1, 30).query
    },
    "Duodecember": {
        "songs": DUO_SONGS,
        "sonnets": DUO_SONNETS,
        "proverbs": DUO_PROVERBS
    },
    "Intercalaris": {
        "songs": INT_SONGS,
        "sonnets": INT_SONNETS,
        "proverbs": INT_PROVERBS
    }
}
