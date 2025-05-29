# # Сервер
# import socket
# from view import index, blog
#
# URLS = {
#     '/': index,
#     '/blog': blog
# }
#
#
# def parse_request(request):
#     parsed = request.split()
#     method = parsed[0]  # GET
#     url = parsed[1]  # / или /blog
#     return method, url
#
#
# def generate_headers(method, url):
#     if method != "GET":
#         return 'HTTP/1.1 405 Method Not Allowed!\n\n', 405
#     if url not in URLS:
#         return 'HTTP/1.1 404 Page Not Found!\n\n', 404
#     return 'HTTP/1.1 200 OK!\n\n', 200
#
#
# def generate_content(code, url):
#     if code == 404:
#         return '<h1>404</h1><h3>Page Not Found</h3>'
#     if code == 405:
#         return '<h1>405</h1><h3>Method Not Allowed</h3>'
#     return URLS[url]()
#
#
# def generate_response(request):
#     method, url = parse_request(request)
#     headers, code = generate_headers(method, url)
#     body = generate_content(code, url)
#     return (headers + body).encode()
#
#
# def run():
#     server_soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server_soket.bind(('127.0.0.1', 5000))  # 127.0.0.1:5000
#     server_soket.listen()
#
#     while True:
#         client_soket, addr = server_soket.accept()
#
#         request = client_soket.recv(1024)
#
#         print(f"Клиент: {addr} => \n{request.decode('utf-8')}\n")
#
#         response = generate_response(request.decode())
#         client_soket.sendall(response)
#         client_soket.close()
#
#
# if __name__ == '__main__':
#     run()

# jinja2
# from jinja2 import Template
#
# name = "Игорь"
# age = 28
# tm = Template("Мне {{a * 2}} лет. Меня зовут {{n.upper()}}")
# msg = tm.render(n=name, a=age)
# print(msg)

# ЧЕРЕЗ СПИСКИ
# from jinja2 import Template
# per = {'name': 'Игорь', 'age': 28}
# tm = Template("Мне {{p}} лет. Меня зовут {{p}}")
# msg = tm.render(p=per)
# print(msg)

# ЧЕРЕЗ КЛАСС
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

cities = [

]