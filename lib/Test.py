from Author import Author
from Magazine import Magazine
from Article import Article

# Creating instances
author1 = Author("John Doe")
magazine1 = Magazine("Tech Magazine", "Technology")
article1 = Article(author1, magazine1, "Python Basics")

# Testing methods
print(author1.name())  # Output: John Doe
print(magazine1.name())  # Output: Tech Magazine
print(article1.title())  # Output: Python Basics

author1.add_article(magazine1, "Python Advanced")
print(len(author1.articles()))  # Output: 2

print(magazine1.contributing_authors())  # Output: [Author instance]

print(Magazine.find_by_name("Tech Magazine"))  # Output: Magazine instance

# Test other methods...
