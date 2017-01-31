import mysql.connector



class DB:
    config = {
        'user': 'pingpongtestuser',
        'password': 'paradise2017',
        'host': '129.241.200.204',
        'database': 'test'
    }


    def __init__(self):
        try:
            self.cnx = mysql.connector.connect(**config)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

    def createPlayer(self, name, cardid, profile_picture):
        cnx = self.cnx
        cursor = cnx.cursor()

        add_player = ("INSERT INTO player "
                    "(name, cardid, profile_picture) "
                    "VALUES (%s, %s, %s)")
        data_player = (name, cardid, profile_picture)

        cursor.execute(add_player, data_player)

        cnx.commit()
        cursor.close()

    def getPlayerFromPlayerId(self, playerid):
        cnx = self.cnx
        cursor = cnx.cursor()

        query = ("SELECT * FROM player "
                "WHERE id=%i")
        cursor.execute(query, playerid)

        for data in cursor:
            print data

        cursor.close()

    def getPlayerFromCardId(self, cardid):
        cnx = self.cnx
        cursor = cnx.cursor()

        query = ("SELECT * FROM player "
                "WHERE id=%i")
        cursor.execute(query, cardid)

        for data in cursor:
            print data

        cursor.close()

    def close(self):
        self.cnx.close()
