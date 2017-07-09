#coding:utf-8

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
bootstrap=Bootstrap(app) #没有这行，用不了bootstrap--初始化Bootstrap扩展
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Love@mysql4ever@localhost/Shouldbuy'

db = SQLAlchemy(app) # 暂时数据库不启用
login_manager = LoginManager() #创建登录管理模块

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/product')
@app.route('/product/<productId>')
def product(productId):
	return render_template('product.html',productId=productId)

#路由至登录界面
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


#处理查找逻辑
@app.route('/search')
def search():
	return render_template('product.html')

#404页面
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'),404

#500页面
@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'),500

@app.route('/about')
def about():
	return render_template('about.html')

#定义数据库表模型
class User(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	username = db.Column(db.String(80),unique=True)
	email = db.Column(db.String(120),unique=True)

	def __init__(self, username,email):
		self.username = username
		self.email = email
		
	def __repr__(self):
		return '<User %r>' % self.username

if __name__ == "__main__":
	app.run()