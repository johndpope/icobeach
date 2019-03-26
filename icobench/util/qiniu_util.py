import time,random
import datetime
from qiniu import BucketManager
from qiniu import Auth, put_file, etag
import qiniu.config
import requests
import os
import json
from .uuid_util import UUIDUtil

class QiniuUtil():
    # 需要填写你的 Access Key 和 Secret Key
    access_key = 'YhJdLFOJyWUjBKf19RQS0k_f1L7FwSLRIbsLTIbC'
    secret_key = 'aO2XI4UPpk3FjBMBk6NB_y_mVMgKYkqz9rcaXzVz'
    # def __init__(self):
    #     self.client = Auth(self.access_key, self.secret_key)

    def upload_url(self,s_url,f_name):
        bucket_name = 'knightcomment'
        q = Auth(self.access_key, self.secret_key)

        bucket = BucketManager(q)
        ret,info = bucket.fetch(s_url, bucket_name, f_name)
        print("response:", ret)
        print("response:", info)
        # ret_dic = json.loads(info)
        status = False
        if info.status_code == 200:
            status = True
        return status

    def upload_url2file(self,s_url,f_name):
        if not os.path.exists('./temp'):
            os.makedirs('./temp')
        img = requests.get(s_url)
        # print(img.content)
        localfile = "./temp/"+f_name
        fp = open(localfile, 'ab')
        fp.write(img.content)
        fp.flush()
        fp.close()
        # 构建鉴权对象
        q = Auth(self.access_key, self.secret_key)
        # 要上传的空间
        bucket_name = 'knightcomment'
        # 生成上传 Token，可以指定过期时间等
        token = q.upload_token(bucket_name, f_name, 3600)
        # 要上传文件的本地路径
        ret,info = put_file(token, f_name, localfile)
        print("response:", ret)
        print("response:", info)
        # ret_dic = json.loads(info)
        status = False
        if info.status_code == 200:
            status = True

        os.remove(localfile)
        return status


# if __name__ == '__main__':
#     s_url="https://pbs.twimg.com/profile_images/1050633669583364097/HovTdr6k_400x400.jpg"
#     # s_url="http://ruidian.mobi/img/xinwenpic.jpg"
#     # s_url="https%3a%2f%2fpbs.twimg.com%2fprofile_images%2f1050633669583364097%2fHovTdr6k_400x400.jpg"
#     # f_name = "HovTdr6k_400x400.jpg"
#     f_name = UUIDUtil().get_uuid()
#     print(f_name)
#     print(QiniuUtil().upload_url2file(s_url,f_name))
#     #"img.lvluozhibao.com/xinwenpic.jpg"
#     # r = requests.get(s_url)
#     # print(r)
#     # print(r.text)
#     # localfile = "./temp/" + f_name
#     # os.remove(localfile)


