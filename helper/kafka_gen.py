import sys
from random import random
from pysqler import Insert
from .data_gen import DataGen
from .dbclient import DBClient
from kafka import KafkaProducer
import time
import json


class KafkaDataGen(DataGen):
    def __init__(self):
        pass

    def get_client(self) -> KafkaProducer:
        raise ValueError("need implemented in subclass")

    def send_success(self, *args, **kwargs):
        """异步发送成功回调函数"""
        print('save success')
        return

    def send_error(self, *args, **kwargs):
        """异步发送错误回调函数"""
        print('error => {0}'.format(*args))
        return

    def run(self, topic_name: str, row_count=-1, time_interval_seconds=0.1):

        producer = self.get_client()

        gen = super().run(10, time_interval_seconds)
        columns = next(gen)

        print("running...")
        leng = len(columns)
        for vv in gen:
            item = dict()
            for i in range(0,  leng):
                item[columns[i]] = vv[i]

            doc = json.dumps(item).encode('utf-8')
            producer.send(topic_name, doc).add_callback(
                self.send_success).add_errback(self.send_error)
            producer.flush()
