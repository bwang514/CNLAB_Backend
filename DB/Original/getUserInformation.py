import sqlite3

def getUserInformation(user_id):
    conn = sqlite3.connect('Database.db3')
    cursor = conn.cursor()
    cursor.execute("select * from User where user_id = " + user_id)
    a = cursor.fetchall()
    cursor.close()
    conn.close()
    name = a[0][2]
    photo_id = a[0][3]
    voice_id = a[0][4]

    FH = open( './Photo/' + str(photo_id), "r") 
    photo = FH.read()  
    FH.close()

    FH = open( './Voice/' + str(voice_id), "r") 
    voice = FH.read()  
    FH.close()
    
    print(name, photo, voice)

    return name, photo, voice
