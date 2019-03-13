
from app.models.DatabaseFactory import DatabaseFactory

class Evaluation():
    def __init__(self, paper="", judge="", originality=0, consistency=0, clarity=0, relevance=0, quality=0, domain=0):
        self.paper = paper
        self.judge = judge
        self.originality = originality
        self.consistency = consistency
        self.clarity = clarity
        self.relevance = relevance
        self.quality = quality
        self.domain = domain
        self.connection = DatabaseFactory().getConnection()

    def create(self):
        try:
          with self.connection.cursor() as cursor:
            sql = "INSERT INTO evaluation(paper, judge, originality, consistency, clarity, relevance, quality, domain) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (self.paper, self.judge, self.originality, self.consistency, self.clarity, self.relevance, self.quality, self.domain))
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
            sql = "UPDATE evaluation SET originality=%s AND consistency=%s AND clarity=%s AND relevance=%s AND quality=%s AND domain=%s WHERE judge=%s AND paper=%s"
            cursor.execute(sql, (self.originality, self.consistency, self.clarity, self.relevance, self.quality, self.domain, self.judge, self.paper))
            self.connection.commit()

            return True
        except Exception as e:
            print(e)
            return False
        finally:
          self.connection.close()
