from app.models.DatabaseFactory import DatabaseFactory

class Admin():
    def __init__(self):
        self.connection = DatabaseFactory().getConnection()

    def getAdminByEmail(self, email):
        try:
          with self.connection.cursor() as cursor:
            sql = "SELECT  *  FROM  admins  WHERE  email=%s"
            cursor.execute(sql, (email))
            result = cursor.fetchone()

            return result
        except Exception as e:
            print(e)
            return None
        finally:
          self.connection.close()
