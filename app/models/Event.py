from app.models.DatabaseFactory import DatabaseFactory

class Event():
    def __init__(self, name="", description=""):
        self.name = name
        self.description = description
        self.connection = DatabaseFactory().getConnection()

    def getEventByCode(self, code):
        try:
          with self.connection.cursor() as cursor:
            sql = "SELECT  *  FROM  events  WHERE  code=%s"
            cursor.execute(sql, (code))
            result = cursor.fetchone()

            return result
        except Exception as e:
            print(e)
            return []
        finally:
          self.connection.close()

    def getAllEvents(self):
        try:
          with self.connection.cursor() as cursor:
            sql = "SELECT  *  FROM  events"
            cursor.execute(sql)
            result = cursor.fetchall()

            return result
        except Exception as e:
            print(e)
            return None
        finally:
          self.connection.close()
