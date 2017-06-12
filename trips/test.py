from login import isLoginSuccess, setUserAccount, changePassword

#BUILDING
# conn.execute('''CREATE TABLE User
#        (user_id INT PRIMARY KEY  NOT NULL, 
#        password       CHAR(50)    NOT NULL,
#        user_name      CHAR(50)    NOT NULL
#        );''')
# conn.execute('''CREATE TABLE Sound
#        (sound_id     INT PRIMARY KEY  NOT NULL, 
#        user_id       INT NOT NULL,
#        longitude     FLOAT    NOT NULL,
#        latitude      FLOAT    NOT NULL,
#        privacy       BOOLEAN  NOT NULL,
#        description   TEXT ,
#        tag           TEXT
#        );''')

#DELETE
#conn.execute('DELETE Voice')	

#ADD
# conn.execute("INSERT INTO User (user_id, password, user_name) VALUES (1, 'mactavish', 'Allen')");
# conn.commit()
# conn.execute("INSERT INTO Sound (sound_id, user_id, longitude, latitude, privacy, description, tag) VALUES (1, 1, 0, 0, 0, '', '')");
# conn.commit()

#PRINT
# cursor = conn.execute("SELECT * from User")
# for row in cursor:
#    print ("user_id = ", row[0])
#    print ("password = ", row[1])
#    print ("user_name = ", row[2], '\n')

#get_sound_by_GPS
# result = get_sound_by_GPS(0, 0)
# print(result.sound_id)

setUserAccount('d', 'e', 'f')

