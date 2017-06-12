import sqlite3

def setUserAccount(user_id, password, user_name):
    conn = sqlite3.connect('Database.db3')

    conn.execute("INSERT INTO User (user_id, password, user_name) VALUES ( '" + user_id + "', '" + password + "', '" + user_name + "')");
    conn.commit()   
    conn.close()

    return True