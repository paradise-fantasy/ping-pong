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
                sql = "INSERT INTO `player` (`name`, `cardid`, `profile_picture`, `surname`) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, (name, cardid, profile_picture, surname))
            connection.commit()

            with connection.cursor() as cursor:
                sql = "SELECT `id` FROM `player` WHERE `cardid`=%s"
                cursor.execute(sql, (cardid,))
                return cursor.fetchone()
        except Exception as e:
            return "Error: " + str(e)

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
                sql = "SELECT * FROM `player` WHERE `cardid`=%s"
                cursor.execute(sql, (cardid,))
                result = cursor.fetchone()
        finally:
            return result

    def getAllPlayers(self):
        try:
            connection = self.connection
            with connection.cursor() as cursor:
                sql ="SELECT * FROM `player`"
                cursor.execute(sql)
                result = cursor.fetchall()
        finally:
            return result

    def createMatch(player_1, player_2, score_player_1, score_player_2, winner, scores):
        try:
            connection = self.connection
            with connection.cursor() as cursor:
                sql = "INSERT INTO `matches` (`player_1`, `player_2`, `score_player_1`, `score_player_2`, `winner`, `scores`) VALUES (%i, %i, %i, %i, %i, %s)"
                cursor.execute(sql, (player_1, player_2, score_player_1, score_player_2, winner, scores))
            connection.commit()
        finally:
            return True

    def close(self):
        self.connection.close()
