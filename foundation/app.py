from flask import Flask,render_template
from flask import url_for

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
#创建数据库模型   
class User(db.Model):
    # __tablename__='user'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(20),nullable=False)
    password=db.Column(db.String(30),nullable=False)
class Movie(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    title=db.Column(db.String(20),nullable=False)
    year=db.Column(db.String(4),nullable=False)

@app.route('/database')
def database():
    db.create_all()#创建表
    return 'create successfully'

   
@app.route('/deldatabase')
def deldatabase():
    db.drop_all()
    return 'deldatabase successfully'
    
@app.route('/add')
def add():
    #插入数据
    user=User(name='李四',password='123')
    db.session.add(user)
    db.session.commit()
    return 'insert'
@app.route('/query/<string:name>')
def query(name):
    user=User()
    data=user.query.filter_by(name=name)#得到的是query对象
    for i in data:
        print({'id':i.id,'name':i.name,'password':i.password})
    return '查询成功'
@app.route('/delete/<string:name>')
def delete(name):
    user=User()
    data=user.query.filter_by(name=name).first()
    db.session.delete(data)
    db.session.commit()
    return 'delete'
@app.route('/update')
def update():
    user=User()
    data=user.query.filter_by(name='张三').first()
    data.name='李四'
    db.session.commit()
    return 'update'
@app.route('/test')
def test():
    with db.engine.connect() as conn:
        result=conn.execute(sqlalchemy.text("select 1"))
        value=result.fetchone()
    
    return str(value)
@app.route('/database')
def createdatabase():
    return 'database'
@app.route('/')
def index():
    return render_template('index.html', name=name , movies=movies)
