# настройки для вашего сайта
import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'poprobui-ugadai'

