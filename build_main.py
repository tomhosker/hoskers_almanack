### This code builds and compiles "main.tex".

# Imports.
import sqlite3, os

# Local imports.
from month_builder import Month_builder
from bib_builder import build_bib

# Constants.
version = " (Fourth Draft)"

# Fetch packages used from the database.
def fetch_loadout():
  conn = sqlite3.connect("almanack.db")
  c = conn.cursor()
  select = "SELECT latex FROM package_loadout WHERE name = \"main\";"
  c.execute(select)
  extract = c.fetchone()
  result = extract[0]
  conn.close()
  return result

# Build the frontmatter from the database.
def build_frontmatter():
  conn = sqlite3.connect("almanack.db")
  c = conn.cursor()
  select = "SELECT * FROM frontmatter_chapters ORDER BY no;"
  c.execute(select)
  extract = c.fetchall()
  conn.close()
  result = ""
  for i in range(len(extract)):
    result = (result+"\\chapter{"+extract[i][1]+"}"+"\n\n"+extract[i][2]+
              "\n\n")
  return result

# Build the mainmatter from the "Month_builder" class.
def build_mainmatter():
  month_builder = Month_builder()
  result = month_builder.digest()
  return result

# Build the backmatter from the database.
def build_backmatter():
  conn = sqlite3.connect("almanack.db")
  c = conn.cursor()
  select = "SELECT * FROM backmatter_chapters ORDER BY no;"
  c.execute(select)
  extract = c.fetchall()
  conn.close()
  result = ""
  for i in range(len(extract)):
    result = (result+"\\chapter{"+extract[i][1]+"}"+"\n\n"+extract[i][2]+
              "\n\n")
  return result

# This is where the magic happens.
def build_tex():
  conn = sqlite3.connect("almanack.db")
  c = conn.cursor()
  select = "SELECT * FROM tween_syntax;"
  c.execute(select)
  extract = c.fetchall()
  for i in range(len(extract)):
    if extract[i][0] == "in_preamble":
      in_preamble = extract[i][1]
    elif extract[i][0] == "pre_mainmatter":
      pre_mainmatter = extract[i][1]
    elif extract[i][0] == "pre_backmatter":
      pre_backmatter = extract[i][1]
    elif extract[i][0] == "bibliography_note":
      bibliography_note = extract[i][1]
  conn.close()
  loadout = fetch_loadout()
  frontmatter = build_frontmatter()
  mainmatter = build_mainmatter()
  backmatter = build_backmatter()
  
  main = ("\\documentclass{amsbook}\n"+
          "\\title{Hosker's Almanack"+version+"}\n\n"+
          loadout+"\n\n"+
          in_preamble+"\n\n"+
          "\\begin{document}\n\n"+
          "\\frontmatter\n\n"+
          "\\maketitle\n"+
          "\\tableofcontents\n"+
          "\\listoffigures\n\n"+
          "\\part{Introductory Material}\n\n"+
          frontmatter+"\n\n"+
          "\\mainmatter\n\n"+
          "\\part{The \\textit{Almanack} Proper}\n\n"+
          pre_mainmatter+"\n\n"+
          mainmatter+"\n\n"+
          "\\backmatter\n\n"+
          pre_backmatter+"\n\n"+
          "\\part{Other Material}\n\n"+
          backmatter+"\n\n"+
          "\\printbibliography[title={Sources}]\n"+
          "\\bigskip\n"+
          "{\\footnotesize "+bibliography_note+"}\n\n"+
          "\\end{document}")
  f = open("main.tex", "w")
  f.write(main)
  f.close()

# Runs XeLaTeX on "main.tex" and BibTex on "main.aux" in order to build our
# PDF, "main.pdf".
def build_pdf():
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
  build_bib()
  build_tex()
  build_pdf()
run()
