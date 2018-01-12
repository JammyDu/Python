# coding = utf-8
import configparser
import os

class TestReadConfigFile(object):

    @property
    def get_value(self):
        root_dir = os.path.dirname(os.path.abspath('.'))
        print(root_dir+"***88888*888***")

        config = configparser.ConfigParser() #python中有一个类ConfigParser支持读ini文件
        #file_path = os.path.dirname(os.path.dirname('.')) + '\\config\\config.ini'
        print("*8888**获取当前路径")
        file_path = os.getcwd()
        print(os.path.abspath(os.path.dirname(file_path)))

        print("*88*8获取上级目录")
        #print(os.path.abspath(os.path.dirname(os.path.dirname(file_path))))
       # print(os.path.abspath(os.path.dirname(os.getcwd())))
        print(os.path.abspath(os.path.join(os.getcwd(),".."))+'\config\config.ini')
        file_path = os.path.abspath(os.path.join(os.getcwd(),".."))+'\config\config.ini'

        print("*88888获取上上级目录")
        print(os.path.abspath(os.path.join(os.getcwd(), "../..")))


        config.read(file_path)
        print(file_path+".........")

        #config.add_section("browserType")
        browser = config.get("browserType","browserName")
        url = config.get("testServer","URL")

        return (browser,url)
trcf = TestReadConfigFile()
print(trcf.get_value)





