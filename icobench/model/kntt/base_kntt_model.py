from peewee import *
import datetime
from playhouse import pool

"""
database config
"""
qishi_db = MySQLDatabase('qishidb', user='qishi', password='EKX1xL6r', charset='utf8',
                         host='182.92.235.154', port=3306)

"""
BaseModel
"""
class BaseKnttModel(Model):

    class Meta:
        database = qishi_db
        print("database", database)