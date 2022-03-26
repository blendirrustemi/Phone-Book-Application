from tkinter import *
from register_contact import *
import mysql.connector
from PIL import ImageTk, Image


class Contacts:
    def __init__(self, UID):
        self.UID = UID
        self.j = 0


    def contact_search(self):

        root = Tk()

        welcome_msg = Label(root, text='Search your Contacts', font='BOLD')
        welcome_msg.grid(row=0, column=1)

        blnk = Label(root, text=' ')
        blnk.grid(row=1, column=0)

        c_name = Label(root, text='Enter a name')
        c_name.grid(row=2, column=0)
        search_contact = Entry(root)
        search_contact.grid(row=2, column=1)

        list_numbers = []

        def myclick_search():

            conn = mysql.connector.connect(host='localhost', port='3306', user='root', password='', database='contacts')
            cursor=conn.cursor()
            selectquery = 'select name, numbers.Phone_Number, numbers.profilepic from users, numbers where users.UID = numbers.UID and users.UID =' + str(self.UID)  #where users.UID = numbers.UID and users.UID = 1;'  #"select * from users"
            cursor.execute(selectquery)
            records = cursor.fetchall()

            get_cname = search_contact.get()

            for i in records:

                if get_cname.lower() == (i[0]).lower():

                    name_in_list = i[0] + ' ' + i[1]

                    list_numbers.append(name_in_list + '\n')
                    print(name_in_list)

                    blank = Label(root, text = ' ')
                    blank.grid(row=5, column=0)

                    text = Label(root, text=(list_numbers[self.j]), font='BOLD')
                    text.grid(row=6, column=1)
                    self.j += 1

                    try:
                        image = Image.open(i[2])
                        res_image = image.resize((100, 100), Image.ANTIALIAS)
                        new_img = ImageTk.PhotoImage(res_image)

                        label = Label(root, image = new_img)
                        label.image = new_img
                        label.grid(row=6, column=0)
                    except:
                        pass


                    def done_func():
                        text.destroy()
                        try:
                            label.destroy()
                        except:
                            pass

                    done_btn = Button(root, text='Done', padx=1, pady=1, command=done_func)
                    done_btn.grid(row=7, column=2)


        src_btn = Button(root, text='Search', padx=7, pady=4, command=myclick_search)
        src_btn.grid(row=4, column=1)


        def myclick_register():
            root.destroy()
            register = Register(self.UID)
            register.reg_contact()

        rg_button = Button(root, text='Register a new number?', padx=2, pady=1, command=myclick_register)
        rg_button.grid(row=4, column=0)

        root.mainloop()
