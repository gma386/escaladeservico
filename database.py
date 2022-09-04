import sqlite3

dbase = sqlite3.connect('employee_records.db')
c = dbase.cursor()
dbase.execute('''CREATE TABLE IF NOT EXISTS employee_records(
                ID INT PRIMATY KEY NOT NULL,
                NAME TEXT NOT NULL)''')
dbase.commit()
))