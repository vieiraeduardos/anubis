from app.models.DatabaseFactory import DatabaseFactory

class Author():
    def __init__(self, email="", name="", cpf="", isStudent=0, createdAt="", modifiedAt=""):
        self.name = name
        self.cpf = cpf
        self.email = email
        self.isStudent = isStudent
        self.createdAt = createdAt
        self.modifiedAt = modifiedAt
        self.connection = DatabaseFactory().getConnection()

    def create(self):
        try:
          with self.connection.cursor() as cursor:
            sql = "INSERT INTO authors(email, cpf, name, isStudent, createdAt, modifiedAt) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (self.email, self.cpf, self.name, self.isStudent, self.createdAt, self.modifiedAt))
            self.connection.commit()

            return True
        except Exception as e:
            print(e)
            return False
        finally:
          self.connection.close()

    def getAllAuthors(self):
        try:
          with self.connection.cursor() as cursor:
            sql = "SELECT  *  FROM  authors"
            cursor.execute(sql)
            result = cursor.fetchall()

            return result
        except Exception as e:
            print(e)
            return None
        finally:
          self.connection.close()
