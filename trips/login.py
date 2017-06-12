import sqlite3

def isLoginSuccess(user_id, password):
    conn = sqlite3.connect('/nfs/home/haoen0514/djangogirls/mysite/DB/Database.db3')

    cursor = conn.cursor()
    cursor.execute("select * from User where user_id = '" + user_id + "' and password = '" + password + "'")
    result = cursor.fetchall()
    cursor.close()
    conn.close()

    if len(result) == 0:
    	return False
    else :
    	return True	

def setUserAccount(user_id, password):
    conn = sqlite3.connect('/nfs/home/haoen0514/djangogirls/mysite/DB/Database.db3')

    conn.execute("INSERT INTO User (user_id, password) VALUES ( '" + user_id + "', '" + password + "')");
    conn.commit()   
    conn.close()

    return True

def changePassword(user_id, new_password):
    conn = sqlite3.connect('/nfs/home/haoen0514/djangogirls/mysite/DB/Database.db3')

    conn.execute("UPDATE User SET password = '" + new_password + "' WHERE user_id = '" + user_id + "'")
    conn.commit()
    conn.close()

    return True