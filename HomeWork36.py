import csv
import requests
from bs4 import BeautifulSoup


def get_html(url):
    row = requests.get(url)
    return row.text


def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    element = soup.find_all('div', class_="vmproduct")
    for el in element:
        exampl = el.find("a", class_='titlee2').text
        price = el.find("span", class_="PricesalesPrice").text

        data = {
            'exampl': exampl,
            'price': price,
        }
        write_csv(data)
    # print(element)


def write_csv(data):
    with open("plugin3.csv", "a", encoding="utf-8-sig") as f:
        writer = csv.writer(f, delimiter=";", lineterminator="\r")
        writer.writerow((data["exampl"], data["price"]))


def main():
    url = "https://webshopdv.ru/"
    get_data(get_html(url))


if __name__ == '__main__':
    main()

# Проверка
# import requests
# row = requests.get("https://webshopdv.ru/")
# print(row)
