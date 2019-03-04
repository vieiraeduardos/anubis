
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
