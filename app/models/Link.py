from app.models.DatabaseFactory import DatabaseFactory


class Link():
    def __init__(self, judge="", paper=""):
        self.judge = judge
        self.paper = paper
        self.connection = DatabaseFactory().getConnection()

    def create(self):
        try:
          with self.connection.cursor() as cursor:
            sql = "INSERT INTO links(judge, paper) VALUES (%s, %s)"
            cursor.execute(sql, (self.judge, self.paper))
            self.connection.commit()

            return True
        except Exception as e:
            print(e)
            return False
        finally:
          self.connection.close()
