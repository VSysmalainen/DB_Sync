import os


db_params_lis_nsb = {
    "user": os.getenv('LIS_NSB_POSTGRES_USER', default='user'),
    "password": os.getenv('LIS_NSB_POSTGRES_PASSWORD', default='password'),
    "host":  os.getenv('LIS_NSB_POSTGRES_HOST', default='host'),
    "port": os.getenv('LIS_NSB_POSTGRES_PORT', default=5432),
    "database": os.getenv('LIS_NSB_POSTGRES_DB', default='db'),

}

db_params_mcc = {
    "user": os.getenv('MCC_POSTGRES_USER', default='user'),
    "password": os.getenv('MCC_POSTGRES_PASSWORD', default='password'),
    "host":  os.getenv('MCC_POSTGRES_HOST', default='host'),
    "port": os.getenv('MCC_POSTGRES_PORT', default=5432),
    "database": os.getenv('MCC_POSTGRES_DB', default='db'),

}

db_params_dp = {
    "user": os.getenv('DP_POSTGRES_USER', default='user'),
    "password": os.getenv('DP_POSTGRES_PASSWORD', default='password'),
    "host":  os.getenv('DP_POSTGRES_HOST', default='host'),
    "port": os.getenv('DP_POSTGRES_PORT', default=5432),
    "database": os.getenv('DP_POSTGRES_DB', default='db'),

}
