from template import Sound
import sqlite3

def get_sound_by_GPS(longitude, latitude):
    result = Sound()
    conn = sqlite3.connect('Database.db3')
    cursor = conn.execute("SELECT * from Sound where privacy = 0 and longitude = " + str(longitude) + " and latitude = " + str(latitude))
    for row in cursor:
        result.sound_id = row[0];
        result.user_id = row[1];
        result.longitude = row[2];
        result.latitude = row[3];
        result.description = row[4];
        result.tag = row[5];

    return result