# Приложение «Приём заявок», версия 0.2.1 (готовая после исправлений)

from tkinter import *
from tkinter import ttk

LIMIT = 12000000
count = 0 


def accept():
    global count
    count = count + 1
    label_count["text"] = count
    label_date["text"] = "Накликай лям двести"
    if count >= LIMIT:
        label_count["text"] = "Красава, накликал: " + str(count)
        btn_accept["state"] = "disabled"



window = Tk()
window.title("Кликер")
window.geometry("300x420")

label_title = Label(text="Количество кликов:")
label_title.pack()

label_count = Label(text="0", fg="black")
label_count.pack()

label_date = Label(text="Накликал:")
label_date.pack()

btn_accept = ttk.Button()
btn_accept.pack(pady=5)
btn_accept["text"] = "Клик"
btn_accept["command"] = accept

btn_reset = ttk.Button()
btn_reset.pack(pady=5)
btn_reset["text"] = "Сбросить"


btn_accept["width"] = 20
btn_reset["width"] = 20

window.mainloop()
