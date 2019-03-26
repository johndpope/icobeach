import  json
from peewee import *
import uuid
import datetime
import random,string
import time, base64, string
from hashlib import md5
import os,binascii

class UUIDUtil(TextField):

    def get_id(self):
        return self.tid_maker()

    def tid_maker(self):
        return '{0:%Y%m%d%H%M%S%f}'.format(datetime.datetime.now())

    def get_uuid(self):
        return str(uuid.uuid1())

    def get_sessionid(self):
        return uuid.uuid4().hex

    def get_session(self):
        return "session-"+uuid.uuid4().hex


if __name__ == '__main__':
    # print(UUIDUtil().tid_maker())
    # name = "test_name"
    # namespace = uuid.NAMESPACE_URL
    # print(UUIDUtil().get_uuid() ) # 带参的方法参见Python Doc
    # print(uuid.uuid3(namespace, name))
    # print(uuid.uuid4())
    # print(uuid.uuid5(namespace, name))
    print(UUIDUtil().get_session())












