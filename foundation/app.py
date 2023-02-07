from flask import Flask,render_template
from flask import url_for
from loguru import logger
import logging
app=Flask(__name__)
name='Mr Du'
movies=[{'title':'test1','year':1990},
{'title':'test2','year':1980},
{'title':'test3','year':1970}]
@app.route('/test')
def test():
    return 'test'
@app.route('/')
def index():
    return render_template('index.html', name=name , movies=movies)
