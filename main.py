from tkinter import *
from tkinter import ttk
import os
import sqlite3

# os.system('python pages/start.py')


# Подключаемся к базе данных SQLite
conn = sqlite3.connect('pages/Dog_Diseases.db')
c = conn.cursor()

# Получаем структуру базы данных
# c.execute("""delete from normal_values where id_signs ='5'""")
# print(c.fetchall())
c.execute("""SELECT * FROM characteristics_values""")
print(c.fetchall())

conn.commit()
# Закрываем соединение
conn.close()