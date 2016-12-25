import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()
# cursor.execute('insert into user (id,name) values (\'6\',\'a tjmaxx\')')
cursor.execute(('select * from user order by name DESC'))
value = cursor.fetchall()
print([i[1] for i in value])
cursor.close()
conn.commit()
conn.close()
