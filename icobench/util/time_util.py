import  time,random
import datetime
class TimeUtil():

    def sleep_random_extime(self):
        time.sleep(random.randint(5, 10))

    def sleep_random_10extime(self):
        time.sleep(random.randint(15, 25))

    def repl_rayndom_extime(self):
        time.sleep(random.randint(5, 30))


    def sleep_get_phone_extime(self):
        time.sleep(5)

    def sleep_random(self,start,end):
        time.sleep(random.randint(start, end))

    def sleep_extime(self,sec):
        time.sleep(sec)

    def str_to_time(self,str_time):
        d_time = datetime.datetime.strptime(str_time, "%Y-%m-%d %H:%M:%S")
        return d_time

    def time_to_enstr(self,e_time):
        str_time = e_time.strftime("%c")
        return str_time

    # 将字符串time转为datetime
    def str_time_todatatime(self,str_time):
        print('str_time:' + str(str_time))
        date_time = datetime.datetime.strptime(str_time, "%Y-%m-%d")
        return date_time

#     英式时间转中式时间
    def en_datetime_to_zh_datetime(self,time):
        print('time_format' + str(time))
        time_format = datetime.datetime.strptime(time, '%d %b %Y')
        return time_format


