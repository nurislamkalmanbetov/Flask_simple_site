from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Главная страница<h1>"


@app.route("/about")
def about():
    return "<h1>Страница о нас!<h1>"



if __name__== '__main__':
    app.run(debug=True) # для просмотра ошибок

