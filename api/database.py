import pymysql.cursors

class DB:

    def __init__(self):
        self.connection = pymysql.connect(host='127.0.0.1',
                                            user='testuser',
                                            password='testpass',
                                            db='test',
                                            charset='utf8mb4',
                                            cursorclass=pymysql.cursors.DictCursor)

    def createPlayer(self, name, cardid, surname="", profile_picture=""):
        try:
            connection = self.connection
            with connection.cursor() as cursor:
                sql = "INSERT INTO `player` (`name`, `cardid`, `profile_picture`) VALUES (%s, %s, %s)"
                cursor.execute(sql, (name, cardid, profile_picture))

            connection.commit()
        finally:
            return True;
    def getPlayerFromPlayerId(self, playerid):
        try:
            connection = self.connection
            with connection.cursor() as cursor:
                sql = "SELECT * FROM `player` WHERE `id`=%s"
                cursor.execute(sql, (playerid,))

                result = cursor.fetchone()
        finally:
            return result

    def getPlayerFromCardId(self, cardid):
        try:
            connection = self.connection
            with connection.cursor() as cursor:
                sql = "SELECT * FROM `player` WHERE `id`=%s"
                cursor.execute(sql, (playerid,))
                result = cursor.fetchone()

        finally:
            return result

    def close(self):
        self.connection.close()
