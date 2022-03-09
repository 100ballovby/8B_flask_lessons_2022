from flask import Flask, render_template
from config import Config  # из файла config.py импортировать класс Config
from flask_sqlalchemy import SQLAlchemy  # класс для работы с БД


app = Flask(__name__)  # сам сайт
app.config.from_object(Config)  # получить настройки сайта из объекта Config
db = SQLAlchemy(app)  # создаю объект для Базы Данных

from routes import *


if __name__ == '__main__':
    app.run()
