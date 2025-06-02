def add_title(title):
    def wrapper(func):
        def wrap(*args, **kwargs):
            print(f" {title} ".center(50, "="))
            output = func(*args, **kwargs)
            print("=" * 50)
            return output

        return wrap

    return wrapper


class UserInterface:

    @add_title("Редактирование данных каталога фильмов")
    def wait_user_answer(self):
        # print(" Ввод пользовательских данных ".center(50, "="))
        print("Действия с фильмами:")
        print("1 - Добавление фильма"
              "\n2 - Каталог фильмов"
              "\n3 - просмотр определённого фильма"
              "\n4 - удаление фильма"
              "\nq - выход из программы")
        user_answer = input("Действия с фильмами: ")
        # print("=" * 50)
        return user_answer

    @add_title("Редактирование данных каталога фильмов:")
    def add_user_article(self):
        dict_article = {
            "название фильма:": None,
            "жанр:": None,
            "режиссер:": None,
            "год выпуска:": None,
            'Длительность:': None,
            'Студия:': None,
            'Актёр:': None
        }
        for key in dict_article:
            dict_article[key] = input(f"{key}")
        # print("=" * 50)
        return dict_article

    @add_title("Каталог фильмов:")
    def show_all_articles(self, articles):
        for ind, article in enumerate(articles, 1):
            print(f"{ind}. {article}")
        # print("=" * 50)

    @add_title("Просмотр определённого фильма:")
    def show_one_articles(self, articles):
        for ind, article in enumerate(articles):
            print(f"{article}")

    @add_title("Ввод фильма")
    def get_user_article(self):
        user_article = input("Введите название фильма:")
        return user_article

    @add_title("Просмотр фильма")
    def show_single_article(self, article):
        for key in article:
            print(f"{key} фильм - {article[key]}")

    @add_title("Ошибка!")
    def show_incorrect_title_error(self, user_name):
        print(f"Фильма {user_name} не существует")

    # Удаление
    @add_title("Удаление статьи:")
    def remove_single_article(self, article):
        print(f"Фильм {article} - был удален")

    @add_title("Ошибка!")
    def show_incorrect_answer_error(self, answer):
        print(f"Фильма {answer} не существует")
