import mysql.connector
from search_contact import *


class Login:
    def __init__(self):
        pass

    def log_in(self):
        root = Tk()

        welcome_login = Label(root, text='LOG IN!', font='BOLD')
        welcome_login.grid(row=0, column=1)


        u_name = Label(root, text='Enter Name')
        u_name.grid(row=1, column=0)
        username = Entry(root)
        username.grid(row=1, column=1)

        p_word = Label(root, text='Enter Password')
        p_word.grid(row=2, column=0)
        a_pass = Entry(root, show = '*')
        a_pass.grid(row=2, column=1)

        def whenclicked():
            get_username = username.get()
            get_password = a_pass.get()

            # if (list(filter(lambda x: x['Name'] == get_username.lower(), db["users"]))) and
            # (list(filter(lambda x: x['Password'] == get_password, db["users"]))): # this was used for dictionary/json file

            conn = mysql.connector.connect(host='localhost', port='3306', user='root', password='', database='contacts')
            cursor = conn.cursor()
            selectquery = "select UID, username, password from users where username = (%s) and password = (%s);"
            values = (get_username, get_password)
            cursor.execute(selectquery, values)
            records = cursor.fetchall()

            try:
                if (get_username.lower() == (records[0][1]).lower()) and (get_password == records[0][2]):
                    get_UID = records[0][0]
                    root.destroy()
                    person = Contacts(get_UID)
                    person.contact_search()
                else:
                    root.destroy()
                    repeat = Login()
                    repeat.log_in()
            except:
                wrong_user_pass = Label(root, text='Wrong Username or Password!', fg='RED')
                wrong_user_pass.grid(row=3, column=1)


        login_btn = Button(root, text='Log In', padx=7, pady=4, command=whenclicked)
        login_btn.grid(row=4, column=1)


        root.mainloop()
