import sqlite3
import os
from flask import Flask, render_template, flash, request, g, abort
from FourDz.sitedb import FDataBase

DATABASE = '/tmp/flskDZ.db'
DEBUG = True
SECRET_KEY = 'efwduimfifueddiwkefurdekiudergikuedrgikhekdrghi'

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path, "flaskDZ.db")))


def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con


def create_db():
    db = connect_db()
    with app.open_resource("sq_db.sql", "r") as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.route('/')
def index():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('index.html', menu=dbase.get_menu())


@app.route("/add_post", methods=["POST", "GET"])
def add_post():
    db = get_db()
    dbase = FDataBase(db)

    if request.method == "POST":
        if len(request.form["name"]) > 4 and len(request.form["post"]) > 10:
            res = dbase.add_post(request.form["name"], request.form["post"])
            if not res:
                flash("Ошибка", category="error")
            else:
                flash("Предложение отправлено успешно", category="success")
        else:
            flash("Ошибка отправки", category="error")

    return render_template('add_post.html', menu=dbase.get_menu())


@app.route("/contact")
def contact():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('contact.html', menu=dbase.get_menu())


@app.route("/about")
def about():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('about.html', menu=dbase.get_menu())


@app.route("/post/<int:id_post>")
def show_post(id_post):
    db = get_db()
    dbase = FDataBase(db)
    title, post = dbase.get_post(id_post)
    if not title:
        abort(404)

    return render_template('post.html', menu=dbase.get_menu(), title=title, post=post)


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


if __name__ == "__main__":
    app.run()
