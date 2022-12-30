# mysql
HOST = 'demo.c6lwjjfhbm6a.rds.cn-northwest-1.amazonaws.com.cn'
PORT = 3306
USER = 'admin'
PWD = 'Demo1234'
DB = 'kpmg_dev'  # 这个名称请保持和 script 各个初始化脚本中创建的db 名称一致

# kafka
BootStrap_Servers = [
    "b-1.demokafka.8ec31u.c4.kafka.cn-northwest-1.amazonaws.com.cn:9092",
    "b-3.demokafka.8ec31u.c4.kafka.cn-northwest-1.amazonaws.com.cn:9092",
    "b-2.demokafka.8ec31u.c4.kafka.cn-northwest-1.amazonaws.com.cn:9092"
]
