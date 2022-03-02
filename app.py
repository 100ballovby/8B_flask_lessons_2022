from flask import Flask, render_template
from config import Config  # из файла config.py импортировать класс Config


app = Flask(__name__)  # сам сайт
app.config.from_object(Config)  # получить настройки сайта из объекта Config

from routes import *


if __name__ == '__main__':
    app.run()
