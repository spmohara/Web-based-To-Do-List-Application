import sqlite3
from bottle import route, template, request, error, default_app, run

@route('/todo')
def show_tasks():

    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT id, task, date FROM todo WHERE status LIKE '1' ORDER BY date ASC;")
    result = c.fetchall()
    c.close()

    output = template('show_tasks', rows=result)
    return output

@route('/todo/new', method='GET')
def new_task():

    if request.GET.get('save','').strip():

        new_task = request.GET.get('task', '').strip()
        task_date = request.GET.get('date', '').strip()
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()

        c.execute("INSERT INTO todo (task,date,status) VALUES (?,?,?)", (new_task,task_date,1))
        new_id = c.lastrowid

        conn.commit()
        c.close()

        return '<p><center><font size="6">Task successfully added</font></center></p><meta http-equiv="refresh" content="2;URL=/todo">'
        
    else:
        return template('new_task.tpl')

@route('/todo/edit/:no', method='GET')
def edit_task(no):

    if request.GET.get('save','').strip():
        edit_task = request.GET.get('task','').strip()
        edit_date = request.GET.get('date','').strip()
        status = request.GET.get('status','').strip()

        if status == 'In Progress':
            status = 1
            
            conn = sqlite3.connect('todo.db')
            c = conn.cursor()
            c.execute("UPDATE todo SET task = ?, date = ?, status = ? WHERE id LIKE ?", (edit_task,edit_date,status,no))
            conn.commit() 

	    return '<p><center><font size="6">Task successfully updated</font></center></p><meta http-equiv="refresh" content="2;URL=/todo">'

        else:
            status = 0

            conn = sqlite3.connect('todo.db')
            c = conn.cursor()
            c.execute("DELETE from todo WHERE id LIKE ?", (str(no),))
            conn.commit()

	    return '<p><center><font size="6">Task successfully completed</font></center></p><meta http-equiv="refresh" content="2;URL=/todo">'	

    else:
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("SELECT task, date FROM todo WHERE id = ?", (str(no),))
        cur_data = c.fetchone()

        return template('edit_task', old = cur_data, no = no)

@error(403)
def mistake403(code):
    return '<p><center><font size="6">Incorrect URL</font></center></p><meta http-equiv="refresh" content="2;URL=/todo">'

@error(404)
def mistake404(code):
    return '<p><center><font size="6">Page does not exist</font></center></p><meta http-equiv="refresh" content="2;URL=/todo">'
    
run()
