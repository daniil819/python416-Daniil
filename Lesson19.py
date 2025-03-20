# Flags
# import re
#
# print(re.findall(r"\w+", '12 + й'))
# print(re.findall(r"\w+", '12 + й', flags=re.ASCII))
#
# text = 'helo world'
# print(re.findall(r'\w+', text))
# print(re.findall(r'\w+', text, re.DEBUG))


# re.IGNORECASE
# import re
# text = 'helLo worLd'
# print(re.findall(r'l', text, re.IGNORECASE))

# re.DOTALL
# import re
# text = """ one two """
# # print(re.findall(r"one.\w+", text))
# # print(re.findall(r"one.\w+", text, re.DOTALL))
# print(re.findall(r"one$", text))
# print(re.findall(r"one$", text, re.MULTILINE))

# re.VERBOSE
# import re
#
# print(re.findall("""[a-z.-]+@[a-z.]+""", 'test@mail.ru', re.VERBOSE))

# флаги
# import re
#
# text = """Python,
# python,
# PYTHON
# """
# reg = "(?mi)python"
# print(re.findall(reg, text))

# Ленивое совпадение
# text = "<body>Пример жадного соотвествия регулярных выражений</body>"
# print(re.findall("<.*?>", text))

# *?, +?, ??
# {m, n}?, {,n}?, {m,}?

# |
# s = "Петя, Ольга и Витя отлично учаться!"
# reg = "Петя|Ольга|Витя|Вася"
# print(re.findall(reg, s))


# s = "int = 4, float = 4.0f. double = 8.0"
# # reg = r"int\s*=\s*\d[\w.]* | float\s*=\s*\d[\w.]*"
# reg = r"(?:int|float)\s*=\s*\d[\w.]*"
# print(re.findall(reg, s))

# re.search
# s = "Word2006, PS6, AI5"
# reg = r"[a-z]+\d+"
# print(re.findall(reg, s, re.IGNORECASE))
# print(re.search(reg, s, re.IGNORECASE))

# re.split
# import re
#
# s = "5 + 7*2 - 4"
# reg = r"\s*[+*-]\s*"
# print(re.split(reg, s))
#
# s = "5 + 7*2 - 4"
# reg = r"\s*([+*-])\s*"
# print(re.split(reg, s))


# ЗАДАНИЕ
# s = "28-12-1911"  # 01 - 31
# reg = r"(0[1-9]|[12][0-9]|[3][01])-(0[1-9]|1[0-2])-(19[0-9][0-9]|20[0-9][0-9])"
# print(re.findall(reg, s))
# print(re.search(reg, s))

# Обращение по индексу
# s = "Word2006, PS6, AI5"
# reg = r"([a-z]+)(\d+)"
# print(re.findall(reg, s, re.IGNORECASE))
# print(re.search(reg, s, re.IGNORECASE).group())
# m = re.search(reg, s, re.IGNORECASE)
# print(m[1])
# print(m[2])
# print(m[0])  # Всё совпадение шаблона

# Меняем местами
# s = "Сомалёт прилетает 10/23/2025. Будем рады вас видеть после 10/24/2025. "
# reg = r"(\d{2})/(\d{2})/(\d{4})"
# print(re.sub(reg, r"\2.\1.\3", s))  # 2,1,3 - номер скобки

# Ссылки
# s = 'yandex.com and yandex.ru'
# reg = r'(([a-z0-9-]{2,}\.)+[a-z]{2,4})'
# print(re.sub(reg, r'http://\1', s))

# РЕКУРСИЯ
# def elevator(n):
#     if n == 0:  # базовый случай
#         print('Вы в подвале')
#         return
#
#     print("=>", n)
#     elevator(n - 1)
#     print(n, end=" ")
#
#
# n1 = int(input("На каком, вы этаже?:"))
# elevator(n1)

# Задача с 2 способами через рекурсия и обычная функция
# Без рекурсии
# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res += i
#     return res
#
#
# print(sum_list([1, 3, 5, 7, 9]))


# Рекурсия
def sum_list(lst):
    if len(lst) == 1:
        print(lst, "=> lst[0]:", lst[0])
        return lst[0]
    else:
        print(lst, "=> lst[0]:", lst[0])
        return lst[0] + sum_list(lst[1:])


print(sum_list([1, 3, 5, 7, 9]))


# Преобразование числа
# def to_str(n, base):
#     convert = '0123456789ABCDEF'
#     if n < base:
#         return convert[n]
#     else:
#         return to_str(n // base, base) + convert[n % base]
#
#
# print(to_str(254, 16))

# isinstance
# names = ['Adam', ["Bob", ["Chet", "Cat"], "Bard", "Bert"], 'Alex', ["Bea", "Bill"], "Ann"]
# print(names)
# print(len(names))
# print(names[0])
# print(isinstance(names[0], list))
# print(names[1])
# print(isinstance(names[1][1], list))
# print(isinstance(names[1][1][0], list))


# names = ['Adam', ["Bob", ["Chet", "Cat"], "Bard", "Bert"], 'Alex', ["Bea", "Bill"], "Ann"]
#
#
# def count_items(item_list):
#     count = 0
#     for item in item_list:
#         if isinstance(item, list):
#             count += count_items(item)
#         else:
#             count += 1
#         return count
#
#
# print(count_items(names))
