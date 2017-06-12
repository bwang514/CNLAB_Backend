import sqlite3

# def getUserInformation(user_id):
#     conn = sqlite3.connect('Database.db3')
#     cursor = conn.cursor()
#     cursor.execute("select * from User where user_id = " + user_id)
#     a = cursor.fetchall()
#     cursor.close()
#     conn.close()
#     name = a[0][2]
#     photo_id = a[0][3]
#     voice_id = a[0][4]

#     FH = open( './Photo/' + str(photo_id), "rb") 
#     photo = FH.read()  
#     FH.close()

#     FH = open( './Voice/' + str(voice_id), "rb") 
#     voice = FH.read()  
#     FH.close()

#     return name, photo, voice

def setUserVoice(user_id, voice):
    conn = sqlite3.connect('/nfs/home/haoen0514/djangogirls/mysite/DB/Database.db3')


    FH = open("/nfs/home/haoen0514/djangogirls/mysite/DB/Dat/voice.dat", "r") 
    line = FH.readline()  
    voice_id = int(line) + 1
    FH.close()
    FH = open("/nfs/home/haoen0514/djangogirls/mysite/DB/Dat/voice.dat", "w")
    FH.write(str(voice_id))
    FH.close()

    # Create a file object in "write" mode  
    FH = open("/nfs/home/haoen0514/djangogirls/mysite/DB/Voice/" + str(voice_id), "wb")  
    # Write all the lines at once to the file handle
    FH.write(voice)    
    FH.close()      


    conn.execute("UPDATE User SET voice_id = '" + str(voice_id) + "' WHERE user_id = '" + user_id + "'")
    conn.commit()
    conn.close()

    return True

def setUserPhoto(user_id, photo):
    conn = sqlite3.connect('/nfs/home/haoen0514/djangogirls/mysite/DB/Database.db3')


    FH = open("/nfs/home/haoen0514/djangogirls/mysite/DB/Dat/photo.dat", "r") 
    line = FH.readline()  
    photo_id = int(line) + 1
    FH.close()
    FH = open("/nfs/home/haoen0514/djangogirls/mysite/DB/Dat/photo.dat", "w")
    FH.write(str(photo_id))
    FH.close()

    # Create a file object in "write" mode  
    FH = open("/nfs/home/haoen0514/djangogirls/mysite/DB/Photo/" + str(photo_id), "wb")  
    # Write all the lines at once to the file handle  
    FH.write(photo)    
    FH.close()      


    conn.execute("UPDATE User SET photo_id = '" + str(photo_id) + "' WHERE user_id = '" + user_id + "'")
    conn.commit()
    conn.close()

    return True


# def getUserName(user_id):
#     conn = sqlite3.connect('/nfs/home/haoen0514/djangogirls/mysite/DB/Database.db3')
#     cursor = conn.cursor()
#     cursor.execute("select * from User where user_id = " + user_id)
#     a = cursor.fetchall()
#     cursor.close()
#     conn.close()
#     name = a[0][2]
#     return name

def getUserPhoto(user_id):
    conn = sqlite3.connect('/nfs/home/haoen0514/djangogirls/mysite/DB/Database.db3')
    cursor = conn.cursor()
    cursor.execute("select * from User where user_id = '" + user_id + "'")
    a = cursor.fetchall()
    cursor.close()
    conn.close()
    photo_id = a[0][2]
    return "/nfs/home/haoen0514/djangogirls/mysite/DB/Photo/" + str(photo_id)

def getUserVoice(user_id):
    conn = sqlite3.connect('/nfs/home/haoen0514/djangogirls/mysite/DB/Database.db3')
    cursor = conn.cursor()
    cursor.execute("select * from User where user_id = '" + user_id + "'")
    a = cursor.fetchall()
    cursor.close()
    conn.close()
    voice_id = a[0][3]
    return "/nfs/home/haoen0514/djangogirls/mysite/DB/Voice/" + str(voice_id)
