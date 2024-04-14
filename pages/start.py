from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import font
import os

root = Tk()  # создание окна
root.geometry("700x390")


# открытие страницы заболеваний
def open_window_diseases():
    root.destroy()
    os.system('python diseases.py')


# открытие страницы признаков
def open_window_signs():
    root.destroy()
    os.system('python signs.py')


# открытие страницы возможных значений признаков
def open_window_possible_values():
    root.destroy()
    os.system('python possible_values.py')


# открытие страницы нормальных значений признаков
def open_window_normal_values():
    root.destroy()
    os.system('python normal_values.py')


# открытие страницы клиническая картина
def open_window_clinical_picture():
    root.destroy()
    os.system('python clinical_picture.py')


# открытие страницы значения признаков заболевания
def open_window_feature_values():
    root.destroy()
    os.system('python feature_values.py')


# открытие страницы проверка
def open_window_check():
    root.destroy()
    os.system('python check.py')

frm = ttk.Frame(root, borderwidth=1, relief=SOLID, padding=5)
frm.grid(row=0, column=0, sticky="ns", rowspan=8)

font1 = font.Font(family= "Arial", size=11, weight="normal", slant="roman")

tk.Label(frm, text="Разделы", font=font1).grid(column=0, row=0,  sticky="ns", padx=10, pady=5) #добавление надписи
tk.Button(frm, text='Заболевания', command=open_window_diseases).grid(column=0, row=1,  sticky="ew", padx=5, pady=2)
tk.Button(frm, text='Признаки', command=open_window_signs).grid(column=0, row=2,  sticky="ew", padx=5, pady=2)
tk.Button(frm, text='Возможные начения', command=open_window_possible_values).grid(column=0, row=3, sticky="ew", padx=5, pady=2)
tk.Button(frm, text='Нормальные значения', command=open_window_normal_values).grid(column=0, row=4,  sticky="ew", padx=5, pady=2)
tk.Button(frm, text='Клиническая картина', command=open_window_clinical_picture).grid(column=0, row=5,  sticky="ew", padx=5, pady=2)
tk.Button(frm, text='Значения признаков для заболеваний', command=open_window_feature_values).grid(column=0, row=6,  sticky="ew", padx=5, pady=2)
tk.Button(frm, text='Проверка полноты', command=open_window_check).grid(column=0, row=7,  sticky="ew", padx=5, pady=2)

label_text = "Выберите нужный раздел"
label = tk.Label(root, text=label_text, justify="left")
label.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

# Добавление кнопки под надписью справа
# bottom_button = ttk.Button(root, text="Нижняя кнопка")
# bottom_button.grid(row=1, column=1, padx=10, pady=10, sticky="n")

# root.columnconfigure(1, weight=1)
# root.rowconfigure(0, weight=1)

root.mainloop()
