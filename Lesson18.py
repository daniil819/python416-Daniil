# split() разбивание строк
# print('Стока разделённая пробелами'.split())
# print('www.python.org.ru'.split('.', 1))
# import re
# где он нужен ввод фио
# s = input('Введите ФИО:').split()
# print(s)
# print(f'{s[0]} {s[1][0]}. {s[2][0]}')


# Строка к int
# s = input('Введите числа через пробел:').split()
# print(s)
# num = list(map(int, s))
# print(num)
# print(sum(num))

# Регулярные выражения
# import re
#
# s = "Я ищу совпадения в 2025 году. И я их найду в 2 счёта."
# # print(dir(re))
# reg = r'\.'
# print(re.findall(reg, s))  # возвращает список совпадений с шаблоном (reg(шаблон), s(с чем сравниваем))
# print(re.search(reg, s).span())  # Находит только первое совпадение , а span показывает индексы совпадений
# # print(re.search(reg, s).start())
# # print(re.search(reg, s).end())
# # print(re.search(reg, s).group())
# print(re.split(reg, s))  # Возвращает список, который разбит по заданному шбалону
# print(re.sub(reg, '!', s))  # Поиск и замена

# Спец комбинации
# import re

# s = "Я ищу совпадения в 2025 году. И я их найду в 2 счёта. [Hel_lo] World 6789"
# reg = r'[205]' # перечисление символов
# reg = r'[0-9]'  # Диапазон от 0 до 9
# reg = r'[12][0-9][0-9][0-9]'
# reg = r'[А-яЁё.\]\\[-]'
# reg = r'[A-Za-z]'
# reg = r'[^0-9]'  # Ищем все кроме цифр
# print(re.findall(reg, s))

# Задача
# import re
#
# st = 'Час в 24-часовом формате от 00 до 23ю 2021-06-15T19:49. Минуты в диапазоне от 00 до 59. 2021-06-15T01:09.'
# reg = '[0-2][0-9]:[0-5][0-9]'
# print(re.findall(reg, st))


# СПец пары символов
# import re

# s = "Я ищу совпадения в 2025 году. И я их найду в 2 счёта. [Hel_lo] World 20000000"
# reg = r'\d' #[0-9]
# reg = 'r\D' # [^0-9]
# reg = r'\s'  # [ ]
# reg = r'\S'  # [^ ]
# reg = r'\w' # [А-яА-Za-z0-9_]
# reg = r'\W' # [^А-яА-Za-z0-9_]
# reg = r'AЯ ищу'
# reg = r'Wor-ld\Z'
# reg = r'\bния'

# reg = r'20+'
# print(re.findall(reg, s))
# Кол-во повторений
# + - от 1 до бесконечности
# * - от 0 до бесконечности
# ? - от 0 до 1 повторения

# d = 'Цифры: 7, +17, -42, 0013, 0.3'
# reg = r'[+-]?[\d.]+'
# print(re.findall(reg, d))


# st = '05-03-1987 # Дата рождения'
# print("дата рождения:", re.sub(r'\s#.+', "", st))
# print(re.sub('-', '.', st))
#
# print("дата рождения:", re.sub(r'\s#.+', "",re.sub('-', '.', st)))

# Задача
# import re
#
# st = "author=Пушкин А.С.; title = Евгений Онегин; price =200; year= 1831"
# # reg = r'\w+\s*=\s*\w+\s*\w*\.?\w*\.?'
# # reg = r'\w+\s*=\s*\w+[\s\w.]*'
# reg = r'\w+\s*=[^;]+'
# print(re.findall(reg, st))
# print(re.split(r';\s', st))


# import re
#
# st = '12 сентября 2025 год 456 789456123'
# # reg = r'\d{4}'
# # reg = r'\d{2,4}'
# reg = r'\d{,4}'
# # reg = r'\d{4,}'
# print(re.findall(reg,  st))

# Задача на нахождение номера телефыона
# import re
#
# st = "+7 499 456-45-78, +74994564578, +7 (499) 456 45 78, 74994564578"
# reg = r'\+?7\d{10}'
# print(re.findall(reg, st))

import re
s = "Я ищу совпадения в 2025 году. И я их найду в 2 счёта."

reg = r"^\w+\s\w+"
reg = r"^\w+\s\w+$"
print(re.findall(reg, s))
#
#
# def validate_login(login):
#     return re.findall('r^[a-zA-Z)-9_-]{3,16}$', login)
#
#
# print(validate_login("Python_master"))
# print(validate_login("Python_master"))
