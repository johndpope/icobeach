from peewee import *
import datetime
from playhouse import pool

"""
database config
"""
scrapy_db = MySQLDatabase('db_scrapy', user='scrapy', password='3RmLudCo', charset='utf8',
                         host='182.92.235.154', port=3306)

"""
BaseModel
"""
class BaseScrapyModel(Model):

    class Meta:
        database = scrapy_db
        print("database", database)