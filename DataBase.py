import pymysql
from tkinter import messagebox
class MySql:
    def __init__(self,host,user,passward):
        self.host = host
        self.user = user
        self.passward = passward
        try:
            self.con = pymysql.connect(host=self.host, user=self.user, password=self.passward)
            self.mycursor = self.con.cursor()
            self.connect = True
        except:
            messagebox.showerror('Notification','Data in incorrect!')
            self.connect=False

        if(self.connect):
            try:
                query = "create database studentmanagementsystem1;"
                self.mycursor.execute(query)
                query = "use studentmanagementsystem1;"
                self.mycursor.execute(query)
                query = "create table studentdata1(id int not null unique auto_increment,name varchar(100) not null,Father_name varchar(100) not null,DOB varchar(100) not null,mobile varchar(13) unique,Email_id varchar(320) unique,gender varchar(10), category varchar(10), Time varchar(20),date varchar(20));"
                self.mycursor.execute(query)
                messagebox.showinfo('Notification', 'Database created, Now you are connected to the Database')
            except:
                query = f"use studentmanagementsystem1;"
                self.mycursor.execute(query)
                messagebox.showinfo('Notification', 'Now you are connected to the Database')

    def insert(self,name,fname,dob,mobile,email,gender,category,date,time):
        try:
            query = "insert into studentdata1(name,Father_name,DOB,mobile,Email_id,gender,category,Time,date) values(%s,%s,%s,%s,%s,%s,%s,%s,%s);"
            self.mycursor.execute(query,(name,fname,dob,mobile,email,gender,category,time,date))
            self.con.commit()
            messagebox.showinfo('Notification','Registerion Successful!')
        except:
            messagebox.showerror('Notification','This Email/mobile no already exists!')

    def showdata(self):
        query = "select * from studentdata1;"
        self.mycursor.execute(query)
        datas = self.mycursor.fetchall()
        return datas

    def search(self,searchby,val):
        try:
            query = ""
            if searchby=='Id':
                query = "select * from studentdata1 where id = %s;"
            elif searchby=='name':
                query = "select * from studentdata1 where name = %s;"
            elif searchby=='Father_name':
                query = "select * from studentdata1 where Father_name = %s;"
            elif searchby=='Email_id':
                query = "select * from studentdata1 where Email_id = %s;"
            elif searchby=='mobile':
                query = "select * from studentdata1 where mobile = %s;"
            elif searchby=='DOB':
                query = "select * from studentdata1 where DOB = %s;"
            elif searchby=='gender':
                query = "select * from studentdata1 where gender = %s;"
            elif searchby=='category':
                query = "select * from studentdata1 where category = %s;"
            elif searchby=='date':
                query = "select * from studentdata1 where date = %s;"

            self.mycursor.execute(query, (val))
            datas = self.mycursor.fetchall()
            return datas
        except:
            messagebox.showerror('Notification','Data not found')
            return None


    def update(self,id,name,fname,mobile,email,gender,dob,category):
        try:
            query = "update studentdata1 set name=%s,Father_name=%s,mobile=%s,Email_id=%s,gender=%s,DOB=%s,category=%s where id=%s;"
            self.mycursor.execute(query,(name,fname,mobile,email,gender,dob,category,id))
            self.con.commit()
            messagebox.showinfo('Notification','Updated successfully!')
            return True
        except:
            messagebox.showerror('Notification','Id not found!')
            return False

    def delete(self,id):
        try:
            query = 'delete from studentdata1 where id = %s;'
            self.mycursor.execute(query,(id))
            self.con.commit()
            messagebox.showinfo('Notification','Deleted successfully!')
        except:
            pass
