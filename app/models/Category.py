from app.models.DatabaseFactory import DatabaseFactory

class Category():
    def __init__(self):
        self.connection = DatabaseFactory().getConnection()
        
    def getAllCategories(self):
        try:
          with self.connection.cursor() as cursor:
            sql = "SELECT  *  FROM  categories"
            cursor.execute(sql)
            result = cursor.fetchall()

            return result
        except Exception as e:
            print(e)
            return None
        finally:
          self.connection.close()
