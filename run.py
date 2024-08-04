from flask import Flask, render_template
from werkzeug.security import generate_password_hash, check_password_hash
from requests import request
import mypy
import os

app = Flask(__name__)

app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
)
#неинформативный комментарий
config_path = 'config.py'

if os.path.exists(config_path):
    app.config.from_pyfile(config_path, silent=True)

db.init_app(app)


# username_db, password_db = ('nik','12345')


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return do_the_login()
#     else:
# return show_the_login_form()

# def do_the_login():
#
#     if request.username == username_db and \
#             check_password_hash(generate_password_hash(password), password_db):
#         return f'{username} success enter'
#     else:
#         return 'Wrong credentials'


# @app.route('/login/<username>&<password>')
# def hash_pass(username, password):


@app.route('/')
def home():
    return render_template('index.html', title='Главная')


@app.route('/html_page')
def html_page():
    return render_template('html_page.html', title='html')


@app.route('/css_page')
def css_page():
    return render_template('css_page.html', title='css')


@app.route('/js_page')
def js_page():
    return render_template('js_page.html', title='js')


@app.route('/python_page')
def python_page():
    return render_template('python_page.html', title='python')


@app.route('/flask_page')
def flask_page():
    return render_template('flask_page.html', title='flask')


@app.route('/django_page')
def django_page():
    return render_template('django_page.html', title='django')


if __name__ == '__main__':
    app.run(debug=True, port=5656)
