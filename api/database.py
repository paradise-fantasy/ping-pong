
import pymysql.cursors



class DB:
    config = {
        'user': 'pingpongtestuser',
        'password': 'paradise2017',
        'host': '129.241.200.204',
        'database': 'test',
        'cursorclass': 'pymysql.cursors.DictCursor'
    }


    def __init__(self):
        try:
            self.connection = pymysql.connect(**config)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

    def createPlayer(self, name, cardid, profile_picture):
        try:
            connection = self.connection
            with cnx.cursor() as cursor:
                sql = "INSERT INTO `player` (`name`, `cardid`, `profile_picture`) VALUES (%s, %s, %s)"
                cursor.execute(sql, (name, cardid, profile_picture))

            connection.commit()

        #finally:
        #    connection.close()


    def getPlayerFromPlayerId(self, playerid):
        try:
            connection = self.connection
            with connection.cursor() as cursor:
                sql = "SELECT * FROM `player` WHERE `id`=%s"
                cursor.execute(sql, (playerid,))

                result = cursor.fetchone()
                print result
        #finally:
        #    connection.close()

    def getPlayerFromCardId(self, cardid):
        try:
            connection = self.connection
            with connection.cursor() as cursor:
                sql = "SELECT * FROM `player` WHERE `id`=%s"
                cursor.execute(sql, (playerid,))

                result = cursor.fetchone()
                print result
        #finally:
        #    connection.close()

    def close(self):
        self.connection.close()
