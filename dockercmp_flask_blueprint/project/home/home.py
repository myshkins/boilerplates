from flask import Blueprint, render_template, redirect, url_for
from flask import current_app as app
import requests
import json



home_bp = Blueprint(
    'home_bp', __name__,
    template_folder='templates',
    static_folder='static')



@home_bp.route('/', endpoint='home', methods=['GET'])
def home():
    msg = 'hellow'
    return render_template('index.html', msg=msg)


@home_bp.route('/say_hi', endpoint='say_hi', methods=['GET'])
def say_hi():
    response = requests.get('http://192.168.86.23:8000/say_hi')
    print(response.text)
    return redirect(url_for('home_bp.home'))
