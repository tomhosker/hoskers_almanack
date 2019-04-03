### This code makes the necessary replacements in the numbered
### article files.

import sqlite3, os

# Set up initial variables.
conn = sqlite3.connect("almanack.db")
c = conn.cursor()

# Constants.
articles = "articles/"
replaced = "articles/r/"
short_title = 15
full_title = 16
dob = 17
dod = 18
main = "main.tex"
redacted1 = "$\\xi$"
redacted2 = "$\\zeta$"
last = 777
problem_list = []

#################
### FUNCTIONS ###
#################

# Fetches the poet/author's short title from the DB.
def get_shorttitle(no):
  c.execute("SELECT * FROM article "+
                     "JOIN author ON author.code = article.author "+
                     "WHERE id = "+str(no)+";")
  row = c.fetchall()
  if(len(row) == 0):
    result = ""
  else:
    result = row[0][short_title]
  return(result)

# Fetches the poet/author's name from the DB.
def get_poetauthor(no):
  c.execute("SELECT * FROM article "+
                     "JOIN author ON author.code = article.author "+
                     "WHERE id = "+str(no)+";")
  row = c.fetchall()
  print(row)

  if(len(row) == 0):
    result = ""
  else:
    print(row[0][full_title])
    result = (row[0][full_title]+" "+
              "("+str(row[0][dob])+" -- "+str(row[0][dod])+")")
  return(result)

# Replaces all the instances of "old" in "fname" with "new", and puts
# the results in a new folder.
def make_replacements(no):
  fname = str(no)+".tex"
  if(os.path.exists(articles+fname)):
    shorttitle = get_shorttitle(no)
    poetauthor = get_poetauthor(no)
    f = open(articles+fname, "r")
    fstring = f.read()
    fstring = fstring.decode("utf-8")
    f.close()
    if(poetauthor != ""):
      fstring = fstring.replace(poetauthor, "POETAUTHOR")
      fstring = fstring.replace(shorttitle, "SHORTTITLE")
    fstring = fstring.replace(redacted1, "REDACTED")
    fstring = fstring.replace(redacted2, "REDACTED")
    if(poetauthor != ""):
      if not(poetauthor in fstring):
        problem_list.append(no)
    g = open(replaced+fname, "w")
    fstring = fstring.encode("utf-8")
    g.write(fstring)
    g.close()

# Makes the necessary replacements in ALL article files.
def make_all_replacements():
  for i in range(1, last+1):
    make_replacements(i)

###############
### WRAP UP ###
###############

# Runs the above.
def run():
  make_all_replacements()
  # make_replacements(1)
  print(problem_list)
run()

# Close the database.
conn.close()
