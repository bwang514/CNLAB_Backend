import sqlite3

def isLoginSuccess(user_id, password):
    conn = sqlite3.connect('Database.db3')

    cursor = conn.cursor()
    cursor.execute("select * from User where user_id = '" + user_id + "' and password = '" + password + "'")
    result = cursor.fetchall()
    cursor.close()
    conn.close()

    if len(result) == 0:
    	return False
    else :
    	return True	

    