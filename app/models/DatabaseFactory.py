import pymysql.cursors

class DatabaseFactory():
  def __init__(self):
    self.connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='MySqLUn@Btms',
                                 #password='mysql',
                                 db='anubisdb',
                                 charset='utf8mb4',     cursorclass=pymysql.cursors.DictCursor)

  def getConnection(self):
    return self.connection
