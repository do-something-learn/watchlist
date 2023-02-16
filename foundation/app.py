from flask import Flask,render_template
from flask import url_for
from loguru import logger
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
import pymysql 
import logging 
name='Mr Du'
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]
#操作数据库
USERNAME='root'
PASSWORD='3237never'
HOSTNAME='localhost:3306'
PORT='3306'
DATABASE='flasktest'
app=Flask(__name__)

#在cofig中配置数据库信息
#SQLALchemy会读取config中的内容并创建一个数据库对象
app.config['SQLALCHEMY_DATABASE_URI']=f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}/{DATABASE}'
db=SQLAlchemy(app)
print(db)

@app.route('/test')
def test():
    value=0
    with db.engine.connect() as conn:
        result=conn.execute(sqlalchemy.text("select 1"))
        value=result.fetchone()
    return str(value)
@app.route('/')
def index():
    return render_template('index.html', name=name , movies=movies)
