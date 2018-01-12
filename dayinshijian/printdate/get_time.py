# coding = utf-8
import time

class GetTime(object):

    def get_system_time(self):
        print(time.time()) #获取的是1970到现在的间隔，单位是秒
        print(time.localtime())

        new_time = time.strftime('%Y-%m-%d %H:%M:%S')

        print(new_time)

gettime = GetTime()
gettime.get_system_time()