import pymysql.cursors

class DB:

    def __init__(self):
        self.connection = pymysql.connect(host='127.0.0.1',
                                            user='testuser',
                                            password='testpass',
                                            db='test',
                                            charset='utf8mb4',
                                            cursorclass=pymysql.cursors.DictCursor)

    def createPlayer(self, name, card_id, surname="", profile_picture=""):
        try:
            connection = self.connection
            with connection.cursor() as cursor:
                sql = "INSERT INTO `player` (`name`, `cardid`, `profile_picture`, `surname`) VALUES (%s, %s, %s, %s)"
                new_player = cursor.execute(sql, (name, card_id, profile_picture, surname))
                player_id = cursor.lastrowid
            connection.commit()

            print player_id
            print new_player

            with connection.cursor() as cursor:
                sql = "SELECT `id` FROM `player` WHERE `cardid`=%s"
                cursor.execute(sql, (cardid,))
                return cursor.fetchone()
        except Exception as e:
            return "Error: " + str(e)

    def getPlayerFromPlayerId(self, player_id):
        try:
            connection = self.connection
            with connection.cursor() as cursor:
                sql = "SELECT * FROM `player` WHERE `id`=%s"
                cursor.execute(sql, (player_id,))

                result = cursor.fetchone()
        finally:
            return result

    def getPlayerFromCardId(self, card_id):
        try:
            connection = self.connection
            with connection.cursor() as cursor:
                sql = "SELECT * FROM `player` WHERE `cardid`=%s"
                cursor.execute(sql, (card_id,))
                result = cursor.fetchone()
        finally:
            return result

    def getAllPlayers(self):
        try:
            connection = self.connection
            with connection.cursor() as cursor:
                sql = "SELECT * FROM `player`"
                cursor.execute(sql)
                result = cursor.fetchall()
        finally:
            return result

    def updatePlayer(self, player_id, diff_rating, win):
        win = 1 if win else 0
        try:
            connection = self.connection
            with connection.cursor() as cursor:
                sql = "UPDATE `player` SET `games_played` = `games_played` + 1, `wins` = `wins` + %i, `rating` = `rating` + %i WHERE id=%i"
                affected_row = cursor.execute(sql, (win, diff_rating, player_id))
            return affected_row
        except Exception as e:
            return "Error: " + str(e)


    def createMatch(self, player_1, player_2, score_player_1, score_player_2, winner, scores):
        try:
            connection = self.connection
            with connection.cursor() as cursor:
                sql = "INSERT INTO `matches` (`player_1`, `player_2`, `score_player_1`, `score_player_2`, `winner`, `scores`) VALUES (%i, %i, %i, %i, %i, %s)"
                new_match = cursor.execute(sql, (player_1, player_2, score_player_1, score_player_2, winner, scores))
            connection.commit()

            return new_match
        except Exception as e:
            return "Error: " + str(e)

    def getMatch(self, match_id):
        try:
            connection = self.connection
            with connection.cursor() as cursor:
                sql = "SELECT * FROM `matches` WHERE `id`=%i"
                cursor.execute(sql, (match_id))
                result = cursor.fetchone()
        finally:
            return result

    def getAllMatches(self):
        try:
            connection = self.connection
            with connection.cursor() as cursor:
                sql = "SELECT * FROM `matches`"
                cursor.execute(sql)
                result = cursor.fetchall()
        finally:
            return result

    def close(self):
        self.connection.close()
