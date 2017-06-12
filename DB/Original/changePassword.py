import sqlite3

def changePassword(user_id, new_password):
    conn = sqlite3.connect('Database.db3')

    conn.execute("UPDATE User SET password = '" + new_password + "' WHERE user_id = '" + user_id + "'")
    conn.commit()
    conn.close()

    return True
