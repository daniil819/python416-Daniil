from articles.model import ArticleModel
from view import UserInterface


class Controller:
    def __init__(self):
        self.article_model = ArticleModel()
        self.user_interface = UserInterface()

    def run(self):
        answer = None
        while answer != 'q':
            answer = self.user_interface.wait_user_answer()
            self.check_user_answer(answer)

    def check_user_answer(self, answer):
        if answer == '1':
            article = self.user_interface.add_user_article()
        if answer == '2':
            articles = self.article_model.get_all_articles()
            self.user_interface.show_all_articles(articles)
