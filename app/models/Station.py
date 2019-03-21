from app.models.DatabaseFactory import DatabaseFactory

class Station():
    def __init__(self, paper="", station="", time=""):
        self.paper = paper
        self.station = station
        self.time = time
        self.connection = DatabaseFactory().getConnection()

    def update(self):
        try:
          with self.connection.cursor() as cursor:
            sql = "UPDATE papers SET station=%s, time=%s WHERE code=%s"
            cursor.execute(sql, (self.station, self.time, self.paper))
            self.connection.commit()

            return True
        except Exception as e:
            print(e)
            return False
        finally:
          self.connection.close()
