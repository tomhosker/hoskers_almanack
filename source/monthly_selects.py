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

####################
# HELPER FUNCTIONS #
####################

def get_monthly_select(*args, **kwargs):
    """ Create a MonthlySelect object. Get the query. Move on. """
    monthly_select = MonthlySelect(*args, **kwargs)
    result = monthly_select.query
    return result

######################
# SELECTS DICTIONARY #
######################

QUA_SONGS = (
    "SELECT id FROM article "+
    "WHERE type = 1 "+
        "AND humour = \"blood\" "+
        "AND aux_type = \"english folk\" "+
        "AND ((ranking BETWEEN 1 AND 29) OR (ranking = 101)) "+
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
    "SELECT id "+
    "FROM article "+
    "WHERE ("+
        "type = 1 AND "+
        "humour = \"blood\" AND "+
        "aux_type = \"imperial folk\" AND "+
        "((ranking BETWEEN 1 AND 19) OR (ranking = 101))"+
    ") OR ("+
        "type = 1 AND "+
        "humour = \"blood\" AND "+
        "aux_type = \"hymn\" AND "+
        "((ranking BETWEEN 1 AND 10) OR (ranking = 101))"+
    ") ORDER BY aux_type, ranking DESC;"
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

SELECTS = {
    "Primilis": {
        "songs": get_monthly_select("yellow-bile", 1, 0, 30),
        "sonnets": get_monthly_select("yellow-bile", 2, 0, 30),
        "proverbs": get_monthly_select("yellow-bile", 3, 0, 30)
    },
    "Sectilis": {
        "songs": get_monthly_select("yellow-bile", 1, 1, 29),
        "sonnets": get_monthly_select("yellow-bile", 2, 1, 29),
        "proverbs": get_monthly_select("yellow-bile", 3, 1, 29)
    },
    "Tertilis": {
        "songs": get_monthly_select("yellow-bile", 1, 2, 30),
        "sonnets": get_monthly_select("yellow-bile", 2, 2, 30),
        "proverbs": get_monthly_select("yellow-bile", 3, 2, 30)
    },
    "Quartilis": {
        "songs": QUA_SONGS,
        "sonnets": get_monthly_select("blood", 2, 2, 29),
        "proverbs": get_monthly_select("blood", 3, 2, 29)
    },
    "Quintilis": {
        "songs": QUI_SONGS,
        "sonnets": QUI_SONNETS,
        "proverbs": QUI_PROVERBS
    },
    "Sextilis": {
        "songs": SEX_SONGS,
        "sonnets": get_monthly_select("blood", 2, 1, 29),
        "proverbs": get_monthly_select("blood", 3, 1, 29)
    },
    "September": {
        "songs": get_monthly_select("phlegm", 1, 0, 30),
        "sonnets": get_monthly_select("phlegm", 2, 0, 30),
        "proverbs": get_monthly_select("phlegm", 3, 0, 30)
    },
    "October": {
        "songs": OCT_SONGS,
        "sonnets": OCT_SONNETS,
        "proverbs": OCT_PROVERBS
    },
    "November": {
        "songs": get_monthly_select("phlegm", 1, 2, 30),
        "sonnets": get_monthly_select("phlegm", 2, 2, 30),
        "proverbs": get_monthly_select("phlegm", 3, 2, 30)
    },
    "December": {
        "songs": get_monthly_select("black-bile", 1, 2, 29),
        "sonnets": get_monthly_select("black-bile", 2, 2, 29),
        "proverbs": get_monthly_select("black-bile", 3, 2, 29)
    },
    "Unodecember": {
        "songs": get_monthly_select("black-bile", 1, 1, 30),
        "sonnets": get_monthly_select("black-bile", 2, 1, 30),
        "proverbs": get_monthly_select("black-bile", 3, 1, 30)
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
