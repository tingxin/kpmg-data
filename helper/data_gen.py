import sys
from faker import Faker
from pyspark.sql import SparkSession, DataFrame
from pyspark.context import SparkContext
from random import random
from pysqler import Insert
from .dbclient import DBClient
import time
# total_rows = 50000000
# unit_row = 10000

total_rows = 50
unit_row = 10

faker = Faker()


def facker_bool():
    return faker.random_int(0, 1) == 1


def facker_int():
    return faker.random_int(0, 100000)


def flt_trackingnumber():
    return str(faker.random_int(0, 10000000))


flt_columns_checker = {
    'trackingnumber': flt_trackingnumber
}


class DataGen:
    def __init__(self):
        pass

    def _get_meta(self, create_table_sql: str, spec_columns_checker: dict = None):
        columns_begin = create_table_sql.find('(')
        columns_end = create_table_sql.rfind(")")
        columns_str = create_table_sql[columns_begin+1:columns_end-1]

        columns_parts = columns_str.split(',\n')

        columns_parts = [item.strip() for item in columns_parts]

        columns = list()
        columns_value_funcs = list()
        for part in columns_parts:
            if part.startswith("PRIMARY"):
                continue
            print(part)
            kv = part.split(' ')
            k = kv[0]
            v = kv[1]
            if k.startswith('"'):
                k = k[1:len(k)-1]
            columns.append(k)

            v = v.lower()
            if spec_columns_checker and k in spec_columns_checker:
                f = spec_columns_checker[k]
            elif v.startswith("varchar"):
                f = faker.pystr
            elif v.startswith("timestamp"):
                f = faker.date_this_year
            elif v.startswith("numeric") or v.startswith("int"):
                f = facker_int
            elif v.startswith("bool"):
                f = facker_bool
            else:
                f = faker.pystr

            columns_value_funcs.append(f)

        return columns, columns_value_funcs

    def get_create_table_sql(self) -> str:
        raise ValueError("need implemented in subclass")

    def get_dbclient(self) -> DBClient:
        raise ValueError("need implemented in subclass")

    def run(self, table_name: str, row_count=-1, time_interval_seconds=0.1):
        sql = self.get_create_table_sql()
        columns, value_funcs = self._get_meta(sql)
        dbc = self.get_dbclient()
        conn = dbc.get_conn()
        if row_count > 0:
            index = 0
            while index < row_count:
                vv = [func() for func in value_funcs]
                cmd = Insert(table_name)
                cmd.add_columns(columns)
                cmd.add_row(vv)
                dbc.exec(str(cmd), conn)
                index += 1
                time.sleep(time_interval_seconds)
        else:
            while True:
                vv = [func() for func in value_funcs]
                cmd = Insert(table_name)
                cmd.add_columns(*columns)
                cmd.add_row(*vv)
                dbc.exec(str(cmd), conn)
                time.sleep(time_interval_seconds)
