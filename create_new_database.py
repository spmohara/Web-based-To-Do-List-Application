import sqlite3
con = sqlite3.connect('todo.db')
con.execute("CREATE TABLE todo (id INTEGER PRIMARY KEY, task char(100) NOT NULL, date char(5) NOT NULL, status bool NOT NULL)")
con.execute("INSERT INTO todo (task,date,status) VALUES ('Test 1','3/1',1)")
con.execute("INSERT INTO todo (task,date,status) VALUES ('Test 2','3/5',1)")
con.execute("INSERT INTO todo (task,date,status) VALUES ('Test 3','3/10',1)")
con.execute("INSERT INTO todo (task,date,status) VALUES ('Test 4','3/25',1)")
con.commit()
