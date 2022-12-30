from kafka import KafkaProducer
from helper.kafka_gen import KafkaDataGen
from time import sleep
import json
import sys
from setting import BootStrap_Servers


class GenKafka(KafkaDataGen):
    def get_create_table_sql(self) -> str:
        return """
        create table POC_MR_CFG_CURVE
        (
            V_CURVE_ID       VARCHAR2(40) not null constraint "POC_VAL_CFG_CURVE_pk" primary key,
            V_CURVE_NAME     VARCHAR2(100),
            V_RISK_TYPE      VARCHAR2(20),
            V_CURRENCY_CODE  VARCHAR2(7)  not null,
            V_DAYCOUNT_BASIS VARCHAR2(20),
            V_SETTLE_BASIS   VARCHAR2(20)
        )
        """

    def get_client(self) -> KafkaProducer:
        producer = KafkaProducer(bootstrap_servers=BootStrap_Servers)
        return producer


data1 = GenKafka()
data1.run("demo")
