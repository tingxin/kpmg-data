from helper.data_gen import DataGen
from helper.mysql import MySQL
from helper.dbclient import DBClient
import setting


class GenPOC_MR_CFG_CURVE(DataGen):
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

    def get_dbclient(self) -> DBClient:
        mysql = MySQL(setting.HOST, setting.PORT,
                      setting.USER, setting.PWD, setting.DB)
        return mysql


class GenPOC_MR_CFG_FACTOR(DataGen):
    def get_create_table_sql(self) -> str:
        return """
        create table POC_MR_CFG_FACTOR
        (
            V_CURVE_ID   VARCHAR2(40) not null,
            V_CURVE_TERM VARCHAR2(10),
            V_MKID       VARCHAR2(40) not null constraint "POC_MR_CFG_FACTOR_pk" primary key
        )
        """

    def get_dbclient(self) -> DBClient:
        mysql = MySQL(setting.HOST, setting.PORT,
                      setting.USER, setting.PWD, setting.DB)
        return mysql


# data1 = GenPOC_MR_CFG_CURVE()
# data1.run("POC_MR_CFG_CURVE")

data2 = GenPOC_MR_CFG_FACTOR()
data2.run("POC_MR_CFG_FACTOR")
