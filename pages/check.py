from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import font
import pandas
import sqlite3
import os

root = Tk()  # создание окна
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

def on_select(event):
    # Получаем индекс выбранной строки в Listbox1
    index = listbox.curselection()[0]
    # Получаем данные из вашего источника данных по этому индексу
    selected_data = list_diseases_full[index]
    # Очищаем Listbox2
    listbox2.delete(0, tk.END)
    # Добавляем данные в Listbox2
    for i in list_diseases_full:
        for key, value in i.items():
            for key2, value2 in value.items():
                listbox2.insert(tk.END, key2)
                if value2 == "ERROR":
                    listbox2.itemconfig(tk.END, fg="red")
                else:
                    listbox2.itemconfig(tk.END, fg="green")

frm = ttk.Frame(root, borderwidth=1, relief=SOLID, padding=5)
frm.grid(row=0, column=0, sticky="ns", rowspan=8)

font1 = font.Font(family="Arial", size=11, weight="normal", slant="roman")

tk.Label(frm, text="Разделы", font=font1).grid(column=0, row=0, sticky="ns", padx=10, pady=5)  # добавление надписи
tk.Button(frm, text='Заболевания', command=open_window_diseases).grid(column=0, row=1, sticky="ew", padx=5, pady=2)
tk.Button(frm, text='Признаки', command=open_window_signs).grid(column=0, row=2, sticky="ew", padx=5, pady=2)
tk.Button(frm, text='Возможные начения', command=open_window_possible_values).grid(column=0, row=3, sticky="ew", padx=5,
                                                                                   pady=2)
tk.Button(frm, text='Нормальные значения', command=open_window_normal_values).grid(column=0, row=4, sticky="ew", padx=5,
                                                                                   pady=2)
tk.Button(frm, text='Клиническая картина', command=open_window_clinical_picture).grid(column=0, row=5, sticky="ew",
                                                                                      padx=5, pady=2)
tk.Button(frm, text='Значения признаков для заболеваний', command=open_window_feature_values).grid(column=0, row=6,
                                                                                                   sticky="ew", padx=5,
                                                                                                   pady=2)
tk.Button(frm, text='Проверка полноты', command=open_window_check).grid(column=0, row=7, sticky="ew", padx=5, pady=2)

#####################################################

list_diseases_full = []
my_list = pandas.read_sql(f""" SELECT id_diseases, name_diseases FROM diseases""", conn)
for i in range(len(my_list)):
    my_list_signs = pandas.read_sql(f""" SELECT id_signs, name_signs FROM clinical_picture inner join signs using(id_signs)
                                                        where id_diseases = '{my_list.loc[i, 'id_diseases']}'""", conn)
    my_list_value_signs = pandas.read_sql(f""" SELECT id_signs, value_cv FROM characteristics_values 
                                                        where id_diseases = '{my_list.loc[i, 'id_diseases']}'""", conn)

    list_signs = []
    vocabulary_signs = {}
    for j in range(len(my_list_signs)):
        t = False
        for k in range(len(my_list_value_signs)):
            if my_list_signs.loc[j, 'id_signs'] == my_list_value_signs.loc[k, 'id_signs']:
                vocabulary_signs[my_list_signs.loc[j, 'name_signs']] = my_list_value_signs.loc[k, 'value_cv']
                t = True
        if not t:
            vocabulary_signs[my_list_signs.loc[j, 'name_signs']] = "ERROR"

    list_diseases_full.append({my_list.loc[i, 'name_diseases']: vocabulary_signs})

#######################################################

# фрайм для вывода первого списка слева
button_scroll_frame = Frame(root)
button_scroll_frame.grid(row=0, column=2, rowspan=8, padx=10, pady=10, sticky=tk.W)

# надпись
label_text = "Заболевания:"
label = tk.Label(button_scroll_frame, text=label_text, justify="left")
label.pack(pady=0, padx=0, side="top", fill="both", expand=True)

# Создаем виджет Listbox с возможностью выбора одного элемента
listbox = tk.Listbox(button_scroll_frame, selectmode=tk.SINGLE, width=30)
listbox.pack(pady=0, padx=0, side="right", fill="both", expand=True)

y_scrollbar = tk.Scrollbar(button_scroll_frame, orient=tk.VERTICAL, command=listbox.yview)
y_scrollbar.pack(side='left', fill='y', padx=(0, 0), pady=0)
listbox.config(yscrollcommand=y_scrollbar.set)
# Добавляем элементы из списка в Listbox
for i in list_diseases_full:
    for key, value in i.items():
        listbox.insert(tk.END, key)

listbox.bind("<<ListboxSelect>>", on_select)

# фрайм для вывода второго списка слева
button_scroll_frame2 = Frame(root)
button_scroll_frame2.grid(row=0, column=3, rowspan=8, padx=10, pady=10, sticky=tk.W)

# надпись
label_text = "Признаки:"
label = tk.Label(button_scroll_frame2, text=label_text, justify="left")
label.pack(pady=0, padx=0, side="top", expand=True)

# Создаем виджет Listbox с возможностью выбора одного элемента
listbox2 = tk.Listbox(button_scroll_frame2, selectmode=tk.SINGLE, width=30)
listbox2.pack(pady=0, padx=0, side="left", fill="both", expand=True)

y_scrollbar = tk.Scrollbar(button_scroll_frame2, orient=tk.VERTICAL, command=listbox2.yview)
y_scrollbar.pack(side='right', fill='y', padx=(0, 0), pady=0)
listbox2.config(yscrollcommand=y_scrollbar.set)

frm.grid_rowconfigure(0, weight=1)
root.columnconfigure(2, weight=0)
# root.rowconfigure(0, weight=1)

root.mainloop()
