from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import font
import pandas
import sqlite3
import os

root = Tk() #создание окна
root.geometry("700x390")
conn = sqlite3.connect("Dog_Diseases.db")
cur = conn.cursor()


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

def add_diseases():
    text = entry.get()
    cur.execute(f"""
             INSERT INTO diseases(name_diseases) VALUES ('{text}')""")
    conn.commit()
    entry.delete(0, "end")
    print_list(listbox)

def delete_diseases():
    selected_indices = listbox.curselection()  # Получаем индексы выбранных элементов
    if selected_indices:  # Проверяем, есть ли выбранные элементы
        for index in selected_indices:
            selected_item = listbox.get(index)
            cur.execute(f"""
                         delete from diseases where name_diseases ='{selected_item}'""")
            conn.commit()
            print_list(listbox)
            print("Выделенный элемент:", selected_item)
    else:
        print("No")

def print_list(listbox):
    listbox.delete(0, tk.END)
    my_list = pandas.read_sql(""" SELECT name_diseases FROM diseases """, conn)

    # Добавляем элементы из списка в Listbox
    for i in range(len(my_list)):
        listbox.insert(tk.END, my_list.loc[i, 'name_diseases'])

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


#фрайм для ввода
isert_frame = Frame(root)
isert_frame.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

#надпись
label_text = "Название заболевания:"
label = tk.Label(isert_frame, text=label_text, justify="left")
label.pack(pady=0, padx=0, anchor="nw", expand=True)

#поле для ввода названий
entry = tk.Entry(isert_frame, width=60)
entry.pack(pady=0, padx=0, side="bottom", expand=True, anchor="sw")

# Добавление кнопки под надписью справа
bottom_button = tk.Button(root, text="Добавить", width=10, command=add_diseases)
bottom_button.grid(row=0, column=2, padx=10, pady=10, columnspan=2, sticky="s")

get_frame = Frame(root)
get_frame.grid(row=1, column=1, rowspan=7, padx=10, pady=10, sticky=tk.W)

# надпись2
label_text = "Список заболеваний:"
label = tk.Label(get_frame, text=label_text, justify="left")
label.pack(pady=0, padx=0, anchor="nw", expand=True)

# Создаем виджет Listbox с возможностью выбора одного элемента
listbox = tk.Listbox(get_frame, selectmode=tk.SINGLE, width=50)
listbox.pack(pady=0, padx=0, side="left", fill="both", expand=True)

y_scrollbar = tk.Scrollbar(get_frame, orient=tk.VERTICAL, command=listbox.yview)
y_scrollbar.pack(side='right', fill='y', padx=(0, 0), pady=0)
listbox.config(yscrollcommand=y_scrollbar.set)

print_list(listbox)

# Добавление кнопки под надписью справа
bottom_button = tk.Button(root, text="Удалить", command=delete_diseases)
bottom_button.grid(row=1, column=3, padx=10, pady=10, sticky="s")

frm.grid_rowconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
# root.rowconfigure(0, weight=1)

root.mainloop()