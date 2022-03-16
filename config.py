# настройки для вашего сайта
import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'poprobui-ugadai'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.sqlite'  # путь к файлу БД
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # отслеживание изменений в структуре БД

