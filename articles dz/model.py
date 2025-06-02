import pickle
import os


class Article:
    def __init__(self, name, genre, author, year, time, study, actor):
        self.name = name
        self.genre = genre
        self.author = author
        self.year = year
        self.time = time
        self.study = study
        self.actor = actor

    def __str__(self):
        return f"{self.name} ({self.genre} {self.author} {self.year})"


class ArticleModel:
    def __init__(self):
        self.db_name = 'db.txt'
        self.articles = self.load_data()  # {}

    def add_article(self, dict_article):
        article = Article(*dict_article.values())
        self.articles[article.name] = article

    def get_all_articles(self):
        return self.articles.values()

    def get_single_articles(self, user_name):
        article = self.articles[user_name]
        dict_article = {
            "название": article.name,
            "жанр": article.genre,
            "Режиссёр": article.author,
            "год": article.year,
            "время": article.time,
            "студия": article.study,
            "актёр": article.actor
        }
        return dict_article

    def remove_article(self, user_name):
        return self.articles.pop(user_name)

    def save_data(self):
        with open(self.db_name, "wb") as f:
            pickle.dump(self.articles, f)

    def load_data(self):
        if os.path.exists(self.db_name):
            with open(self.db_name, "rb") as f:
                return pickle.load(f)
        else:
            return dict()
