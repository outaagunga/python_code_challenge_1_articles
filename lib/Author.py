from Article import Article
class Author:
    def __init__(self, name):
        self._name = name
        self.__articles = [] 
    def name(self):
        return self._name

    def articles(self):
        return self.__articles


    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self.__articles.append(article)

    def topic_areas(self):
        return list(set([article.magazine().category() for article in self.__articles]))




