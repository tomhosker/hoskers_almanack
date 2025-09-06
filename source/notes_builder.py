"""
This code defines a class which handles a given article's notes.
"""

# Standard imports.
from dataclasses import dataclass
from enum import Enum

# Local imports.
from .utils import AlmanackError, fetch_to_dict
from .configs import COMPONENT_SEPARATOR, REDACTED_MARKER, REMARKS_SYMBOL
from .constants import ColumnNames, Fullnesses

# Local constants.
NAMED_NON_AUTHORS = ("Anonymous",)

#########
# ENUMS #
#########

class AuthorColumnNames(Enum):
    """ Gives the names of the columns of the Author table. """
    DOB = "dob"
    DOD = "dod"

class CommentColumnNames(Enum):
    """ Gives the names of the columns of the CommentOnLine table. """
    LINE_NUM = "line_num"
    COMMENT = "comment"

##############
# MAIN CLASS #
##############

@dataclass
class NotesBuilder:
    """ The class in question. """
    article_id: int
    fullness: Fullnesses = Fullnesses.FULL
    extract: dict = None
    source: str = None
    non_title: str = None
    remarks: str = None
    redacted: str = None
    author: str = None
    title: str = None
    dates: str = None
    non_author: str = None
    notes_without_comments: str = None
    comments_on_lines: str = None

    def digest(self):
        """ Get a LaTeX representation of the article's notes. """
        self.extract = self.fetch_extract()
        self.source = self.extract[ColumnNames.SOURCE.value]
        self.non_title = self.extract[ColumnNames.NON_TITLE.value]
        self.remarks = self.extract[ColumnNames.REMARKS.value]
        self.redacted = self.extract[ColumnNames.REDACTED.value]
        self.author = self.extract[ColumnNames.AUTHOR.value]
        self.title = self.build_title()
        self.dates = self.build_dates()
        self.non_author = self.build_non_author()
        self.notes_without_comments = self.build_notes()
        self.comments_on_lines = self.build_comments()
        result = self.notes_without_comments
        if (self.comments_on_lines and (self.fullness == Fullnesses.FULL)):
            result = result+" "+self.comments_on_lines
        return result

    def fetch_extract(self) -> list[dict]:
        """ Fetches an article's metadata from the database. """
        select = (
            "SELECT Article.source AS source, "+
                "Article.title AS title, "+
                "Article.non_title AS non_title, "+
                "Article.remarks AS remarks, "+
                "Article.redacted AS redacted, "+
                "Author.full_title AS author, "+
                "Author.dob AS dob, author.dod AS dod, "+
                "NonAuthor.name AS non_author "+
            "FROM Article "+
            "LEFT JOIN Author ON Author.code = Article.author "+
            "LEFT JOIN NonAuthor ON NonAuthor.code = Article.non_author "+
            "WHERE Article.id = ?;"
        )
        rows = fetch_to_dict(select, (self.article_id,))
        if not rows:
            raise AlmanackError(f"No article with id: {self.article_id}")
        result = rows[0]
        return result

    def build_title(self) -> str|None:
        """ Builds an article's title. """
        if self.extract[ColumnNames.TITLE.value]:
            result = "\\refpoem{"+self.extract[ColumnNames.TITLE.value]+"}"
            return result
        return None

    def build_dates(self) -> str:
        """ Builds an author's dates. """
        dob = self.extract[AuthorColumnNames.DOB.value] or "?"
        dod = self.extract[AuthorColumnNames.DOD.value] or "?"
        result = f"({dob} -- {dod})"
        return result

    def build_non_author(self) -> str|None:
        """ Handles the "non_author" field. """
        non_author = self.extract[ColumnNames.NON_AUTHOR.value]
        if non_author in NAMED_NON_AUTHORS:
            return non_author
        return None

    def build_notes(self) -> str:
        """ Builds an article's notes from its record on the database. """
        author_dates = None
        if self.author:
            author_dates = self.author+" "+self.dates
        cited_source = "\\citetitle{"+self.source+"}"
        components = [
            self.title,
            self.non_title,
            author_dates,
            self.non_author,
            cited_source
        ]
        components = list(filter(None, components))
        result = COMPONENT_SEPARATOR.join(components)+"."
        if self.redacted:
            result = REDACTED_MARKER+" "+result
        if self.remarks and (self.fullness == Fullnesses.FULL):
            result = f"{result} {REMARKS_SYMBOL} {self.remarks}"
        return result

    def build_comments(self) -> str|None:
        """ Builds an articles line comments. """
        select = (
            "SELECT line_num, comment "+
            "FROM CommentOnLine "+
            "WHERE article_id = ? "+
            "ORDER BY line_num ASC;"
        )
        rows = fetch_to_dict(select, (self.article_id,))
        comments = []
        if not rows:
            return None
        for row in rows:
            line_num = row[CommentColumnNames.LINE_NUM.value]
            comment_text = row[CommentColumnNames.COMMENT.value]
            comment = f"$\\boldsymbol{{\\ell}}{line_num}$: {comment_text}"
            comments.append(comment)
        result = " ".join(comments)
        return result
