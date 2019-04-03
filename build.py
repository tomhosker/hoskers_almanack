### This code builds the Almanack's contents.

import sqlite3

# Set up initial variables.
conn = sqlite3.connect("almanack.db")
c = conn.cursor()

# Builds the header of the month's .tex file.
def start_build(name):
  header = ("\\documentclass[0main]{subfiles}\n"+
            "\\begin{document}\n\n"+
            "\\chapter{"+name+"}\n\n"+
            "\\subfile{0"+name.lower()+"_intro.tex}\n\n")
  return(header)

# Finishes building the month's .tex file.
def finish_build(month, name, songs, sonnets, proverbs):
  lengths = [len(songs), len(sonnets), len(proverbs)]
  n = min(lengths)
  for i in range(n):
    month = month+"\\bigskip\n\\bigskip\n\\section{}\n\n"
    month = month+"\\subsection{}\n\n"
    month = month+"\\subfile{"+str(songs[i][0])+"}\n\n"
    month = month+"\\subsection{}\n\n"
    month = month+"\\subfile{"+str(sonnets[i][0])+"}\n\n"
    month = month+"\\bigskip\n\\subsection{}\n\n"
    month = month+"\\subfile{"+str(proverbs[i][0])+"}\n\n"
  month = month+"\\end{document}"
  out = open("0"+name.lower()+".tex","w")
  out.write(month)

# Ronseal.
def build_primilis():
  name = "Primilis"
  month = start_build(name)
  c.execute("SELECT * FROM article "+
                     "WHERE type = 1 "+
                     "AND humour = \"bile\" "+
                     "AND aux_type = \"n\" "+
                     "AND ranking BETWEEN 1 AND 30 "+
                     "ORDER BY ranking;")
  songs = c.fetchall()
  c.execute("SELECT * FROM article "+
                     "WHERE type = 2 "+
                     "AND humour = \"bile\" "+
                     "AND aux_type = \"n\" "+
                     "AND ranking BETWEEN 1 AND 30 "+
                     "ORDER BY ranking;")
  sonnets = c.fetchall()
  c.execute("SELECT * FROM article "+
                     "WHERE type = 3 "+
                     "AND humour = \"bile\" "+
                     "AND aux_type = \"n\" "+
                     "AND ranking BETWEEN 1 AND 30 "+
                     "ORDER BY ranking;")
  proverbs = c.fetchall()
  finish_build(month, name, songs, sonnets, proverbs)

# Ronseal.
def build_sectilis():
  name = "Sectilis"
  month = start_build(name)
  c.execute("SELECT * FROM article "+
                     "WHERE type = 1 "+
                     "AND humour = \"bile\" "+
                     "AND aux_type = \"n\" "+
                     "AND ranking BETWEEN 31 AND 59 "+
                     "ORDER BY ranking;")
  songs = c.fetchall()
  c.execute("SELECT * FROM article "+
                     "WHERE type = 2 "+
                     "AND humour = \"bile\" "+
                     "AND aux_type = \"n\" "+
                     "AND ranking BETWEEN 31 AND 59 "+
                     "ORDER BY ranking;")
  sonnets = c.fetchall()
  c.execute("SELECT * FROM article "+
                     "WHERE type = 3 "+
                     "AND humour = \"bile\" "+
                     "AND aux_type = \"n\" "+
                     "AND ranking BETWEEN 31 AND 59 "+
                     "ORDER BY ranking;")
  proverbs = c.fetchall()
  finish_build(month, name, songs, sonnets, proverbs)

# Ronseal.
def build_tertilis():
  name = "Tertilis"
  month = start_build(name)
  c.execute("SELECT * FROM article "+
                     "WHERE type = 1 "+
                     "AND humour = \"bile\" "+
                     "AND aux_type = \"n\" "+
                     "AND ranking BETWEEN 60 AND 89 "+
                     "ORDER BY ranking;")
  songs = c.fetchall()
  c.execute("SELECT * FROM article "+
                     "WHERE type = 2 "+
                     "AND humour = \"bile\" "+
                     "AND aux_type = \"n\" "+
                     "AND ranking BETWEEN 60 AND 89 "+
                     "ORDER BY ranking;")
  sonnets = c.fetchall()
  c.execute("SELECT * FROM article "+
                     "WHERE type = 3 "+
                     "AND humour = \"bile\" "+
                     "AND aux_type = \"n\" "+
                     "AND ranking BETWEEN 60 AND 89 "+
                     "ORDER BY ranking;")
  proverbs = c.fetchall()
  finish_build(month, name, songs, sonnets, proverbs)

# Ronseal.
def build_quartilis():
  name = "Quartilis"
  month = start_build(name)
  c.execute("SELECT * FROM article "+
                     "WHERE type = 1 "+
                     "AND humour = \"blood\" "+
                     "AND aux_type = \"english folk\" "+
                     "AND ranking BETWEEN 1 AND 29 "+
                     "ORDER BY ranking DESC;")
  songs = c.fetchall()
  c.execute("SELECT * FROM article "+
                     "WHERE type = 2 "+
                     "AND humour = \"blood\" "+
                     "AND aux_type = \"n\" "+
                     "AND ranking BETWEEN 30 AND 58 "+
                     "ORDER BY ranking DESC;")
  sonnets = c.fetchall()
  c.execute("SELECT * FROM article "+
                     "WHERE type = 3 "+
                     "AND humour = \"blood\" "+
                     "AND aux_type = \"n\" "+
                     "AND ranking BETWEEN 60 AND 88 "+
                     "ORDER BY ranking DESC;")
  proverbs = c.fetchall()
  finish_build(month, name, songs, sonnets, proverbs)

# Ronseal.
def build_quintilis():
  name = "Quintilis"
  month = start_build(name)
  c.execute("SELECT * FROM article "+
                     "WHERE type = 1 "+
                     "AND humour = \"blood\" "+
                     "AND aux_type = \"scots-irish folk\" "+
                     "AND ranking BETWEEN 1 AND 30 "+
                     "ORDER BY ranking DESC;")
  songs = c.fetchall()
  c.execute("SELECT * FROM article "+
                     "WHERE type = 2 "+
                     "AND humour = \"blood\" "+
                     "AND aux_type = \"shanty\" "+
                     "AND ranking BETWEEN 1 AND 30 "+
                     "ORDER BY ranking DESC;")
  sonnets = c.fetchall()
  c.execute("SELECT * FROM article "+
                     "WHERE type = 3 "+
                     "AND humour = \"blood\" "+
                     "AND aux_type = \"n\" "+
                     "AND ranking BETWEEN 1 AND 30 "+
                     "ORDER BY ranking DESC;")
  proverbs = c.fetchall()
  finish_build(month, name, songs, sonnets, proverbs)

# Ronseal.
def build_sextilis():
  name = "Sextilis"
  month = start_build(name)
  c.execute("SELECT * FROM article "+
                     "WHERE type = 1 "+
                     "AND humour = \"blood\" "+
                     "AND aux_type = \"american folk\" "+
                     "AND ranking BETWEEN 1 AND 19 "+
                     "ORDER BY ranking DESC;")
  songs1 = c.fetchall()
  c.execute("SELECT * FROM article "+
                     "WHERE type = 1 "+
                     "AND humour = \"blood\" "+
                     "AND aux_type = \"hymn\" "+
                     "AND ranking BETWEEN 1 AND 10 "+
                     "ORDER BY ranking DESC;")
  songs2 = c.fetchall()
  songs = songs1+songs2
  c.execute("SELECT * FROM article "+
                     "WHERE type = 2 "+
                     "AND humour = \"blood\" "+
                     "AND aux_type = \"n\" "+
                     "AND ranking BETWEEN 1 AND 29 "+
                     "ORDER BY ranking DESC;")
  sonnets = c.fetchall()
  c.execute("SELECT * FROM article "+
                     "WHERE type = 3 "+
                     "AND humour = \"blood\" "+
                     "AND aux_type = \"n\" "+
                     "AND ranking BETWEEN 31 AND 59 "+
                     "ORDER BY ranking DESC;")
  proverbs = c.fetchall()
  finish_build(month, name, songs, sonnets, proverbs)

# Ronseal.
def build_september():
  name = "September"
  month = start_build(name)
  c.execute("SELECT * FROM article "+
                     "WHERE type = 1 "+
                     "AND humour = \"phlegm\" "+
                     "AND aux_type = \"n\" "+
                     "AND ranking BETWEEN 1 AND 30 "+
                     "ORDER BY ranking;")
  songs = c.fetchall()
  c.execute("SELECT * FROM article "+
                     "WHERE type = 2 "+
                     "AND humour = \"phlegm\" "+
                     "AND aux_type = \"n\" "+
                     "AND ranking BETWEEN 1 AND 30 "+
                     "ORDER BY ranking;")
  sonnets = c.fetchall()
  c.execute("SELECT * FROM article "+
                     "WHERE type = 3 "+
                     "AND humour = \"phlegm\" "+
                     "AND aux_type = \"n\" "+
                     "AND ranking BETWEEN 1 AND 30 "+
                     "ORDER BY ranking;")
  proverbs = c.fetchall()
  finish_build(month, name, songs, sonnets, proverbs)

# Ronseal.
def build_october():
  name = "October"
  month = start_build(name)
  c.execute("SELECT * FROM article "+
                     "WHERE type = 1 "+
                     "AND humour = \"phlegm\" "+
                     "AND aux_type = \"october\" "+
                     "AND ranking BETWEEN 1 AND 29 "+
                     "ORDER BY ranking;")
  songs = c.fetchall()
  c.execute("SELECT * FROM article "+
                     "WHERE type = 2 "+
                     "AND humour = \"phlegm\" "+
                     "AND aux_type = \"october\" "+
                     "AND ranking BETWEEN 1 AND 29 "+
                     "ORDER BY ranking;")
  sonnets = c.fetchall()
  c.execute("SELECT * FROM article "+
                     "WHERE type = 3 "+
                     "AND humour = \"phlegm\" "+
                     "AND aux_type = \"october\" "+
                     "AND ranking BETWEEN 1 AND 29 "+
                     "ORDER BY ranking;")
  proverbs = c.fetchall()
  finish_build(month, name, songs, sonnets, proverbs)

# Ronseal.
def build_november():
  name = "November"
  month = start_build(name)
  c.execute("SELECT * FROM article "+
                     "WHERE type = 1 "+
                     "AND humour = \"phlegm\" "+
                     "AND aux_type = \"n\" "+
                     "AND ranking BETWEEN 31 AND 60 "+
                     "ORDER BY ranking;")
  songs = c.fetchall()
  c.execute("SELECT * FROM article "+
                     "WHERE type = 2 "+
                     "AND humour = \"phlegm\" "+
                     "AND aux_type = \"n\" "+
                     "AND ranking BETWEEN 31 AND 60 "+
                     "ORDER BY ranking;")
  sonnets = c.fetchall()
  c.execute("SELECT * FROM article "+
                     "WHERE type = 3 "+
                     "AND humour = \"phlegm\" "+
                     "AND aux_type = \"n\" "+
                     "AND ranking BETWEEN 31 AND 60 "+
                     "ORDER BY ranking;")
  proverbs = c.fetchall()
  finish_build(month, name, songs, sonnets, proverbs)

# Ronseal.
def build_december():
  name = "December"
  month = start_build(name)
  c.execute("SELECT * FROM article "+
                     "WHERE type = 1 "+
                     "AND humour = \"black bile\" "+
                     "AND aux_type = \"n\" "+
                     "AND ranking BETWEEN 60 AND 88 "+
                     "ORDER BY ranking DESC;")
  songs = c.fetchall()
  c.execute("SELECT * FROM article "+
                     "WHERE type = 2 "+
                     "AND humour = \"black bile\" "+
                     "AND aux_type = \"n\" "+
                     "AND ranking BETWEEN 60 AND 88 "+
                     "ORDER BY ranking DESC;")
  sonnets = c.fetchall()
  c.execute("SELECT * FROM article "+
                     "WHERE type = 3 "+
                     "AND humour = \"black bile\" "+
                     "AND aux_type = \"n\" "+
                     "AND ranking BETWEEN 60 AND 88 "+
                     "ORDER BY ranking DESC;")
  proverbs = c.fetchall()
  finish_build(month, name, songs, sonnets, proverbs)

# Ronseal.
def build_unodecember():
  name = "Unodecember"
  month = start_build(name)
  c.execute("SELECT * FROM article "+
                     "WHERE type = 1 "+
                     "AND humour = \"black bile\" "+
                     "AND aux_type = \"n\" "+
                     "AND ranking BETWEEN 30 AND 59 "+
                     "ORDER BY ranking DESC;")
  songs = c.fetchall()
  c.execute("SELECT * FROM article "+
                     "WHERE type = 2 "+
                     "AND humour = \"black bile\" "+
                     "AND aux_type = \"n\" "+
                     "AND ranking BETWEEN 30 AND 59 "+
                     "ORDER BY ranking DESC;")
  sonnets = c.fetchall()
  c.execute("SELECT * FROM article "+
                     "WHERE type = 3 "+
                     "AND humour = \"black bile\" "+
                     "AND aux_type = \"n\" "+
                     "AND ranking BETWEEN 30 AND 59 "+
                     "ORDER BY ranking DESC;")
  proverbs = c.fetchall()
  finish_build(month, name, songs, sonnets, proverbs)

# Ronseal.
def build_duodecember():
  name = "Duodecember"
  month = start_build(name)
  c.execute("SELECT * FROM article "+
                     "WHERE type = 1 "+
                     "AND humour = \"black bile\" "+
                     "AND aux_type = \"n\" "+
                     "AND ranking BETWEEN 1 AND 29 "+
                     "ORDER BY ranking DESC;")
  songs = c.fetchall()
  c.execute("SELECT * FROM article "+
                     "WHERE type = 2 "+
                     "AND humour = \"black bile\" "+
                     "AND aux_type = \"n\" "+
                     "AND ranking BETWEEN 1 AND 29 "+
                     "ORDER BY ranking DESC;")
  sonnets = c.fetchall()
  c.execute("SELECT * FROM article "+
                     "WHERE type = 3 "+
                     "AND humour = \"black bile\" "+
                     "AND aux_type = \"n\" "+
                     "AND ranking BETWEEN 1 AND 29 "+
                     "ORDER BY ranking DESC;")
  proverbs = c.fetchall()
  finish_build(month, name, songs, sonnets, proverbs)

# Ronseal.
def build_intercalaris():
  name = "Intercalaris"
  month = start_build(name)
  c.execute("SELECT * FROM article "+
                     "WHERE type = 1 "+
                     "AND humour = \"intercalaris\" "+
                     "AND aux_type = \"n\" "+
                     "AND ranking BETWEEN 1 AND 29 "+
                     "ORDER BY ranking DESC;")
  songs = c.fetchall()
  c.execute("SELECT * FROM article "+
                     "WHERE type = 2 "+
                     "AND humour = \"intercalaris\" "+
                     "AND aux_type = \"n\" "+
                     "AND ranking BETWEEN 1 AND 29 "+
                     "ORDER BY ranking DESC;")
  sonnets = c.fetchall()
  c.execute("SELECT * FROM article "+
                     "WHERE type = 3 "+
                     "AND humour = \"intercalaris\" "+
                     "AND aux_type = \"n\" "+
                     "AND ranking BETWEEN 1 AND 29 "+
                     "ORDER BY ranking DESC;")
  proverbs = c.fetchall()
  finish_build(month, name, songs, sonnets, proverbs)

def build_months():
  build_primilis()
  build_sectilis()
  build_tertilis()
  build_quartilis()
  build_quintilis()
  build_sextilis()
  build_september()
  build_october()
  build_november()
  build_december()
  build_unodecember()
  build_duodecember()
  build_intercalaris()

# Build the months.
build_months()

# Close the database.
conn.close()
