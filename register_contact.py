from tkinter import *
# from tkinter import filedialog
from upload_picture import pic_upload
# from TEST2 import pic_upload

import search_contact
import mysql.connector

class Register:
    def __init__(self, UID):
        self.UID = UID
        # self.NID = 1

    def reg_contact(self):

        root = Tk()

        wlcm = Label(root, text='Register a new Contact', font='BOLD')
        wlcm.grid(row=0, column=1)

        blank_line = Label(root, text=' ')
        blank_line.grid(row=1, column=0)

        contact_name = Label(root, text='Enter Full Name')
        contact_name.grid(row=2, column=0)
        enter_contact = Entry(root)
        enter_contact.grid(row=2, column=1)

        contact_num = Label(root, text='Enter Phone Number')
        contact_num.grid(row=3, column=0)
        enter_num = Entry(root)
        enter_num.insert(0, '+383 ')
        enter_num.grid(row=3, column=1)


        def click_to_register():

            get_contact_name = enter_contact.get()
            get_contact_number = enter_num.get()

            conn = mysql.connector.connect(host='localhost', port='3306', user='root', password='', database='contacts')
            cursor = conn.cursor()

            # showquery = "select * from numbers"
            # cursor.execute(showquery)
            # records = cursor.fetchall()
            #
            # for i in records:
            #     if i[0] == self.NID:
            #         self.NID += 1

            selectquery = "Insert into numbers(UID, Name, Phone_Number) values(%s,%s,%s)"
            values = ( self.UID, get_contact_name, get_contact_number)
            cursor.execute(selectquery, values)
            conn.commit()


        reg_btn = Button(root, text='Register', padx=7, pady=4, command=click_to_register)
        reg_btn.grid(row=4, column=1)


        def upload_pic():
            root.destroy()
            profile_pic = pic_upload(self.UID)
            profile_pic.profile_picture()

        photobtn = Button(root, text='Upload Profile Picture', command = upload_pic)
        photobtn.grid(row=5, column=1)

        def back_search():
            root.destroy()
            call_contacts = search_contact.Contacts(self.UID)
            call_contacts.contact_search()

        back_button = Button(root, text='Search a Contact', padx=1, pady=1, command = back_search)
        back_button.grid(row=4, column = 0)


        root.mainloop()

# testi = Register(1)
# testi.reg_contact()

#new test