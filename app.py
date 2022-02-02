from flask import Flask, render_template


app = Flask(__name__)  # сам сайт


from routes import *


if __name__ == '__main__':
    app.run()
