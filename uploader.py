"""
This code defines a class which uploads articles from individual files to
the database.
"""

# Standard imports.
import sqlite3

# Local imports.
import constants

####################
# HELPER FUNCTIONS #
####################

def parse_arg(line, tag):
    """ Ronseal. """
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
    """ Ronseal. """
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
    """ Ronseal. """
    trimmed = []
    for line in lines:
        while line.endswith(" ") or line.endswith("\t"):
            line = line[0:len(line)-1]
        trimmed.append(line)
    return trimmed

##############
# MAIN CLASS #
##############

class Uploader:
    """ The class in question. """
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
        with open(path_to_file, "r") as raw_file:
            self.raw = raw_file.read()
        self.update_meta()
        self.update_comments()
        self.purge_meta()

    def update_meta(self):
        """ Parse the "meta" lines in the file the contents of which we're
        uploading. """
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

    def update_comments(self):
        """ Parses any comments on lines. """
        lines = self.raw.split("\n")
        lines = trim_whitespace(lines)
        line_no = 0
        for line in lines:
            if "####COMMENT" in line:
                comment = parse_arg(line, "####COMMENT")
                self.comments[line_no] = comment
            if (("####" not in line) and ("###" not in line) and
                (line != "")):
                line_no = line_no+1

    def purge_meta(self):
        """ Remove any meta lines. """
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

    def fetch_article_id(self):
        """ Calculate the appropriate ID for our new article. """
        conn = sqlite3.connect(constants.db)
        cursor = conn.cursor()
        select = "SELECT id FROM article ORDER BY id DESC;"
        cursor.execute(select)
        row = cursor.fetchone()
        if len(row) == 0:
            return 1
        else:
            last = row[0]
        return last+1

    def upload_comments(self, article_id):
        """ Upload line-comments to the database. """
        result = True
        insert = ("INSERT INTO comment_on_line "+
                      "(article_id, line_no, comment) "+
                  "VALUES (?, ?, ?);")
        conn = sqlite3.connect(constants.db)
        cursor = conn.cursor()
        for line_no in self.comments.keys():
            params = (article_id, line_no, self.comments[line_no])
            try:
                cursor.execute(insert, params)
            except:
                print("Error uploading comment: \""+
                      self.comments[line_no]+"\".")
                result = False
                break
        if result:
            conn.commit()
        conn.close()
        return result

    def upload(self):
        """ Upload an article to the database. """
        result = True
        article_id = self.fetch_article_id()
        if not self.upload_comments(article_id):
            return False
        insert = ("INSERT INTO article "+
                      "(id, content, author, non_author, type, aux_type, "+
                       "humour, source, title, non_title, remarks, "+
                       "redacted, tune, christFlag) "+
                  "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);")
        c_type = self.categories["type"]
        c_aux_type = self.categories["aux_type"]
        c_humour = self.categories["humour"]
        params = (article_id, self.hpml, self.author, self.non_author,
                  c_type, c_aux_type, c_humour, self.source, self.title,
                  self.non_title, self.remarks, self.redacted, self.tune,
                  self.christ_flag)
        connection = sqlite3.connect(constants.db)
        cursor = connection.cursor()
        try:
            cursor.execute(insert, params)
        except sqlite3.OperationalError as error:
            print("Error uploading content:\n"+self.hpml)
            print("Error: "+str(error))
            result = False
        finally:
            if result:
                connection.commit()
            connection.close()
            return result

###########
# TESTING #
###########

def test():
    """ Run unit tests. """
    uploader = Uploader("uploads/TEST1.hpml")
    assert uploader.author == "eliot"
    assert uploader.non_author is None
    assert (uploader.categories ==
            { "type": 1, "aux_type": "n", "humour": "bile" })
    assert uploader.source == "norton"
    assert uploader.title == "Smeg"
    assert uploader.remarks == "Smeg!"
    assert uploader.tune is None
    assert not uploader.redacted
    assert not uploader.christ_flag
    assert uploader.comments == { 1: "Smegma smegmata." }
    print("Tests passed!")

###################
# RUN AND WRAP UP #
###################

def run():
    test()

if __name__ == "__main__":
    run()
