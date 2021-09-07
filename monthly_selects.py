PRI_SONGS = (
        "SELECT id FROM article "+
        "WHERE type = 1 "+
            "AND humour = \"yellow-bile\" "+
            "AND aux_type = \"n\" "+
            "AND ranking BETWEEN 1 AND 30 "+
        "ORDER BY ranking;")
PRI_SONNETS = (
        "SELECT id FROM article "+
        "WHERE type = 2 "+
            "AND humour = \"yellow-bile\" "+
            "AND aux_type = \"n\" "+
            "AND ranking BETWEEN 1 AND 30 "+
        "ORDER BY ranking;")
PRI_PROVERBS = (
        "SELECT id FROM article "+
        "WHERE type = 3 "+
            "AND humour = \"yellow-bile\" "+
            "AND aux_type = \"n\" "+
            "AND ranking BETWEEN 1 AND 30 "+
        "ORDER BY ranking;")
SEC_SONGS = (
        "SELECT id FROM article "+
        "WHERE type = 1 "+
            "AND humour = \"yellow-bile\" "+
            "AND aux_type = \"n\" "+
            "AND ranking BETWEEN 31 AND 59 "+
        "ORDER BY ranking ;")
SEC_SONNETS = (
        "SELECT id FROM article "+
        "WHERE type = 2 "+
            "AND humour = \"yellow-bile\" "+
            "AND aux_type = \"n\" "+
            "AND ranking BETWEEN 31 AND 59 "+
        "ORDER BY ranking;")
SEC_PROVERBS = (
        "SELECT id FROM article "+
        "WHERE type = 3 "+
            "AND humour = \"yellow-bile\" "+
            "AND aux_type = \"n\" "+
            "AND ranking BETWEEN 31 AND 59 "+
        "ORDER BY ranking;")
TER_SONGS = (
        "SELECT id FROM article "+
        "WHERE type = 1 "+
            "AND humour = \"yellow-bile\" "+
            "AND aux_type = \"n\" "+
            "AND ranking BETWEEN 60 AND 89 "+
        "ORDER BY ranking;")
TER_SONNETS = (
        "SELECT id FROM article "+
        "WHERE type = 2 "+
            "AND humour = \"yellow-bile\" "+
            "AND aux_type = \"n\" "+
            "AND ranking BETWEEN 60 AND 89 "+
        "ORDER BY ranking;")
TER_PROVERBS = (
        "SELECT id FROM article "+
        "WHERE type = 3 "+
            "AND humour = \"yellow-bile\" "+
            "AND aux_type = \"n\" "+
            "AND ranking BETWEEN 60 AND 89 "+
        "ORDER BY ranking;")
QUA_SONGS = (
        "SELECT id FROM article "+
        "WHERE type = 1 "+
            "AND humour = \"blood\" "+
            "AND aux_type = \"english folk\" "+
            "AND ranking BETWEEN 1 AND 29 "+
        "ORDER BY ranking DESC;")
QUA_SONNETS = (
        "SELECT id FROM article "+
        "WHERE type = 2 "+
            "AND humour = \"blood\" "+
            "AND aux_type = \"n\" "+
            "AND ranking BETWEEN 30 AND 58 "+
        "ORDER BY ranking DESC;")
QUA_PROVERBS = (
        "SELECT id FROM article "+
        "WHERE type = 3 "+
            "AND humour = \"blood\" "+
            "AND aux_type = \"n\" "+
            "AND ranking BETWEEN 60 AND 88 "+
        "ORDER BY ranking DESC;")
QUI_SONGS = (
        "SELECT id FROM article "+
        "WHERE type = 1 "+
            "AND humour = \"blood\" "+
            "AND aux_type = \"scots-irish folk\" "+
            "AND ranking BETWEEN 1 AND 30 "+
        "ORDER BY ranking DESC;")
QUI_SONNETS = (
        "SELECT id FROM article "+
        "WHERE type = 2 "+
            "AND humour = \"blood\" "+
            "AND aux_type = \"shanty\" "+
            "AND ranking BETWEEN 1 AND 30 "+
        "ORDER BY ranking DESC;")
QUI_PROVERBS = (
        "SELECT id FROM article "+
        "WHERE type = 3 "+
            "AND humour = \"blood\" "+
            "AND aux_type = \"n\" "+
            "AND ranking BETWEEN 1 AND 30 "+
        "ORDER BY ranking DESC;")
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
        "ORDER BY aux_type, ranking DESC;")
SEX_SONNETS = (
        "SELECT id FROM article "+
        "WHERE type = 2 "+
            "AND humour = \"blood\" "+
            "AND aux_type = \"n\" "+
            "AND ranking BETWEEN 1 AND 29 "+
        "ORDER BY ranking DESC;")
SEX_PROVERBS = (
        "SELECT id FROM article "+
        "WHERE type = 3 "+
            "AND humour = \"blood\" "+
            "AND aux_type = \"n\" "+
            "AND ranking BETWEEN 31 AND 59 "+
        "ORDER BY ranking DESC;")
SEP_SONGS = (
        "SELECT id FROM article "+
        "WHERE type = 1 "+
            "AND humour = \"phlegm\" "+
            "AND aux_type = \"n\" "+
            "AND ranking BETWEEN 1 AND 30 "+
        "ORDER BY ranking;")
SEP_SONNETS = (
        "SELECT id FROM article "+
        "WHERE type = 2 "+
            "AND humour = \"phlegm\" "+
            "AND aux_type = \"n\" "+
            "AND ranking BETWEEN 1 AND 30 "+
        "ORDER BY ranking;")
SEP_PROVERBS = (
        "SELECT id FROM article "+
        "WHERE type = 3 "+
            "AND humour = \"phlegm\" "+
            "AND aux_type = \"n\" "+
            "AND ranking BETWEEN 1 AND 30 "+
        "ORDER BY ranking;")
OCT_SONGS = (
        "SELECT id FROM article "+
        "WHERE type = 1 "+
            "AND humour = \"phlegm\" "+
            "AND aux_type = \"october\" "+
            "AND ranking BETWEEN 1 AND 29 "+
        "ORDER BY ranking;")
OCT_SONNETS = (
        "SELECT id FROM article "+
        "WHERE type = 2 "+
            "AND humour = \"phlegm\" "+
            "AND aux_type = \"october\" "+
            "AND ranking BETWEEN 1 AND 29 "+
        "ORDER BY ranking;")
OCT_PROVERBS = (
        "SELECT id FROM article "+
        "WHERE type = 3 "+
            "AND humour = \"phlegm\" "+
            "AND aux_type = \"october\" "+
            "AND ranking BETWEEN 1 AND 29 "+
        "ORDER BY ranking;")
NOV_SONGS = (
        "SELECT id FROM article "+
        "WHERE type = 1 "+
            "AND humour = \"phlegm\" "+
            "AND aux_type = \"n\" "+
            "AND ranking BETWEEN 31 AND 60 "+
        "ORDER BY ranking;")
NOV_SONNETS = (
        "SELECT id FROM article "+
        "WHERE type = 2 "+
            "AND humour = \"phlegm\" "+
            "AND aux_type = \"n\" "+
            "AND ranking BETWEEN 31 AND 60 "+
        "ORDER BY ranking;")
NOV_PROVERBS = (
        "SELECT id FROM article "+
        "WHERE type = 3 "+
            "AND humour = \"phlegm\" "+
            "AND aux_type = \"n\" "+
            "AND ranking BETWEEN 31 AND 60 "+
        "ORDER BY ranking;")
DEC_SONGS = (
        "SELECT id FROM article "+
        "WHERE type = 1 "+
            "AND humour = \"black-bile\" "+
            "AND aux_type = \"n\" "+
            "AND ranking BETWEEN 60 AND 88 "+
        "ORDER BY ranking DESC;")
DEC_SONNETS = (
        "SELECT id FROM article "+
        "WHERE type = 2 "+
            "AND humour = \"black-bile\" "+
            "AND aux_type = \"n\" "+
            "AND ranking BETWEEN 60 AND 88 "+
        "ORDER BY ranking DESC;")
DEC_PROVERBS = (
        "SELECT id FROM article "+
        "WHERE type = 3 "+
            "AND humour = \"black-bile\" "+
            "AND aux_type = \"n\" "+
            "AND ranking BETWEEN 60 AND 88 "+
        "ORDER BY ranking DESC;")
UNO_SONGS = (
        "SELECT id FROM article "+
        "WHERE type = 1 "+
            "AND humour = \"black-bile\" "+
            "AND aux_type = \"n\" "+
            "AND ranking BETWEEN 30 AND 59 "+
        "ORDER BY ranking DESC;")
UNO_SONNETS = (
        "SELECT id FROM article "+
        "WHERE type = 2 "+
            "AND humour = \"black-bile\" "+
            "AND aux_type = \"n\" "+
            "AND ranking BETWEEN 30 AND 59 "+
        "ORDER BY ranking DESC;")
UNO_PROVERBS = (
        "SELECT id FROM article "+
        "WHERE type = 3 "+
            "AND humour = \"black-bile\" "+
            "AND aux_type = \"n\" "+
            "AND ranking BETWEEN 30 AND 59 "+
        "ORDER BY ranking DESC;")
DUO_SONGS = (
        "SELECT id FROM article "+
        "WHERE type = 1 "+
            "AND humour = \"black-bile\" "+
            "AND aux_type = \"n\" "+
            "AND ranking BETWEEN 1 AND 29 "+
        "ORDER BY ranking DESC;")
DUO_SONNETS = (
        "SELECT id FROM article "+
        "WHERE type = 2 "+
            "AND humour = \"black-bile\" "+
            "AND aux_type = \"n\" "+
            "AND ranking BETWEEN 1 AND 29 "+
        "ORDER BY ranking DESC;")
DUO_PROVERBS = (
        "SELECT id FROM article "+
        "WHERE type = 3 "+
            "AND humour = \"black-bile\" "+
            "AND aux_type = \"n\" "+
            "AND ranking BETWEEN 1 AND 29 "+
        "ORDER BY ranking DESC;")
INT_SONGS = (
        "SELECT id FROM article "+
        "WHERE type = 1 "+
            "AND humour = \"intercalaris\" "+
            "AND aux_type = \"n\" "+
            "AND ranking BETWEEN 1 AND 29 "+
        "ORDER BY ranking DESC;")
INT_SONNETS = (
        "SELECT id FROM article "+
        "WHERE type = 2 "+
            "AND humour = \"intercalaris\" "+
            "AND aux_type = \"n\" "+
            "AND ranking BETWEEN 1 AND 29 "+
        "ORDER BY ranking DESC;")
INT_PROVERBS = (
        "SELECT id FROM article "+
        "WHERE type = 3 "+
            "AND humour = \"intercalaris\" "+
            "AND aux_type = \"n\" "+
            "AND ranking BETWEEN 1 AND 29 "+
        "ORDER BY ranking DESC;")

DEFAULT_SELECTS = {
    "Primilis": {
        "songs": PRI_SONGS,
        "sonnets": PRI_SONNETS,
        "proverbs": PRI_PROVERBS },
    "Sectilis": {
        "songs": SEC_SONGS,
        "sonnets": SEC_SONNETS,
        "proverbs": SEC_PROVERBS },
    "Tertilis": {
        "songs": TER_SONGS,
        "sonnets": TER_SONNETS,
        "proverbs": TER_PROVERBS },
    "Quartilis": {
        "songs": QUA_SONGS,
        "sonnets": QUA_SONNETS,
        "proverbs": QUA_PROVERBS },
    "Quintilis": {
        "songs": QUI_SONGS,
        "sonnets": QUI_SONNETS,
        "proverbs": QUI_PROVERBS },
    "Sextilis": {
        "songs": SEX_SONGS,
        "sonnets": SEX_SONNETS,
        "proverbs": SEX_PROVERBS },
    "September": {
        "songs": SEP_SONGS,
        "sonnets": SEP_SONNETS,
        "proverbs": SEP_PROVERBS },
    "October": {
        "songs": OCT_SONGS,
        "sonnets": OCT_SONNETS,
        "proverbs": OCT_PROVERBS },
    "November": {
        "songs": NOV_SONGS,
        "sonnets": NOV_SONNETS,
        "proverbs": NOV_PROVERBS },
    "December": {
        "songs": DEC_SONGS,
        "sonnets": DEC_SONNETS,
        "proverbs": DEC_PROVERBS },
    "Unodecember": {
        "songs": UNO_SONGS,
        "sonnets": UNO_SONNETS,
        "proverbs": UNO_PROVERBS },
    "Duodecember": {
        "songs": DUO_SONGS,
        "sonnets": DUO_SONNETS,
        "proverbs": DUO_PROVERBS },
    "Intercalaris": {
        "songs": INT_SONGS,
        "sonnets": INT_SONNETS,
        "proverbs": INT_PROVERBS } }
