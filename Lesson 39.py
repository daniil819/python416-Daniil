# # Jinja
from jinja2 import Template

# from jinja2 import Template
#
#
# class Persone:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_name(self):
#         return self.name
#
#     def get_age(self):
#         return self.age
#
#
# per = Persone("Игорь", 28)
# tm = Template("Мне {{p}} лет. Меня зовут {{p}}")
# msg = tm.render(p=per)
# print(msg)
# cities = [
#     {'id': 1, 'city': 'Москва'},
#     {'id': 2, 'city': 'Смоленск'},
#     {'id': 3, 'city': 'Минск'},
#     {'id': 4, 'city': 'Сочи'},
#     {'id': 5, 'city': 'Ярославль'},
# ]
#
# link = """
# <select>
# {% for c in cities %}
#     {% if c.id > 3 %}
#         <option value="{{ c['id'] }}">{{ c['city'] }}</option>
#     {% elif c.city == 'Москва' %}
#         <option>{{ c['city'] }}</option>
#     {% else %}
#         {{ c['city'] }}
#     {% endif %}
# {% endfor %}
# </select>
# """
#
# tm = Template(link)
# msg = tm.render(cities=cities)
#
# print(msg)

# Задание
# from jinja2 import Template
#
# menu = [
#     {'href': '/index', 'link': 'Главная'},
#     {'href': '/news', 'link': 'Новость'},
#     {'href': '/about', 'link': 'О компании'},
#     {'href': '/show', 'link': 'Магазин'},
#     {'href': '/contacts', 'link': 'Контакты'}
#
# ]
# link = """
# <ul>
#     {% for i in menu %}
#         {% if i.link == 'Главная' %}
#             <li> <a href="{{i['href']}}" class = "active">{{ i['link']}}</li>
#         {% else %}
#             <li> <a href="{{i['href']}}">{{ i['link']}}</li>
#         {% endif %}
#         <li> <a href="{{i['href']}}">{{ i['link']}}</li>
#     {% endfor %}
# </ul>
# """
# tm = Template(link)
# msg = tm.render(menu=menu)
# print(msg)

# # Задание 2 функция
# from jinja2 import Template
#
# cars = [
#     {"model": 'Audi', 'price': 23000},
#     {"model": 'Skoda', 'price': 17300},
#     {"model": 'Renault', 'price': 44300},
#     {"model": 'Wolksvagen', 'price': 21300}
# ]
# # cars = [3, 5, 7]
#
# # tpl = "{{ cs | sum(attribute= 'price') }}"  # Функция
# tpl = "{{ (cs | max(attribute= 'price')).model}}"  # нахождение максимального значения и написание её модели
# tm = Template(tpl)
# msg = tm.render(cs=cars)
# print(msg)

# Макро функции
# html = """
# {% macro set_input(name, value='', type='text', size=20) %}
#     <input type = "{{ type }}" name="{{ name }}" value="{{ value }}" size="{{ size }}">
# {% endmacro %}
#
# <p>{{ set_input('username') }}</p>
# <p>{{ set_input('email') }}</p>
# <p>{{ set_input('password', '', 'password') }}</p>
# """
# tm = Template(html)
# msg = tm.render()
# print(msg)

# Загрузка шаблонов
# from jinja2 import Environment, FileSystemLoader
#
# persons = [
#     {"name": "Алексей"},
#     {"name": "Никит"},
#     {"name": "Виталий"},
# ]
# file_loader = FileSystemLoader("templates")  # привязка папки
# env = Environment(loader=file_loader)  # подгрузка
# tm = env.get_template('about.html')  # привязка к файлу html
# msg = tm.render(users=persons, title="About Jinja")  # привязка переменных
# print(msg)


# БАЗЗЗАЗЗАЗАЗ ДАНННЫХ
import sqlite3

# con = sqlite3.connect("profile.db")  # Соединяемся с базой данных и создаёт файл если его нет
# cur = con.cursor()  # считывает данные с файла
# cur = con.execute('')  # можно писать запросы
# con.close() # Закрывает файл

with sqlite3.connect("profile.db") as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    summa REAL,
    data TEXT
    )""")
    cur.execute("DROP TABLE users")
