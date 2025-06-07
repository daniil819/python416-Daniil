from jinja2 import Environment, FileSystemLoader

persons = [
    {"name": "Алексей"},
    {"name": "Никит"},
    {"name": "Виталий"},
]
file_loader = FileSystemLoader("templates_two")
env = Environment(loader=file_loader)
tm = env.get_template('dzMain.html')
msg = tm.render(users=persons, title="About Jinja")
print(msg)