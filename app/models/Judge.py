from app.models.DatabaseFactory import DatabaseFactory

class Judge():
    def __init__(self, name="", cpf="", email="", password="", createdAt="", modifiedAt=""):
        self.name = name
        self.cpf = cpf
        self.email = email
        self.password = password
        self.createdAt = createdAt
        self.modifiedAt = modifiedAt
        self.connection = DatabaseFactory().getConnection()

    def create(self):
        try:
          with self.connection.cursor() as cursor:
            sql = "INSERT INTO judges(cpf, name, email, password, createdAt, modifiedAt) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (self.cpf, self.name, self.email, self.password, self.createdAt, self.modifiedAt))
            self.connection.commit()

            return True
        except Exception as e:
            print(e)
            return False
        finally:
          self.connection.close()
