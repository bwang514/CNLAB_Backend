import sqlite3

def setUserPhoto(user_id, photo):
    conn = sqlite3.connect('Database.db3')


    FH = open("photo.dat", "r") 
    line = FH.readline()  
    photo_id = int(line) + 1
    FH.close()
    FH = open("photo.dat", "w")
    FH.write(str(photo_id))
    FH.close()

    # Create a file object in "write" mode  
    FH = open("./Photo/" + str(photo_id), "w")  
    # Write all the lines at once to the file handle  
    FH.write(photo)    
    FH.close()      


    conn.execute("UPDATE User SET photo_id = '" + str(photo_id) + "' WHERE user_id = '" + user_id + "'")
    conn.commit()
    conn.close()

    return True
