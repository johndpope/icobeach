import  json
from peewee import *
import uuid
import datetime
import random,string

class StrUtil(TextField):
    def db_value(self, value):
        return json.dumps(value,ensure_ascii=False)

    def python_value(self, value):
        if value is not None:
            return json.loads(value)

    def array_to_str(self,array):
        return '&'.join(array)

    def str_to_array(self,str):
        return str.split('&')

    def get_id(self):
        return self.tid_maker()

    def tid_maker(self):
        return '{0:%Y%m%d%H%M%S%f}'.format(datetime.datetime.now())

    def get_repetition_num(self,s1, s2):
        num = 0

        len_s1 = len(s1)
        list_s1 = []
        for j in range(len_s1):
            sub_s1 = s1[j:]
            for i in range(len(sub_s1)):
                two_s1 = sub_s1[0:i + 1]
                list_s1.append(two_s1)
        for i in list_s1:
            # if s2.startswith(i) and len(i) > num:
            if i in s2 and len(i) > num:
                num = len(i)
        return num

    def get_random_digits(self,num):
        return ''.join(random.sample(string.digits, num))

    def get_random_letters(self,num):
        return ''.join(random.sample(string.ascii_lowercase, num))

    def get_random_number(self,num):
        return ''.join(random.sample(string.ascii_letters + string.digits, num))

    def get_nick_name(self,first_name,last_name) :
        nickname = ""
        if first_name is not None:
            len_first = len(first_name) - 1
            if len_first > 4:
                len_first = random.randint(3, 4)
            first_name = first_name[0:len_first]
            nickname +=first_name
        if last_name is not None:
            len_second = len(last_name) - 1
            if len_second > 4:
                len_second = random.randint(3, 4)
            last_name = last_name[0:len_second]
            nickname += last_name
        return nickname

    def get_invite_code(self, num):
        code='0123456789ABCDEF'
        return ''.join(random.sample(code, num))


if __name__ == '__main__':
    # print(StrUtil().tid_maker())
    # name = "test_name"
    # namespace = uuid.NAMESPACE_URL
    # print(uuid.uuid1() ) # 带参的方法参见Python Doc
    # # print(uuid.uuid3(namespace, name))
    # print(uuid.uuid4())
    # print(uuid.uuid5(namespace, name))
    # print(StrUtil().get_nick_name("dfjsdlfj","skfddddjf"))
    print(StrUtil().get_invite_code(6))











