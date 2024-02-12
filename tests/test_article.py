"""
This code tests the Article class.
"""

# Source imports.
from source.article import Article

###########
# TESTING #
###########

def test_article():
    """ Test that we can create an Article object, and that its methods behave
    as expected. """
    article = Article(record_id=1)
    assert isinstance(article.digest(), str)
