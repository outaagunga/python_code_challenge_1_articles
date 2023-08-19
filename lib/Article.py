class Article:
    all_articles = []  # This class-level list will store all article instances

    def __init__(self, author, magazine, title):
        self.__author = author
        self.__magazine = magazine
        self.__title = title
        Article.all_articles.append(self)  # Add the instance to the all_articles list

    def title(self):
        return self.__title

    @classmethod
    def all(cls):
        return cls.all_articles

    # Other methods will be added later


class Article:
    # ... (previous code)

    def author(self):
        return self.__author

    def magazine(self):
        return self.__magazine

    # Other methods...
