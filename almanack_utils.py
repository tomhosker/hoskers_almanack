"""
This is a place to store some useful functions for use across this
repository.
"""

# Standard imports.
import sqlite3

#############
# FUNCTIONS #
#############

def fetch_to_dict(database_name, select, parameters):
    """ Runs a "SELECT" query, and wraps the results into a dictionary. """
    conn = sqlite3.connect(database_name)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute(select, parameters)
    extract = c.fetchall()
    conn.close()
    rows = []
    for item in extract:
        row = dict(item)
        rows.append(row)
    return rows
