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


def add_diseases():
    text = combo_box2.get()
    selected_value = combo_box.get()
    cur.execute(f"""
             INSERT INTO normal_values(id_signs, value_nv) VALUES ((select id_signs from signs 
                                    where name_signs = '{selected_value}'),'{text}')""")
    conn.commit()
    print_list(listbox)


def delete_diseases():
    selected_indices = listbox.curselection()  # Получаем индексы выбранных элементов
    if selected_indices:  # Проверяем, есть ли выбранные элементы
        for index in selected_indices:
            selected_item = listbox.get(index)
            selected_value = combo_box.get()
            cur.execute(f"""
                         delete from normal_values where value_nv ='{selected_item}' and
                                        id_signs = (select id_signs from signs where name_signs='{selected_value}')""")
            conn.commit()
            print_list(listbox)
            print("Выделенный элемент:", selected_item)
    else:
        print("No")


def print_list(listbox):
    listbox.delete(0, tk.END)
    selected_value = combo_box.get()
    list_value = pandas.read_sql(f""" SELECT value_nv FROM normal_values inner join signs using(id_signs) 
                                        where name_signs='{selected_value}' """, conn)

    # Добавляем элементы из списка в Listbox
    for i in range(len(list_value)):
        listbox.insert(tk.END, list_value.loc[i, 'value_nv'])


def update_combobox2(event):
    # Очищаем список значений второго Combobox
    combo_box2['values'] = []
    # В зависимости от выбранного значения в combobox1, обновляем значения в combobox2
    list_name_value = []
    selected_value = combo_box.get()
    my_list_value = pandas.read_sql(f""" SELECT value_pv FROM possible_values inner join signs using(id_signs) 
                                            where name_signs='{selected_value}' """, conn)
    for i in range(len(my_list_value)):
        list_name_value.append(my_list_value.loc[i, 'value_pv'])

    combo_box2['values'] = list_name_value

    combo_box2.set("Выберите значение")


def update_list_value(event):
    listbox.delete(0, tk.END)
    selected_value = combo_box.get()
    list_value = pandas.read_sql(f""" SELECT value_nv FROM normal_values inner join signs using(id_signs) 
                                            where name_signs='{selected_value}' """, conn)

    # Добавляем элементы из списка в Listbox
    for i in range(len(list_value)):
        listbox.insert(tk.END, list_value.loc[i, 'value_nv'])

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

#надпись
label_text = "Выберите признак:"
label = tk.Label(root, text=label_text, justify="left")
label.grid(row=0, column=1, padx=10, pady=10, sticky="sw")

list_name = []
my_list = pandas.read_sql(f""" SELECT name_signs FROM signs""", conn)
for i in range(len(my_list)):
    list_name.append(my_list.loc[i, 'name_signs'])

combo_box = ttk.Combobox(root, values=list_name)
# Устанавливаем текст по умолчанию
combo_box.set("Выберите значение")

#надпись
label_text = "Выберите значение:"
label = tk.Label(root, text=label_text, justify="left")
label.grid(row=1, column=1, padx=10, pady=10, sticky="sw")

combo_box2 = ttk.Combobox(root)
combo_box2.grid(row=1, column=1, padx=10, pady=10, sticky="e")

# Привязываем обработчик событий к выбору в списке
combo_box.bind("<<ComboboxSelected>>", update_combobox2)
combo_box2.bind("<<ComboboxSelected>>", update_list_value)
combo_box.grid(row=0, column=1, padx=10, pady=10, sticky="e")

# Добавление кнопки под надписью справа
bottom_button = tk.Button(root, text="Добавить", width=10, command=add_diseases)
bottom_button.grid(row=1, column=2, padx=10, pady=10, columnspan=2, sticky="n")

#фрайм для вывода
get_frame = Frame(root)
get_frame.grid(row=2, column=1, rowspan=6, padx=10, pady=10, sticky=tk.W)

#надпись2
label_text = "Список нормальных значений:"
label = tk.Label(get_frame, text=label_text, justify="left")
label.pack(pady=0, padx=0, anchor="nw", expand=True)

# Создаем виджет Listbox с возможностью выбора одного элемента
listbox = tk.Listbox(get_frame, selectmode=tk.SINGLE, width=50)
listbox.pack(pady=0, padx=0, side="left", fill="both", expand=True)

y_scrollbar = tk.Scrollbar(get_frame, orient=tk.VERTICAL, command=listbox.yview)
y_scrollbar.pack(side='right', fill='y', padx=(0, 0), pady=0)
listbox.config(yscrollcommand=y_scrollbar.set)
# Добавляем элементы из списка в Listbox
print_list(listbox)

# Добавление кнопки под надписью справа
bottom_button = tk.Button(root, text="Удалить", command=delete_diseases)
bottom_button.grid(row=2, column=3, padx=10, pady=10, sticky="s")

frm.grid_rowconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
# root.rowconfigure(0, weight=1)

root.mainloop()