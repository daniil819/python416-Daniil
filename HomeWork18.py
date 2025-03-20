import re

log = ('Тест: 123456@i.ru, 123_456@ru.name.ru, login@i.ru, логин-1@i.ru, login.3@i.ru, login.3-67@i.ru, '
       '1login@ru.name.ru')
print(log)
reg = r'\w[А-я - a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]'
print(re.findall(reg, log))
# r'\w[a-zA-Z0-9-+-.]+@[a-zA-z]+\.[a-zA-z-0-9]'
