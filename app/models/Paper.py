from app.models.DatabaseFactory import DatabaseFactory

class Paper():
    def __init__(self, title="", abstract="", author="", category="", subcategory="", isExposed="", isPresented="", createdAt="", modifiedAt=""):
        self.title = title
        self.abstract = abstract
        self.author = author
        self.category = category
        self.subcategory = subcategory
        self.isExposed = isExposed
        self.isPresented = isPresented
        self.createdAt = createdAt
        self.modifiedAt = modifiedAt
        self.connection = DatabaseFactory().getConnection()

    def create(self):
        try:
          with self.connection.cursor() as cursor:
            sql = "INSERT INTO papers(event, title, abstract, author, category, subcategory, isExposed, isPresented, createdAt, modifiedAt) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (1, self.title, self.abstract, self.author, self.category, self.subcategory, self.isExposed, self.isPresented, self.createdAt, self.modifiedAt))
            self.connection.commit()

            return True
        except Exception as e:
            print(e)
            return False
        finally:
          self.connection.close()



    def getAllPapers(self):
        try:
          with self.connection.cursor() as cursor:
            sql = "SELECT  *  FROM  papers order by station, time"
            cursor.execute(sql)
            result = cursor.fetchall()

            return result
        except Exception as e:
            print(e)
            return None
        finally:
          self.connection.close()


    def getPaperByCode(self, code):
        try:
          with self.connection.cursor() as cursor:
            sql = "SELECT  *  FROM  papers WHERE code=%s"
            cursor.execute(sql, (code))
            result = cursor.fetchone()

            return result
        except Exception as e:
            print(e)
            return None
        finally:
          self.connection.close()


    def getAllPapersByJudge(self, judge):
        try:
          with self.connection.cursor() as cursor:
            sql = "SELECT papers.*, links.* FROM papers INNER JOIN links WHERE papers.code = links.paper AND links.judge = %s"
            cursor.execute(sql, (judge))
            result = cursor.fetchall()

            return result
        except Exception as e:
            print(e)
            return None
        finally:
          self.connection.close()
