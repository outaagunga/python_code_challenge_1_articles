
class Magazine:
    all_magazines = []

    def __init__(self, name, category):
        self.__name = name
        self.__category = category
        self.__articles = []
        Magazine.all_magazines.append(self)

    def contributing_authors(self):
        authors_count = {}  # A dictionary to count the number of articles by each author
        for article in self.__articles:
            author = article.author()  
            authors_count[author] = authors_count.get(author, 0) + 1

        return [author for author, count in authors_count.items() if count > 2]

    @classmethod
    def find_by_name(cls, name):
        for magazine in cls.all_magazines:
            if magazine.name() == name:
                return magazine

    @classmethod
    def article_titles(cls):
        titles = []
        for magazine in cls.all_magazines:
            titles.extend([article.title() for article in magazine.articles()])
        return titles

    def name(self):
        return self.__name

    def category(self):
        return self.__category

    def articles(self):
        return self.__articles

    # Other methods...
