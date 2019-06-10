### This code builds a BibTeX bibliography from the database.

# Imports.
import sqlite3

# Local imports.
import almanack_utils

# Ronseal.
def fetch_sources():
  select = "SELECT * FROM source ORDER BY code;"
  sources = almanack_utils.fetch_to_dict("almanack.db", select)
  return sources

# Ronseal.
def wipe_bib():
  f = open("sources.bib", "w")
  f.write("")
  f.close()

# Builds our .bib file.
def build_bib():
  sources = fetch_sources()
  wipe_bib()
  f = open("sources.bib", "a")
  for source in sources:
    code = source["code"]
    keywords = source["keywords"]
    if source["author"] == None:
      author = ""
    else:
      author = source["author"]
    title = source["title"]
    if source["year"] == None:
      year = ""
    else:
      year = str(source["year"])
    if source["editor"] == None:
      editor = ""
    else:
      editor = source["editor"]
    if source["translator"] == None:
      translator = ""
    else:
      translator = source["translator"]
    f.write("@book{"+code+",\n")
    f.write("  keywords = \""+keywords+"\",\n")
    f.write("  author = \""+author+"\",\n")
    f.write("  title = \""+title+"\",\n")
    f.write("  year = \""+year+"\",\n")
    f.write("  editor = \""+editor+"\",\n")
    f.write("  translator = \""+translator+"\"\n")
    f.write("}\n\n")
  f.close()

# Run and wrap up.
def run():
  build_bib()
run()
