def sr(fn):
    def wrap(*args):
        st = ""
        for i in args:
            st += str(i) + ', '
        print("Средн-арефм:", st[:-2], '=', fn(*args) / len(args))

    return wrap


@sr
def summa(*args):
    st = ""
    for i in args:
        st += str(i) + ', '
    print("Сумма чисел:", st[:-2], '=', sum(args))
    return sum(args)


summa(2, 3, 3, 4)
