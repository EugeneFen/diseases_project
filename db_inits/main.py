import sqlite3
import pandas as pd
from fill_db import *
from init_db import *

connect = sqlite3.connect("../pages/Dog_Diseases.db")
cursor = connect.cursor()
# * init db
cursor.executescript(init_db)
#
# # * fill db
# cursor.executescript(fill_script)

# cursor.execute("""
# select * FROM dog
# """)
# print(cursor.fetchall())
#
# cursor.execute("""
# update dog_owner
# set surname = "Отсутствует"
# where surname is Null
# """)
# cursor.execute("""
# select * FROM dog_owner
# """)
# print(cursor.fetchall())

connect.commit()
connect.close()