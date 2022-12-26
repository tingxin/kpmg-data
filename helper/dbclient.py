
class DBClient:
    def __init__(self, host: str, port: int, user: str, pwd: str, db: str):
        self.host = host
        self.port = port
        self.user = user
        self.pwd = pwd
        self.db = db

    def get_conn(self):
        raise ValueError("need implemented in subclass")

    def fetch_one(self, sql: str, conn=None):
        raise ValueError("need implemented in subclass")

    def fetch(self, sql: str, conn=None):
        raise ValueError("need implemented in subclass")

    def exec(self, sql: str, conn=None):
        raise ValueError("need implemented in subclass")
