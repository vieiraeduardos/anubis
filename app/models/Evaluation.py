
from app.models.DatabaseFactory import DatabaseFactory

class Evaluation():
    def __init__(self, presenter="", paper="", judge="", originality=0, consistency=0, clarity=0, relevance=0, quality=0, domain=0):
        self.paper = paper
        self.judge = judge
        self.originality = float(originality)
        self.consistency = float(consistency)
        self.clarity = float(clarity)
        self.relevance = float(relevance)
        self.quality = float(quality)
        self.domain = float(domain)
        self.presenter = str(presenter)
        self.connection = DatabaseFactory().getConnection()

    def create(self):
        try:
          with self.connection.cursor() as cursor:
            sql = "INSERT INTO evaluation(presenter, paper, judge, originality, consistency, clarity, relevance, quality, domain) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (self.presenter, self.paper, self.judge, self.originality, self.consistency, self.clarity, self.relevance, self.quality, self.domain))
            self.connection.commit()

            return True
        except Exception as e:
            print(e)
            return False
        finally:
          self.connection.close()

    def getNoteByPaper(self, paper):
        try:
          with self.connection.cursor() as cursor:
            sql = "SELECT avg(originality) + avg(consistency) + avg(clarity) + avg(relevance) + avg(quality) + avg(domain) as total FROM anubisdb.evaluation where evaluation.paper=%s"
            cursor.execute(sql, (paper))
            result = cursor.fetchone()

            return result
        except Exception as e:
            print(e)
            return 0
        finally:
          self.connection.close()

    def getOriginalityByPaper(self, paper):
        try:
          with self.connection.cursor() as cursor:
            sql = "SELECT avg(originality) as originality FROM anubisdb.evaluation where evaluation.paper=%s"
            cursor.execute(sql, (paper))
            result = cursor.fetchone()

            return result
        except Exception as e:
            print(e)
            return 0
        finally:
          self.connection.close()

    def getRelevanceByPaper(self, paper):
        try:
          with self.connection.cursor() as cursor:
            sql = "SELECT avg(relevance) as relevance FROM anubisdb.evaluation where evaluation.paper=%s"
            cursor.execute(sql, (paper))
            result = cursor.fetchone()

            return result
        except Exception as e:
            print(e)
            return 0
        finally:
          self.connection.close()

    def getEvaluation(self, judge, paper):
        try:
          with self.connection.cursor() as cursor:
            sql = "SELECT * FROM evaluation WHERE judge=%s AND paper=%s"
            cursor.execute(sql, (judge, paper))
            result = cursor.fetchone()

            return result
        except Exception as e:
            print(e)
            return None
        finally:
          self.connection.close()



    def update(self):
        try:
          with self.connection.cursor() as cursor:
            sql = "UPDATE evaluation SET presenter=%s, originality=%s, consistency=%s, clarity=%s, relevance=%s, quality=%s, domain=%s WHERE judge=%s AND paper=%s"
            cursor.execute(sql, (self.presenter, self.originality, self.consistency, self.clarity, self.relevance, self.quality, self.domain, self.judge, self.paper))
            self.connection.commit()

            return True
        except Exception as e:
            print(e)
            return False
        finally:
          self.connection.close()
