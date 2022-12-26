import pymysql.cursors
from .dbclient import DBClient


class MySQL(DBClient):
    def __init__(self, host: str, port: int, user: str, pwd: str, db: str):
        self.host = host
        self.port = port
        self.user = user
        self.pwd = pwd
        self.db = db

    def get_conn(self):
        connection = pymysql.connect(host=self.host,
                                     port=self.port,
                                     user=self.user,
                                     password=self.pwd,
                                     database=self.db,
                                     cursorclass=pymysql.cursors.DictCursor)
        return connection

    def get_binlog_info(self):
        conn = self.get_conn()

        with conn.cursor() as cursor:
            sql = 'show master status;'
            cursor.execute(sql)
            conn.commit()
            t = cursor.fetchone()
            return t['File'], t['Position']

    def fetch_one(self, sql: str, conn=None):
        if not conn:
            conn = self.get_conn()

        with conn.cursor() as cursor:
            cursor.execute(sql)
            conn.commit()
            t = cursor.fetchone()
            return t

    def fetch(self, sql: str, conn=None):
        if not conn:
            conn = self.get_conn()

        with conn.cursor() as cursor:
            cursor.execute(sql)
            conn.commit()
            t = cursor.fetch_all()
            return t

    def exec(self, sql: str, conn=None):
        if not conn:
            conn = self.get_conn()

        with conn.cursor() as cursor:
            cursor.execute(sql)
            conn.commit()
