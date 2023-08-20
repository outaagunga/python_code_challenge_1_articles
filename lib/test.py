from Author import Author
from Magazine import Magazine
from Article import Article
import pytest 

# Creating instances
def test_author_name():
    author = Author("Outa Agunga")
    assert author.name() == "Outa Agunga"

def test_magazine_name():
    magazine = Magazine("Adventist Magazine", "Health")
    assert magazine.name() == "Adventist Magazine"

def test_article_title():
    author = Author("Outa Agunga")
    magazine = Magazine("Adventist Magazine", "Health")
    article = Article(author, magazine, "Healthy")
    assert article.title() == "Healthy"

def test_author_add_article():
    author = Author("Outa Agunga")
    magazine = Magazine("Adventist Magazine", "Health")
    print("Before adding articles:", len(author.articles()), author.articles())
    
    author.add_article(magazine, "Healthy")
    print("After adding article:", len(author.articles()), author.articles())
    
    author.add_article(magazine, "Vegeterian Way")
    print("After adding article:", len(author.articles()), author.articles())
   
    author.add_article(magazine, "Natural Way")
    print("After adding article:", len(author.articles()), author.articles())

    assert len(author.articles()) == 3

# ... Add more test functions for other methods ...
