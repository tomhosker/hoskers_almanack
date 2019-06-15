### This code holds a class which builds "almanack.pdf".

# Imports.
import sqlite3, os

# Local imports.
import constants, almanack_utils
from month_builder import Month_builder
from bib_builder import build_bib

# The class in question.
class PDF_builder:
  def __init__(self, fullness):
    # This determines how much front- and backmatter, etc gets put in.
    self.fullness = fullness
    build_bib()
    self.loadout = self.fetch_loadout()
    self.tween_syntax = self.fetch_tween_syntax()
    if(self.fullness == "full"):
      self.frontmatter = self.build_frontmatter()
    else:
      self.frontmatter = ""
    self.mainmatter = self.build_mainmatter()
    if(self.fullness in ["full", "slender"]):
      self.backmatter = self.build_backmatter()
    else:
      self.backmatter = ""
    self.build_tex()
    self.build_pdf()

  # Fetch packages used from the database.
  def fetch_loadout(self):
    select = "SELECT latex FROM package_loadout WHERE name = \"main\";"
    rows = almanack_utils.fetch_to_dict(constants.db, select, tuple())
    result = rows[0]["latex"]
    return result

  # Fetches the bits of LaTeX syntax which go between the lumps of content.
  def fetch_tween_syntax(self):
    conn = sqlite3.connect(constants.db)
    c = conn.cursor()
    select = "SELECT * FROM tween_syntax;"
    c.execute(select)
    rows = c.fetchall()
    result = dict()
    for row in rows:
      result[row[0]] = row[1]
    return result

  # Build the frontmatter from the database.
  def build_frontmatter(self):
    select = "SELECT * FROM frontmatter_chapters ORDER BY no;"
    rows = almanack_utils.fetch_to_dict(constants.db, select, tuple())
    result = ("\\listoffigures\n\n"+
              "\\part{Introductory Material}\n\n")
    for row in rows:
      title = "\\chapter{"+row["name"]+"}"
      content = row["content"]
      result = result+title+"\n\n"+content
      if rows.index(row) != len(rows)-1:
        result = result+"\n\n"
    return result

  # Build the mainmatter from the "Month_builder" class.
  def build_mainmatter(self):
    month_builder = Month_builder(self.fullness)
    result = ("\\part{The \\textit{Almanack} Proper}\n\n"+
              self.tween_syntax["pre_mainmatter"]+"\n\n")
    result = result+month_builder.digest()
    return result

  # Build the backmatter from the database.
  def build_backmatter(self):
    select = "SELECT * FROM backmatter_chapters ORDER BY no;"
    rows = almanack_utils.fetch_to_dict(constants.db, select, tuple())
    result = (self.tween_syntax["pre_backmatter"]+"\n\n"+
              "\\part{Other Material}\n\n")
    for row in rows:
      title = "\\chapter{"+row["name"]+"}"
      content = row["content"]
      result = result+title+"\n\n"+content+"\n\n"
    result = (result+"\\printbibliography[title={Sources}]\n"+
                     "\\bigskip\n"+
                     "{\\footnotesize "+
                       self.tween_syntax["bibliography_note"]+"}\n\n")
    return result

  # This is where the magic happens.
  def build_tex(self):
    tex =  ("\\documentclass{amsbook}\n"+
            "\\title{Hosker's Almanack ("+constants.version+")}\n\n"+
            self.loadout+"\n\n"+
            self.tween_syntax["in_preamble"]+"\n\n"+
            "\\begin{document}\n\n"+
            "\\frontmatter\n\n"+
            "\\maketitle\n"+
            "\\tableofcontents\n"+
            self.frontmatter+"\n\n"+
            "\\mainmatter\n\n"+
            self.mainmatter+"\n\n"+
#            "\\backmatter\n\n"+
            self.backmatter+"\n\n"+
            "\\end{document}")
    f = open("main.tex", "w")
    f.write(tex)
    f.close()

  # Runs XeLaTeX on "main.tex" and BibTex on "main.aux" in order to build
  # our PDF, "main.pdf".
  def build_pdf(self):
    try:
      os.system("xelatex main.tex")
      os.system("bibtex main.aux")
      os.system("xelatex main.tex")
      os.system("cp main.pdf almanack.pdf")
      os.system("rm -rf main*")
    except:
      print("Run build.tex() first!")
    os.system("rm sources.bib")

# Run and wrap up.
def run():
  PDF_builder("full")
run()
