### This is a place to store some useful functions for use across this
### repository.

# Imports.
import sqlite3

# Runs a "SELECT" query, and wraps the results into a dictionary.
def fetch_to_dict(database_name, select):
  conn = sqlite3.connect(database_name)
  conn.row_factory = sqlite3.Row
  c = conn.cursor()
  c.execute(select)
  extract = c.fetchall()
  conn.close()
  rows = []
  for item in extract:
    row = dict(item)
    rows.append(row)
  return rows
