from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import session

from flask import Flask
import pymysql
import sqlalchemy
from sqlalchemy import text
USERNAME='root'
PASSWORD='3237never'
HOSTNAME='localhost:3306'
PORT='3306'
DATABASE='goods'

app=Flask(__name__)

#在cofig中配置数据库信息
#SQLALchemy会读取config中的内容并创建一个数据库对象
app.config['SQLALCHEMY_DATABASE_URI']=f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}/{DATABASE}'
db=SQLAlchemy(app)
with app.app_context():
    with db.engine.connect() as conn:
        result = conn.execute(text("select 1"))
        print(result.fetchone())
#创建数据库模型   
class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(20))
class Movie(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(20))
    year=db.Column(db.String(4))

