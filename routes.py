# здесь будут храниться все переходы на страницы сайта
from flask import render_template, redirect, url_for
from app import app


@app.route('/')  # говорит, что будет происходить, если перейти на главную страницу сайта
def index():  # функция, которая будет отображать главную страницу сайта
    title = 'Главная страница'  # задаю заголовок странице
    return render_template('index.html', title=title)  # отрисовать шаблон главной страницы


@app.route('/contacts')  # новая страница контакты
def contacts():
    return render_template('contacts.html')


@app.route('/about')  # новая страница о нас
def about_us():
    return render_template('about.html')