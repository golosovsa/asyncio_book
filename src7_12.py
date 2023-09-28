"""
Приложение "Hello world" на TKiner
с. 207
"""
import time
import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.title = 'Hello world app'
window.geometry('200x100')


def say_hello():
    time.sleep(10)
    print('Привет')


hello_button = ttk.Button(window, text='Say hello', command=say_hello)
hello_button.pack()

window.mainloop()
