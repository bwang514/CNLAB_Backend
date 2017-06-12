import sqlite3

def setUserVoice(user_id, photo):
    conn = sqlite3.connect('Database.db3')


    FH = open("voice.dat", "r") 
    line = FH.readline()  
    voice_id = int(line) + 1
    FH.close()
    FH = open("voice.dat", "w")
    FH.write(str(voice_id))
    FH.close()

    # Create a file object in "write" mode  
    FH = open("./Voice/" + str(voice_id), "w")  
    # Write all the lines at once to the file handle  
    FH.write(Phototo)    
    FH.close()      


    conn.execute("UPDATE User SET voice_id = '" + str(voice_id) + "' WHERE user_id = '" + user_id + "'")
    conn.commit()
    conn.close()

    return True
