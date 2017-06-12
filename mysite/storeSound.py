from template import *

def storeSound(latitude, longitude, user_id, sound, title, description, date):
    conn = sqlite3.connect('Database.db3')

    FH = open("./Dat/sound.dat", "r") 
    line = FH.readline()  
    sound_id = int(line) + 1
    FH.close()
    FH = open("./Dat/sound.dat", "w")
    FH.write(str(sound_id))
    FH.close()

    # Create a file object in "write" mode  
    FH = open("./Sound/" + str(sound_id), "w")  
    # Write all the lines at once to the file handle  
    FH.write(sound)    
    FH.close()
    

    conn.execute("INSERT INTO Sound (sound_id, user_id, longitude, latitude, privacy, description, tag) VALUES (1, 1, 0, 0, 0, '', '')");
    conn.execute("INSERT INTO Sound (latitude, longitude, user_id, sound_id, title, description, date) VALUES (" + latitude + ", " + longitude + ", '" + user_id + "', '" + sound_id + "', '" + title + "', '" + description + "' ,'" + date + "')");
    conn.commit()  
    conn.close()

    return True