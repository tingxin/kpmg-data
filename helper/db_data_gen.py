import sys
from random import random
from pysqler import Insert
from .data_gen import DataGen
from .dbclient import DBClient
import time


class DBDataGen(DataGen):
    def __init__(self):
        pass

    def get_client(self) -> DBClient:
        raise ValueError("need implemented in subclass")

    def run(self, table_name: str, row_count=-1, time_interval_seconds=0.1):

        dbc = self.get_client()
        conn = dbc.get_conn()

        gen = super().run(row_count, time_interval_seconds)
        columns = next(gen)
        print(columns)
        print("running...")
        for vv in gen:
            cmd = Insert(table_name)
            cmd.add_columns(*columns)
            cmd.add_row(*vv)
            dbc.exec(str(cmd), conn)
