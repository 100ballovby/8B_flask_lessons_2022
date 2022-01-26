from flask import Flask, render_template


app = Flask(__name__)  # сам сайт


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


if __name__ == '__main__':
    app.run()
