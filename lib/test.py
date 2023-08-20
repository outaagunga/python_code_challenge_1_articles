from Author import Author
from Magazine import Magazine
from Article import Article
import pytest 

# Creating instances
def test_author_name():
    author = Author("John Doe")
    assert author.name() == "John Doe"

def test_magazine_name():
    magazine = Magazine("Tech Magazine", "Technology")
    assert magazine.name() == "Tech Magazine"

def test_article_title():
    author = Author("John Doe")
    magazine = Magazine("Tech Magazine", "Technology")
    article = Article(author, magazine, "Python Basics")
    assert article.title() == "Python Basics"

def test_author_add_article():
    author = Author("John Doe")
    magazine = Magazine("Tech Magazine", "Technology")
    print("Before adding articles:", len(author.articles()), author.articles())
    
    author.add_article(magazine, "Python Basics")
    print("After adding article:", len(author.articles()), author.articles())
    
    author.add_article(magazine, "Python Advanced")
    print("After adding article:", len(author.articles()), author.articles())
   
    author.add_article(magazine, "Python Extra")
    print("After adding article:", len(author.articles()), author.articles())

    assert len(author.articles()) == 3

# ... Add more test functions for other methods ...
