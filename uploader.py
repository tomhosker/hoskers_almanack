### This code holds a class which uploads articles from individual files to
### the database.

# Imports.
import sqlite3

# Local imports.
import constants

# Helper functions.
def parse_arg(line, tag):
  if (tag+"{") not in line:
    raise Exception("\""+tag+"{\" not in "+"\""+line+"\".")
  start = line.index(tag+"{")+len(tag)+1
  i = start
  while (line[i] != "}") and (i < len(line)):
    i = i+1
  if line[i] != "}":
    raise Exception("No } paired with { in: "+line+".")
  finish = i
  return line[start:finish]
def parse_categories(line):
  catstring = parse_arg(line, "####CATEGORIES")
  categories = catstring.split(", ")
  if len(categories) != 3:
    raise Exception("Badly formed categories: \""+catstring+"\".")
  result = dict()
  result["type"] = int(categories[0])
  result["aux_type"] = categories[1]
  result["humour"] = categories[2]
  return result
def trim_whitespace(lines):
  trimmed = []
  for line in lines:
    while line.endswith(" ") or line.endswith("\t"):
      line = line[0:len(line)-1]
    trimmed.append(line)
  return trimmed

# The class in question.
class Uploader:
  def __init__(self, path_to_file):
    self.author = None
    self.non_author = None
    self.categories = None
    self.source = None
    self.title = None
    self.non_title = None
    self.remarks = None
    self.tune = None
    self.redacted = False
    self.christ_flag = False
    self.comments = dict()
    self.hpml = ""
    f = open(path_to_file, "r")
    self.raw = f.read()
    f.close()
    self.update_meta()
    self.update_comments()
    self.purge_meta()

  # Parses the "meta" lines in the file the contents of which we're
  # uploading.
  def update_meta(self):
    lines = self.raw.split("\n")
    for line in lines:
      if "####AUTHOR" in line:
        self.author = parse_arg(line, "####AUTHOR")
      elif "####NONAUTHOR" in line:
        self.non_author = parse_arg(line, "####NONAUTHOR")
      elif "####CATEGORIES" in line:
        self.categories = parse_categories(line)
      elif "####SOURCE" in line:
        self.source = parse_arg(line, "####SOURCE")
      elif "####TITLE" in line:
        self.title = parse_arg(line, "####TITLE")
      elif "####NONTITLE" in line:
        self.non_title = parse_arg(line, "####NONTITLE")
      elif "####REMARKS" in line:
        self.remarks = parse_arg(line, "####REMARKS")
      elif "####TUNE" in line:
        self.tune = parse_arg(line, "####TUNE")
      elif "####REDACTED" in line:
        self.redacted = True
      elif "####CHRISTFLAG" in line:
        self.christ_flag = True

  # Parses any comments on lines.
  def update_comments(self):
    lines = self.raw.split("\n")
    lines = trim_whitespace(lines)
    line_no = 0
    for line in lines:
      if "####COMMENT" in line:
        comment = parse_arg(line, "####COMMENT")
        self.comments[line_no] = comment
      if ("####" not in line) and ("###" not in line) and (line != ""):
        line_no = line_no+1

  # Remove any meta lines.
  def purge_meta(self):
    lines = self.raw.split("\n")
    clean = []
    for line in lines:
      if "####" not in line:
        clean.append(line)
    while clean[0] == "":
      clean.pop(0)
    while clean[len(clean)-1] == "":
      clean.pop(len(clean)-1)
    for cline in clean:
      self.hpml = self.hpml+cline
      if (self.hpml != "") and (clean.index(cline) != len(clean)-1):
        self.hpml = self.hpml+"\n"

  # Calculate the appropriate ID for our new article.
  def fetch_article_id(self):
    conn = sqlite3.connect(constants.db)
    c = conn.cursor()
    select = "SELECT id FROM article ORDER BY id DESC;"
    c.execute(select)
    row = c.fetchone()
    if len(row) == 0:
      return 1
    else:
      last = row[0]
    return last+1

  # Upload line-comments to the database.
  def upload_comments(self, article_id):
    result = True
    insert = ("INSERT INTO comment_on_line (article_id, line_no, comment) "+
              "VALUES (?, ?, ?);")
    conn = sqlite3.connect(constants.db)
    c = conn.cursor()
    for line_no in self.comments.keys():
      params = (article_id, line_no, self.comments[line_no])
      try:
        c.execute(insert, params)
      except:
        print("Error uploading comment: \""+self.comments[line_no]+"\".")
        result = False
        break
    if result:
      conn.commit()
    conn.close()
    return result

  # Upload an article to the database.
  def upload(self):
    result = True
    article_id = self.fetch_article_id()
    if self.upload_comments(article_id) == False:
      return False
    insert = ("INSERT INTO article "+
                "(id, content, author, non_author, type, aux_type, "+
                 "humour, source, title, non_title, remarks, redacted, "+
                 "tune, christFlag) "+
              "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);")
    c_type = self.categories["type"]
    c_aux_type = self.categories["aux_type"]
    c_humour = self.categories["humour"]
    params = (article_id, self.hpml, self.author, self.non_author, c_type,
              c_aux_type, c_humour, self.source, self.title, self.non_title,
              self.remarks, self.redacted, self.tune, self.christ_flag)
    conn = sqlite3.connect(constants.db)
    c = conn.cursor()
    try:
      c.execute(insert, params)
    except:
      print("Error uploading content:\n"+self.hpml)
      result = False
    finally:
      if result:
        conn.commit()
      conn.close()
      return result

# Run unit tests.
def test():
  u = Uploader("uploads/TEST1.hpml")
  assert(u.author == "eliot")
  assert(u.non_author == None)
  assert(u.categories == { "type": 1, "aux_type": "n", "humour": "bile" })
  assert(u.source == "norton")
  assert(u.title == "Catch this Daddio")
  assert(u.remarks == "Smegma!")
  assert(u.tune == None)
  assert(u.redacted == True)
  assert(u.christ_flag == False)
  assert(u.comments == { 1: "Smegma smegmata." })
  assert(u.upload() == True)
  assert(u.upload() == False)
  print("Tests passed!")

# Run and wrap up.
def run():
  test()
#run()
