from flask_wtf import FlaskForm  # импортируем класс формы
from wtforms import StringField, TextAreaField, SubmitField, BooleanField  # импортируем поля
from wtforms.validators import DataRequired  # импортируем валидатор (поле обязательно)


class ContactForm(FlaskForm):
    name = StringField('Ваше имя: ', validators=[DataRequired()])
    phone = StringField('Номер телефона: ', validators=[DataRequired()])
    message = TextAreaField('Ваше сообщение: ')
    status = BooleanField('Обработано?')
    submit = SubmitField('Отправить')
