### This code holds a class which handles a given article's notes.

# Imports.
import os, sys

# Local imports.
import constants, almanack_utils

# The class in question.
class Notes_builder:
  # Class variables.
  named_non_authors = ["Anonymous"]
  redacted_marker = "$\mathfrak{R}$"

  def __init__(self, idno, fullness):
    self.idno = idno
    self.fullness = fullness
    self.extract = self.fetch_extract()
    self.source = self.extract["source"]
    self.non_title = self.extract["non_title"]
    self.remarks = self.extract["remarks"]
    self.redacted = self.extract["redacted"]
    self.author = self.extract["author"]
    self.title = self.build_title()
    self.dates = self.build_dates()
    self.non_author = self.build_non_author()
    self.notes_without_comments = self.build_notes()
    self.comments_on_lines = self.build_comments()
    self.notes = self.notes_without_comments
    if (self.comments_on_lines != None) and (self.fullness != "slender"):
      self.notes = self.notes+" "+self.comments_on_lines

  # Fetches an article's metadata from the database.
  def fetch_extract(self):
    select = ("SELECT article.source AS source, article.title AS title, "+
                "article.non_title AS non_title, "+
                "article.remarks AS remarks, "+
                "article.redacted AS redacted, "+
                "author.full_title AS author, "+
                "author.dob AS dob, author.dod AS dod, "+
                "non_author.name AS non_author "+
              "FROM article "+
              "LEFT JOIN author ON author.code = article.author "+
              "LEFT JOIN non_author "+
                "ON non_author.code = article.non_author "+
              "WHERE article.id = ?;")
    rows = (
      almanack_utils.fetch_to_dict(constants.db, select, (self.idno,)))
    try:
      return rows[0]
    except:
      raise Exception("No article with ID "+str(self.idno)+".")

  # Builds an article's title.
  def build_title(self):
    if self.extract["title"] == None:
      return None
    else:
      result = "`"+self.extract["title"]+"'"
      return result

  # Builds an author's dates.
  def build_dates(self):
    if self.extract["dob"] == None:
      dob = "?"
    else:
      dob = str(self.extract["dob"])
    if self.extract["dod"] == None:
      dod = "?"
    else:
      dod = str(self.extract["dod"])
    result = "("+dob+" -- "+dod+")"
    return result

  # Handles the "non_author" field.
  def build_non_author(self):
    if self.extract["non_author"] in Notes_builder.named_non_authors:
      return self.extract["non_author"]
    else:
      return None

  # Builds an article's notes from its record on the database.
  def build_notes(self):
    if self.redacted == 1:
      r = Notes_builder.redacted_marker
    else:
      r = None
    if self.author != None:
      author_dates = self.author+" "+self.dates
    else:
      author_dates = None
    cited_source = "\\cite{"+self.source+"}"
    result_list = [self.title, self.non_title, author_dates,
                   self.non_author, cited_source]
    result = "" 
    for item in result_list:
      if item != None:
        result = result+item
        if result_list.index(item) != len(result_list)-1:
          result = result+", "
        else:
          result = result+"."
    if r != None:
      result = r+" "+result
    if (self.remarks != None) and (self.fullness != "slender"):
      result = result+" "+self.remarks
    return result

  # Builds an articles line comments.
  def build_comments(self):
    select = ("SELECT line_no, comment FROM comment_on_line "+
              "WHERE article_id = ? ORDER BY line_no ASC;")
    rows = (
      almanack_utils.fetch_to_dict(constants.db, select, (self.idno,)))
    result = ""
    for row in rows:
      result = result+"\P "+str(row["line_no"])+". "+row["comment"]
      if rows.index(row) != len(rows)-1:
        result = result+" "
    if result == "":
      return None
    else:
      return result

  # Returns the class's product as a string.
  def digest(self):
    return self.notes

# Run a demonstration.
def demo():
  print(Notes_builder(1, "full").digest())
  print()
  print(Notes_builder(4, "full").digest())
  print()
  print(Notes_builder(19, "full").digest())
  print()
  print(Notes_builder(26, "full").digest())
  print()
  print(Notes_builder(26, "slender").digest())

# Run and wrap up.
def run():
  demo()
#run()
