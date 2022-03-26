import mysql.connector
from tkinter import *
from tkinter import filedialog
import search_contact


class pic_upload:

    def __init__(self, UID):
        self.UID = UID

    def profile_picture(self):

        root = Tk()
        root.withdraw()

        file_path = filedialog.askopenfilename()

        print(file_path)

        canvas = Canvas(root, width=300, height=300)
        canvas.pack()

        conn = mysql.connector.connect(host='localhost', port='3306', user='root', password='', database='contacts')
        cursor = conn.cursor()

        all_query = "select UID, profilepic from numbers where UID=" + str(self.UID) + ";"
        cursor.execute(all_query)
        records = cursor.fetchall()


        showquery ="update numbers set profilepic='" + file_path + "'where UID =" + str(self.UID) + ";"
        cursor.execute(showquery)
        conn.commit()

        call_search_contacts = search_contact.Contacts(self.UID)
        call_search_contacts.contact_search()
        root.destroy()
