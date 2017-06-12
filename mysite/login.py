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

def setUserAccount(user_id, password, user_name):
    conn = sqlite3.connect('Database.db3')

    conn.execute("INSERT INTO User (user_id, password, user_name) VALUES ( '" + user_id + "', '" + password + "', '" + user_name + "')");
    conn.commit()   
    conn.close()

    return True

def changePassword(user_id, new_password):
    conn = sqlite3.connect('Database.db3')

    conn.execute("UPDATE User SET password = '" + new_password + "' WHERE user_id = '" + user_id + "'")
    conn.commit()
    conn.close()

    return True