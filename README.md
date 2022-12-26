# kpmg-data

## MySQL
```
        create table POC_MR_CFG_CURVE
        (
            V_CURVE_ID       VARCHAR(40),
            V_CURVE_NAME     VARCHAR(100),
            V_RISK_TYPE      VARCHAR(20),
            V_CURRENCY_CODE  VARCHAR(7)  not null,
            V_DAYCOUNT_BASIS VARCHAR(20),
            V_SETTLE_BASIS   VARCHAR(20),
            PRIMARY KEY (`V_CURVE_ID`)
        )



        create table POC_MR_CFG_FACTOR
        (
            V_CURVE_ID   VARCHAR(40) not null,
            V_CURVE_TERM VARCHAR(10),
            V_MKID       VARCHAR(40),
            PRIMARY KEY (`V_MKID`)
        )
```