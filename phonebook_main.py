import mysql.connector
from login_page import Login
from tkinter import *


def sign_up():
    root = Tk()

    welcome = Label(root, text='Sign Up', font='bold')
    welcome.grid(row=0, column=1)

    name = Label(root, text='Enter Name')
    name.grid(row=1, column=0)
    enter_name = Entry(root)
    enter_name.grid(row=1, column=1)

    phone_num = Label(root, text='Phone Number')
    phone_num.grid(row=2, column=0)
    enter_phone = Entry(root)
    enter_phone.grid(row=2, column=1)

    password = Label(root, text='Password')
    password.grid(row=3, column=0)
    enter_pass = Entry(root, show = '*')
    enter_pass.grid(row=3, column=1)

    def onclick():
        get_name = enter_name.get()
        get_pass = enter_pass.get()
        get_phone = enter_phone.get()
        save_num(get_name, get_pass, get_phone)
        call_login()

    signup_btn = Button(root, text='Sign Up', padx=7, pady=4, command=onclick)
    signup_btn.grid(row=4, column=1)


    def call_login():
        root.destroy()  # added destroy to remove the window after log in has been opened
        go_login = Login()
        go_login.log_in()

    log_btn = Button(root, text='Login?', padx=0, pady=0, command=call_login)
    log_btn.grid(row=4, column=0)

    root.mainloop()


def save_num(name, password, get_phone):

    uid = 1

    conn = mysql.connector.connect(host='localhost', port='3306', user='root', password='', database='contacts')
    cursor = conn.cursor()

    showquery = "select * from users"
    cursor.execute(showquery)
    records = cursor.fetchall()

    for i in records:
        if i[0] == uid:
            uid += 1

    selectquery = "Insert into users(UID, username, password, Phone_Number) values(%s,%s,%s,%s)"
    values = (uid, name, password, get_phone)
    cursor.execute(selectquery, values)
    conn.commit()

sign_up()
