from flask import Flask,render_template,request,redirect
import pymysql
x=Flask(__name__)

@x.route('/')

def index():
      try:
            db=pymysql.connect(host="localhost",user="root",password="",database="todo1")
            cu=db.cursor()
            sql="select * from employee"
            cu.execute(sql)
            data=cu.fetchall()
            return render_template('dashboard.html',d=data)
      except Exception as e:
            print("Error:",e)
@x.route('/form')
def create():
    return render_template('form.html')

@x.route('/store',methods=['POST'])
def store():
      i=request.form['id']
      en=request.form['ename']
      ind=request.form['iname']
      dt=request.form['detail']
      G=request.form['Gender']
      a=request.form['age']
      sal=request.form['salary']
      d=request.form['doj']
      try:
            db=pymysql.connect(host="localhost",user="root",password="",database="todo1")
            cu=db.cursor()
            sql="insert into employee (id, ename,iname,detail,Gender,age,salary,doj) values({},'{}','{}','{}','{}',{},{},{})".format(i,en,ind,dt,G,a,sal,d)
            cu.execute(sql)
            db.commit()
            return redirect('/')
      except Exception as e:
            print("Error:",e)
@x.route('/delete/<rid>')
def delete(rid):
      try:
            db=pymysql.connect(host="localhost",user="root",password="",database="todo1")
            cu=db.cursor()
            sql="delete from employee where id='{}'".format(rid)
            cu.execute(sql)
            db.commit()
            return redirect('/')
      except Exception as e:
             print("Error:",e)               
@x.route('/edit/<rid>')
def edit(rid):
      try:
            db=pymysql.connect(host="localhost",user="root",password="",database="todo1")
            cu=db.cursor()
            sql="select * from employee where id='{}'".format(rid)
            cu.execute(sql)
            data=cu.fetchone()
            return render_template('editform.html',d=data)
      except Exception as e:
            print("Error:",e)
@x.route('/update/<rid>',methods=['POST'])

def update(rid):
      i=request.form['id']
      en=request.form['ename']
      ind=request.form['iname']
      dt=request.form['detail']
      G=request.form['Gender']
      a=request.form['age']
      sal=request.form['salary']
      d=request.form['doj']
      try:
            db=pymysql.connect(host="localhost",user="root",password="",database="todo1")
            cu=db.cursor()   
            sql="update employee SET id={}, ename='{}',iname='{}',detail='{}',Gender='{}',age={},salary={},doj='{}' where id={}".format(i,en,ind,dt,G,a,sal,d,rid)
            cu.execute(sql)
            db.commit()
            return redirect('/')
      except Exception as e:
            print("Error:",e)
        
#x.run(debug=True)
x.run()

