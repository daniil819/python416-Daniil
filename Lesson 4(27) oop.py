# САМЫЙ СЛОЖНЫЙ ТИП МЕТОДА "класс"
# class Date:
#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @classmethod
#     def from_string(cls, string_date):
#         day, month, year = map(int, string_date.split("."))  # [23, 01, 2025]
#         date = cls(day, month, year)  # d = Date(day, month, year)
#         return date
#
#     def string_to_db(self):
#         return f"{self.year}-{self.month}-{self.day}"
#
#
# # string_date = "23.01.2025"
# # day, month, year = map(int, string_date.split("."))  # [23, 01, 2025]
# # d = Date(day, month, year)
# d = Date.from_string("15.11.2025")
# print(d.string_to_db())

# Большая задача

# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = "RUB"
#     suffix_usd = "USD"
#     suffix_eur = "EUR"
#
#     def __init__(self, num, surname, percent, value):
#         self.num = num
#         self.surname = surname
#         self.percent = percent
#         self.value = value
#         print(f"Счёт #{self.num} принадлежащий {self.surname} был открыт.")
#         print("*" * 50)
#
#     def __del__(self):
#         print("*" * 50)
#         print(f"Счёт #{self.num} принадлежащий {self.surname} закрыт")
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f'Состояние счёта: {usd_val} {Account.suffix_usd}')
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.value, Account.rate_eur)
#         print(f'Состояние счёта: {eur_val} {Account.suffix_eur}')
#
#     def edit_owner(self, surname):
#         self.surname = surname
#
#     def add_percents(self):
#         self.value += self.value * self.percent
#         print("Проценты успешно начислены")
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.value:
#             print(f"К сожалению у вас нет {val} {Account.suffix}")
#         else:
#             self.value -= val
#             print(f"{val}{Account.suffix} было успешно снято")
#         self.print_balance()
#
#     def add_money(self, val):
#         self.value += val
#         print(f"{val}{Account.suffix} было успешно добавлено")
#
#     def print_balance(self):
#         print(f"Текущий баланс {self.value} {Account.suffix}")
#
#     def print_info(self):
#         print("Информация о счёте: ")
#         print("-" * 20)
#         print(f"#{self.num}")
#         print(f"Владелец: {self.surname}")
#         self.print_balance()
#         print(f"Проценты: {self.percent:.0%}")
#         print("-" * 20)
#
#
# acc = Account("12345", "Долгих", 0.03, 1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
#
# Account.set_usd_rate(2)
# acc.convert_to_usd()
# Account.set_eur_rate(3)
# acc.convert_to_eur()
# print()
#
# acc.edit_owner("Дюма")
# acc.print_info()
# print()
#
# acc.add_percents()
# print()
#
# acc.withdraw_money(100)
# print()
# acc.add_money(100)
# print()

# Задача 2
import re


class UserData:
    def __init__(self, fio, old, ps, weight):
        self.verify_fio(fio)
        self.verify_old(old)
        self.verify_weight(weight)
        self.verify_ps(ps)
        self.__fio = fio
        self.__old = old
        self.__ps = ps
        self.__weight = weight

    @staticmethod
    def verify_fio(fio):
        if not isinstance(fio, str):
            raise TypeError("ФИО должно быть строкой")
        f = fio.split()  # ['Волков', 'Иго!!рь', 'Николаевич']
        # print(f)
        if len(f) != 3:
            raise TypeError("Неверный формат фио")
        letters = "".join(re.findall(r"[a-zа-яё-]", fio, flags=re.IGNORECASE))  # ВолковИгорьНиколаевич
        for s in f:
            # print(s.strip(letters))
            if len(s.strip(letters)) != 0:
                raise TypeError("В ФИО можно использовать только буквы и дефисы")

    @staticmethod
    def verify_old(old):
        if not isinstance(old, int) or not 14 <= old <= 100:  # old < 14 or old > 100
            raise TypeError("Возраст от 14 до 100")

    @staticmethod
    def verify_weight(w):
        if not isinstance(w, float) or w < 20:
            raise TypeError("Вес должен быть вещественным числом от 20 и выше")

    @staticmethod
    def verify_ps(ps):
        if not isinstance(ps, str):
            raise TypeError("Паспорт должен быть строкой")
        s = ps.split()
        if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
            raise TypeError("неверный формат")


p1 = UserData("Волков Игорь Николаевич", 45, "1234 567890", 80.8)
