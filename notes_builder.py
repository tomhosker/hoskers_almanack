"""
This code holds a class which handles a given article's notes.
"""

# Standard imports.
import os
import sys

# Local imports.
import constants
import almanack_utils

##############
# MAIN CLASS #
##############

class NotesBuilder:
    """ The class in question. """
    # Class variables.
    named_non_authors = ["Anonymous"]
    redacted_marker = "$\mathbb{R}$"

    def __init__(self, idno, fullness):
        self.idno = idno
        self.fullness = fullness
        self.not_on_db = False
        self.extract = self.fetch_extract()
        if self.not_on_db:
            return
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
        self.out = self.notes_without_comments
        if ((self.comments_on_lines is not None) and
            (self.fullness != "slender")):
            self.out = self.out+" "+self.comments_on_lines

    def fetch_extract(self):
        """ Fetches an article's metadata from the database. """
        select = ("SELECT article.source AS source, "+
                      "article.title AS title, "+
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
        rows = almanack_utils.fetch_to_dict(constants.db, select,
                                            (self.idno,))
        try:
            return rows[0]
        except:
            print("No article with ID "+str(self.idno)+".")
            self.not_on_db = True
            return None

    def build_title(self):
        """ Builds an article's title. """
        if self.extract["title"] is None:
            return None
        else:
            result = "`"+self.extract["title"]+"'"
            return result

    def build_dates(self):
        """ Builds an author's dates. """
        if self.extract["dob"] is None:
            dob = "?"
        else:
            dob = str(self.extract["dob"])
        if self.extract["dod"] is None:
            dod = "?"
        else:
            dod = str(self.extract["dod"])
        result = "("+dob+" -- "+dod+")"
        return result

    def build_non_author(self):
        """ Handles the "non_author" field. """
        if self.extract["non_author"] in NotesBuilder.named_non_authors:
            return self.extract["non_author"]
        return None

    def build_notes(self):
        """ Builds an article's notes from its record on the database. """
        if self.redacted == 1:
            pre_result = NotesBuilder.redacted_marker
        else:
            pre_result = None
        if self.author:
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
        if pre_result:
            result = pre_result+" "+result
        if self.remarks and (self.fullness != "slender"):
            result = result+" "+self.remarks
        return result

    def build_comments(self):
        """ Builds an articles line comments. """
        select = ("SELECT line_no, comment FROM comment_on_line "+
                  "WHERE article_id = ? ORDER BY line_no ASC;")
        rows = almanack_utils.fetch_to_dict(constants.db, select,
                                            (self.idno,))
        result = ""
        for row in rows:
            result = result+"\P "+str(row["line_no"])+". "+row["comment"]
            if rows.index(row) != len(rows)-1:
                result = result+" "
        if result == "":
            return None
        else:
            return result

    def digest(self):
        """ Deprecated. """
        return self.out

###########
# TESTING #
###########

def demo():
    """ Run a demonstration. """
    print(NotesBuilder(1, "full").out)
    print()
    print(NotesBuilder(4, "full").out)
    print()
    print(NotesBuilder(19, "full").out)
    print()
    print(NotesBuilder(26, "full").out)
    print()
    print(NotesBuilder(26, "slender").out)

###################
# RUN AND WRAP UP #
###################

def run():
    if "--test" not in sys.argv:
        demo()

if __name__ == "__main__":
    run()
