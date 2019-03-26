import  json
import time,random,string

class GAUtil():

    def get_random_ga(self):

        #_ga=GA1.2.816831884.1539823218; _gid=GA1.2.1037120345.1546486176
        #_ga=GA1.2.816831884.1539823218; _gid=GA1.2.1737332155.1545897835


        _ga = "GA1.2.8"+str(self.get_random_number(8))+"."+str(int(time.time())-(random.randint(1, 6)*30*24*3600)-random.randint(1, 3600))
        _gid = "GA1.2.1"+str(self.get_random_number(9))+"."+str(int(time.time()))



        return "_ga="+_ga+"; "+"_gid="+_gid

    def get_random_number(self,num):
        return ''.join(random.sample(string.digits, num))
if __name__ == '__main__':
    print(GAUtil().get_random_ga())
    pass









