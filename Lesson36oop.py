# import csv
#
# with open("student1.csv", 'w') as f:
#     names = ['Имя', "Возраст"]
#     writer = csv.DictWriter(f, delimiter=";", lineterminator='\r', fieldnames=names)
#     writer.writeheader()
#     writer.writerow({"Имя": "Саша", "Возраст": 6})
#     writer.writerow({"Имя": "Маша", "Возраст": 15})
#     writer.writerow({"Имя": "Вова", "Возраст": 14})
# import csv
#
# # Задание 2
# data = [{
#     'hostname': 'sw1',
#     'location': 'London',
#     'model': '3750',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw2',
#     'location': 'Liverpool',
#     'model': '3850',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw3',
#     'location': 'Liverpool',
#     'model': '3650',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw4',
#     'location': 'London',
#     'model': '3650',
#     'vendor': 'Cisco'
# }]
#
# with open("dict_writer.csv", 'w') as f:
#     writer = csv.DictWriter(f, delimiter=';', lineterminator='\r', fieldnames=[0].keys())
#     writer.writrheader()
#     for d in data:
#         writer.writerow(d)
# import re
# from lib2to3.pygram import pattern_grammar
#
# # ПАРСИНГ САЙТА
# from bs4 import BeautifulSoup
#
# f = open('index.html').read()
# soup = BeautifulSoup(f, "html.parser")
import csv

# row = soup.find('div', class_='name').text
# row2 = soup.find_all('div', class_='name')
# row3 = soup.find_all('div', class_='row')
# row4 = soup.find_all('div', class_='row')[1].find_all('div', class_='name')
# row5 = soup.find_all('div', class_='row')[1].find_all('div', {'class': 'name'})
# row6 = soup.find('div', {"data-set": "salary"})
# row7 = soup.find('div', string="Alena").find_parent(class_='row')  # получаем доступ к выше лежашим напрямую
# row8 = soup.find("div", id="whois3")  # получение по id
# row9 = soup.find("div", id="whois3").find_next_sibling()  # получение тега после
# row10 = soup.find("div", id="whois3").find_previous_sibling()  # получение тега до
# print(row)
# print(row2)
# print(row3)
# print(row4)
# print(row5)
# print(row6)
# print(row7)
# print(row8)
# print(row9)
# print(row10)

# Получение и удаление ненужных элементов


# def get_salary(s):
#     pattern = r"\d+"
#     # res = re.findall(pattern, s)[0]
#     res = re.search(pattern, s).group()
#     print(res)
#
#
# row = soup.find_all('div', {"data-set": "salary"})
# for i in row:
#     get_salary(i.text)

# import requests
# from bs4 import BeautifulSoup
#
#
# def get_html(url):
#     row = requests.get(url)
#     return row.text
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find("div", id="intro").find("h1", class_="wp-block-heading").text
#     return p1
#
#
# def main():
#     url = 'https://ru.wordpress.org/'
#     print(get_data(get_html(url)))
#
#
# if __name__ == "__name__":
#     main()

# r = requests.get('https://ru.wordpress.org/')
# # print(r.content)
# print(type(r.text))

# Просмотор блоков и сохранение о них данных
# import csv
# import re
# import requests
# from bs4 import BeautifulSoup
#
#
# def write_csv(data):
#     with open("plugins.csv", "a") as f:
#         writer = csv.writer(f, delimiter=",", lineterminator="\r")
#         writer.writerow((data["name"], data["url"], data["rating"]))
#
#
# def refined(s):
#     return re.sub(r"\D+", "", s)
#
#
# def get_html(url):
#     row = requests.get(url)
#     return row.text
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find_all("section", class_="plugin-section")[1]
#     plugins = p1.find_all("li")
#
#     for plugin in plugins:
#         name = plugin.find("h3").text
#         # url = plugin.find("h3").find("a").get("href")
#         url = plugin.find("h3").find("a")["href"]
#         rating = plugin.find("span", class_="rating-count").text
#         r = refined(rating)
#
#         data = {"name": name, "url": url, "rating": r}
#         write_csv(data)
#
#
# def main():
#     url = "https://ru.wordpress.org/plugins/"
#     get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()


#
import csv
import requests
from bs4 import BeautifulSoup


def get_html(url):
    row = requests.get(url)
    return row.text


def refine_cy(s):
    return s.split()[-1]


def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    elements = soup.find_all("li", class_="wp-block-post")
    for el in elements:
        name = el.find("h3").text
        url = el.find("h3").find("a").get("href")
        snippet = el.find("div", class_="entry-excerpt").text.strip()
        active = el.find("span", class_="active-installs").text.strip()
        tested = el.find("span", class_="tested-with").text.strip()
        test = refine_cy(tested)
        data = {
            "name": name,
            "url": url,
            "snippet": snippet,
            "active": active,
            "test": test
        }
        write_csv(data)


def write_csv(data):
    with open("plugins1.csv", "a", encoding="utf-8-sig") as f:
        writer = csv.writer(f, delimiter=",", lineterminator="\r")
        writer.writerow((data["name"], data["url"], data["snippet"], data["active"], data["test"]))


def main():
    for i in range(3, 23):
        url = f"https://ru.wordpress.org/plugins/browse/blocks/page/{i}/"
        get_data(get_html(url))


if __name__ == '__main__':
    main()
