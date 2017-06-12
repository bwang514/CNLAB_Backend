def getUserInformation(user_id):
    conn = sqlite3.connect('Database.db3')
    conn.execute("DELETE FROM User")
    conn.close()
    
    return