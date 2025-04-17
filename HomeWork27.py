# Вариант 1 через property
class Account:
    rate_usd = 0.013
    rate_eur = 0.011
    suffix = "RUB"
    suffix_usd = "USD"
    suffix_eur = "EUR"

    def __init__(self, num, surname, percent, value):
        self.__num = num
        self.__surname = surname
        self.__percent = percent
        self.__value = value
        print(f"Счёт #{self.__num} принадлежащий {self.__surname} был открыт.")
        print("*" * 50)

    def __del__(self):
        print("*" * 50)
        print(f"Счёт #{self.__num} принадлежащий {self.__surname} закрыт")

    @property
    def num(self):
        if isinstance(self.__num, int):
            return self.__num
        else:
            raise ValueError("Только цифры")

    @num.setter
    def num(self, n):
        self.__num = n

    @property
    def sur(self):
        return self.__surname

    @sur.setter
    def sur(self, sn):
        self.__surname = sn

    @property
    def per(self):
        return self.__percent

    @per.setter
    def per(self, pr):
        self.__percent = pr

    @property
    def val(self):
        return self.__value

    @val.setter
    def val(self, vl):
        self.__value = vl

    @staticmethod
    def convert(value, rate):
        return value * rate

    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    @classmethod
    def set_eur_rate(cls, rate):
        cls.rate_eur = rate

    def convert_to_usd(self):
        usd_val = Account.convert(self.__value, Account.rate_usd)
        print(f'Состояние счёта: {usd_val} {Account.suffix_usd}')

    def convert_to_eur(self):
        eur_val = Account.convert(self.__value, Account.rate_eur)
        print(f'Состояние счёта: {eur_val} {Account.suffix_eur}')

    def edit_owner(self, surname):
        self.__surname = surname

    def add_percents(self):
        self.__value += self.__value * self.__percent
        print("Проценты успешно начислены")
        self.print_balance()

    def withdraw_money(self, val):
        if val > self.__value:
            print(f"К сожалению у вас нет {val} {Account.suffix}")
        else:
            self.__value -= val
            print(f"{val}{Account.suffix} было успешно снято")
        self.print_balance()

    def add_money(self, val):
        self.__value += val
        print(f"{val}{Account.suffix} было успешно добавлено")

    def print_balance(self):
        print(f"Текущий баланс {self.__value} {Account.suffix}")

    def print_info(self):
        print("Информация о счёте: ")
        print("-" * 20)
        print(f"#{self.__num}")
        print(f"Владелец: {self.__surname}")
        self.print_balance()
        print(f"Проценты: {self.__percent:.0%}")
        print("-" * 20)


acc = Account(12345, "Долгих", 0.03, 1500)
acc.print_info()
acc.convert_to_usd()
acc.convert_to_eur()
print()

Account.set_usd_rate(2)
acc.convert_to_usd()
Account.set_eur_rate(3)
acc.convert_to_eur()
print()

acc.edit_owner("Валентайн")
acc.print_info()
print()

acc.add_percents()
print()

acc.withdraw_money(100)
print()
acc.add_money(100)
print()


# Вариант 2 через get и set
class Account:
    rate_usd = 0.013
    rate_eur = 0.011
    suffix = "RUB"
    suffix_usd = "USD"
    suffix_eur = "EUR"

    def __init__(self, num, surname, percent, value):
        self.__num = num
        self.__surname = surname
        self.__percent = percent
        self.__value = value
        print(f"Счёт #{self.__num} принадлежащий {self.__surname} был открыт.")
        print("*" * 50)

    def __del__(self):
        print("*" * 50)
        print(f"Счёт #{self.__num} принадлежащий {self.__surname} закрыт")

    def set_num(self):
        return self.__num

    def get_num(self, n):
        self.__num = n

    def set_sur(self):
        return self.__surname

    def get_sur(self, sn):
        self.__surname = sn

    def set_per(self):
        return self.__percent

    def get_per(self, pr):
        self.__percent = pr

    def set_value(self):
        return self.__value

    def get_value(self, vl):
        self.__value = vl

    @staticmethod
    def convert(value, rate):
        return value * rate

    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    @classmethod
    def set_eur_rate(cls, rate):
        cls.rate_eur = rate

    def convert_to_usd(self):
        usd_val = Account.convert(self.__value, Account.rate_usd)
        print(f'Состояние счёта: {usd_val} {Account.suffix_usd}')

    def convert_to_eur(self):
        eur_val = Account.convert(self.__value, Account.rate_eur)
        print(f'Состояние счёта: {eur_val} {Account.suffix_eur}')

    def edit_owner(self, surname):
        self.__surname = surname

    def add_percents(self):
        self.__value += self.__value * self.__percent
        print("Проценты успешно начислены")
        self.print_balance()

    def withdraw_money(self, val):
        if val > self.__value:
            print(f"К сожалению у вас нет {val} {Account.suffix}")
        else:
            self.__value -= val
            print(f"{val}{Account.suffix} было успешно снято")
        self.print_balance()

    def add_money(self, val):
        self.__value += val
        print(f"{val}{Account.suffix} было успешно добавлено")

    def print_balance(self):
        print(f"Текущий баланс {self.__value} {Account.suffix}")

    def print_info(self):
        print("Информация о счёте: ")
        print("-" * 20)
        print(f"#{self.__num}")
        print(f"Владелец: {self.__surname}")
        self.print_balance()
        print(f"Проценты: {self.__percent:.0%}")
        print("-" * 20)


acc = Account("12345", "Долгих", 0.03, 1500)
acc.print_info()
acc.convert_to_usd()
acc.convert_to_eur()
print()

Account.set_usd_rate(2)
acc.convert_to_usd()
Account.set_eur_rate(3)
acc.convert_to_eur()
print()

acc.edit_owner("Валентайн")
acc.print_info()
print()

acc.add_percents()
print()

acc.withdraw_money(100)
print()
acc.add_money(100)
print()
