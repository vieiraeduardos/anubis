from app.models.DatabaseFactory import DatabaseFactory

class Subcategory():
    def __init__(self):
        self.connection = DatabaseFactory().getConnection()

    def getAllSubcategories(self):
        try:
          with self.connection.cursor() as cursor:
            sql = "SELECT  *  FROM  subcategories"
            cursor.execute(sql)
            result = cursor.fetchall()

            return result
        except Exception as e:
            print(e)
            return None
        finally:
          self.connection.close()
