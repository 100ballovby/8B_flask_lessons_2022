# здесь будут храниться все переходы на страницы сайта
from flask import render_template, redirect, url_for
from app import app, db
from forms import ContactForm  # импортирую форму
from models import Questions


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


@app.route('/catalog')
def catalog():
    goods = [
        {
            'good_name': 'Молоток "Тор"',
            'good_price': 89.99,
            'good_description': 'Лучший молоток на рынке молотков.',
            'good_image': 'https://cdn-icons-png.flaticon.com/512/2505/2505252.png',
        },
        {
            'good_name': 'Пила "Дружба"',
            'good_price': 129.45,
            'good_description': 'Распили своего друга весело.',
            'good_image': 'https://cdn-icons-png.flaticon.com/512/3428/3428061.png',
        },
        {
            'good_name': 'Перфоратор "Привет, сосед!"',
            'good_price': 899.34,
            'good_description': 'Вашему соседу скучно жить? Подарите ему радость.',
            'good_image': 'https://cdn-icons.flaticon.com/png/512/3108/premium/3108914.png?token=exp=1643786118~hmac=df37d4cba5b8da32fe6538193aae45b7',
        },
        {
            'good_name': 'Пассатижи "Первый поцелуй"',
            'good_price': 67.19,
            'good_description': 'Каждый раз как в первый раз. Больно и странно.',
            'good_image': 'https://cdn-icons-png.flaticon.com/512/971/971912.png',
        },
    ]
    return render_template('catalog.html', items=goods)  # передаю список товаров в шаблон


@app.route('/question', methods=['GET', 'POST'])  # форма будет работать с методами GET и POST
def send_question():  # когда зайдут на страницу /question
    form = ContactForm()  # создать форму
    if form.validate_on_submit():  # если форма отправляется
        quest = Questions(
            username=form.name.data,
            phone=form.phone.data,
            message=form.message.data)  #записываю данные из формы в класс Question
        db.session.add(quest)  # добавляю вопрос в базу данных
        db.session.commit()  # применя изменения
        return redirect(url_for('send_question'))  # перенаправляю на ту же страницу
    return render_template('send_question.html', form=form)


@app.route('/show-questions')
def show_questions():
    questions = Questions.query.order_by(Questions.created_at).all()  # достать все вопросы из БД сортируя по дате
    return render_template('show_questions.html', items=questions)


@app.route('/show-quest/update/<int:id>', methods=['GET', 'POST'])
def update_question(id):
    question = Questions.query.get_or_404(id)  # если id вопроса не будет найдет, вылетит ошибка 404
    form = ContactForm()
    if form.validate_on_submit():
        question.status = form.status.data
        db.session.commit()
        return redirect(url_for('show_questions'))
    else:
        return render_template('update_question.html', form=form, quest=question)
