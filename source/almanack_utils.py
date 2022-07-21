"""
This is a place to store some useful functions for use across this
repository.
"""

# Standard imports.
import sqlite3

# Local imports.
if __package__:
    from . import configs
else:
    import configs

#############
# FUNCTIONS #
#############

def fetch_to_dict(select, parameters, path_to_db=configs.PATH_TO_DB):
    """ Runs a "SELECT" query, and wraps the results into a dictionary. """
    connection = sqlite3.connect(path_to_db)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute(select, parameters)
    extract = cursor.fetchall()
    connection.close()
    rows = []
    for item in extract:
        row = dict(item)
        rows.append(row)
    return rows
