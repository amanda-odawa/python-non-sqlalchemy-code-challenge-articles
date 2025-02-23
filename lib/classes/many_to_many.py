class Article:
    all = [] 

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise ValueError("Author must be of type Author")
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be of type Magazine")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string of 5 to 50 letters")

        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all.append(self)

    @property
    def title(self):
        if hasattr(self, "_title") and isinstance(self._title, str) and 5 <= len(self._title) <= 50:
            return self._title
        else:
            raise ValueError("Title must be a string of 5 to 50 letters")

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        if isinstance(new_author, Author):
            self._author = new_author
        else:
            raise ValueError("Author must be of type Author")

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, new_magazine):
        if isinstance(new_magazine, Magazine):
            self._magazine = new_magazine
        else:
            raise ValueError("Magazine must be of type Magazine")


class Author:
    _articles = []  

    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Author's name must be a string")
        self._name = name

    @property
    def name(self):
        if hasattr(self, "_name") and isinstance(self._name, str) and len(self._name) > 0:
            return self._name
        else:
            raise ValueError("Author's name must be a string")

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        categories = list(set(article.magazine.category for article in self.articles()))
        return categories if categories else None


class Magazine:
    _articles = []  

    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Magazine name must be a string of 2 to 16 letters")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a string")

        self._name = name
        self._category = category

    @property
    def name(self):
        if hasattr(self, "_name") and isinstance(self._name, str) and 2 <= len(self._name) <= 16:
            return self._name
        else:
            raise ValueError("Magazine name must be a string of 2 to 16 letters")

    @name.setter
    def name(self, new_name):
        if hasattr(self, "_name") and isinstance(new_name, str) and 2 <= len(new_name) <= 16:
            self._name = new_name
        else:
            raise ValueError("Magazine name must be a string of 2 to 16 letters")

    @property
    def category(self):
        if hasattr(self, "_category") and isinstance(self._category, str) and len(self._category) > 0:
            return self._category
        else:
            raise ValueError("Category must be a string")

    @category.setter
    def category(self, new_category):
        if hasattr(self, "_category") and isinstance(new_category, str) and len(new_category) > 0:
            self._category = new_category
        else:
            raise ValueError("Category must be a string")

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        contributors = {}
        for article in self.articles():
            contributors[article.author] = contributors.get(article.author, 0) + 1

        contributing_authors = [author for author, count in contributors.items() if count > 2]
        return contributing_authors if contributing_authors else None
