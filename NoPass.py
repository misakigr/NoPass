#!/usr/bin/env python
"""Creates remote backups.

It let's remote machines stream it's data to your machine using the SSH connection.
There are plugins available that provide functionality.
"""

import hashlib

from tkinter import *

__author__ = "Igor V. Misak"
__copyright__ = "Copyright 2021, Debian SSH Backup"
__credits__ = ["Elena Kozlova", "Maxim Stravinsky"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Igor V. Misak"
__email__ = "misakigr@mail.ru"
__status__ = "Production"


salt = ''
def clicked():
    res = "{}".format(txt.get())
    lbl.configure(text=res)
    global salt
    salt = res
    print(salt)
    res1 = "{}".format(txt1.get())
    lbl1.configure(text=res1)
    global login
    login = res1
    print(login)
    window.destroy()


window = Tk()
window.title("NoPass")
window.geometry('300x50')
x = (window.winfo_screenwidth() - window.winfo_reqwidth()) / 2
y = (window.winfo_screenheight() - window.winfo_reqheight()) / 2
window.wm_geometry("+%d+%d" % (x, y))
lbl = Label(window, text="Введите соль:")
lbl.grid(column=0, row=0)
txt = Entry(window,width=15)
txt.focus()
txt.grid(column=1, row=0)
lbl1 = Label(window, text="Введите Лог:")
lbl1.grid(column=0, row=2)
txt1 = Entry(window,width=15)
txt1.focus()
txt1.grid(column=1, row=2)


btn = Button(window, text="Клик!", command=clicked)
btn.grid(column=2, row=0)

window.mainloop()


digits='1234567890'

leters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

leters_2='abcdefghijklmnopqrstuvwxyz'

symbols='!@#$%^&*()-+'

#salt = input("Enter salt: ")
#salt = a.encode()
print()
#print(salt)

p=''

salt =salt.encode()

login = login.encode()

key = hashlib.pbkdf2_hmac('sha256', login, salt, 100000, 16)

key = int(key.hex(),16)

key = str(key)

print (key)

n=0

p+=(leters_2[(int(key[0:1])):((int(key[0:1]))+1)])
p+=(leters_2[(int(key[1:2])):((int(key[1:2]))+1)])
p+=(leters[(int(key[2:3])):((int(key[2:3]))+1)])
p+= (digits[(int(key[3:4])):((int(key[3:4]))+1)])

p+=(leters[(int(key[4:5])+9):((int(key[4:5]))+10)])
p+= (digits[(int(key[5:6])):((int(key[5:6]))+1)])

p+=(leters_2[(int(key[6:7])+9):((int(key[6:7]))+10)])
p+=(symbols[(int(key[7:8])):((int(key[7:8]))+1)])
p+=(leters_2[(int(key[9:10])+16):((int(key[9:10]))+17)])

p+= (digits[(int(key[11:12])):((int(key[11:12]))+1)])
p+=(leters[(int(key[13:14])+16):((int(key[13:14]))+17)])
p+=(leters[(int(key[14:15])+16):((int(key[14:15]))+17)])
print()
print(p)

root = Tk()
root.title("NoPass")
root.geometry('250x50')
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.wm_geometry("+%d+%d" % (x, y))

lbl = Label(root, text = p)
lbl1 = Label(root, text ="Нажмите на бутон 'copy'-->")

def copy_to_clipboard():
    root.clipboard_clear()  # Очистить буфер обмена
    root.clipboard_append(lbl['text'])  # Добавить текст в буфер обмена


btn = Button(root, text='copy', command=copy_to_clipboard)

lbl.grid(row=1, column=0)
lbl1.grid(row=0, column=0)
btn.grid(row=0, column=1)


root.mainloop()