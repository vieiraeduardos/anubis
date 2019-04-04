from app.models.DatabaseFactory import DatabaseFactory


class Link():
    def __init__(self, judge="", paper=""):
        self.judge = judge
        self.paper = paper
        self.connection = DatabaseFactory().getConnection()

    def create(self):
        try:
          with self.connection.cursor() as cursor:
            sql = "INSERT INTO links(judge, paper, status) VALUES (%s, %s, %s)"
            cursor.execute(sql, (self.judge, self.paper, 0))
            self.connection.commit()

            return True
        except Exception as e:
            print(e)
            return False
        finally:
          self.connection.close()

    def remove(self, code):
        print("LINKS CODE")
        print(code)
        try:
          with self.connection.cursor() as cursor:
            sql = "delete from links where code=%s"
            cursor.execute(sql, (code))
            self.connection.commit()

            return True
        except Exception as e:
            print(e)
            return False
        finally:
          self.connection.close()


    def isComplete(self):
        try:
          with self.connection.cursor() as cursor:
            sql = "select count(paper) as number from links where paper=%s"
            cursor.execute(sql, (self.paper))
            result = cursor.fetchone()

            if result["number"] < 2:
                return True
            else:
                return False

        except Exception as e:
            print(e)
            return False

    def alreadyExists(self):
        try:
          with self.connection.cursor() as cursor:
            sql = "select * from links where paper=%s and judge=%s"
            cursor.execute(sql, (self.paper, self.judge))
            result = cursor.fetchall()

            if result:
                return False
            else:
                return True
        except Exception as e:
            print(e)
            return False

    def updateStatus(self, judge, paper):
        try:
          with self.connection.cursor() as cursor:
            sql = "UPDATE links SET status = %s WHERE judge=%s AND paper=%s"
            cursor.execute(sql, (1, judge, paper))
            self.connection.commit()

            return True
        except Exception as e:
            print(e)
            return False
        finally:
          self.connection.close()


    def getAllLinks(self):
        try:
          with self.connection.cursor() as cursor:
            sql = "select judges.name, links.* from judges inner join links where judges.cpf = links.judge"
            cursor.execute(sql)
            result = cursor.fetchall()

            return result

        except Exception as e:
            print(e)
            return None
        finally:
          self.connection.close()
