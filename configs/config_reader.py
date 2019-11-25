# coding:utf-8
import configparser
#读取配置文件
class ReadConfig:
    def __init__(self):
        self.cf = configparser.ConfigParser()
        #读取路径、编码格式
        self.cf.read("../configs/config.ini", encoding='utf-8')
    def get_project(self, name):
        value = self.cf.get("PROJECT", name)
        return value

    def get_db(self, name):
        value = self.cf.get("DATABASE", name)
        return value

    def get_cases(self, name):
        value = self.cf.get("CASES", name)
        return value

    def get_report(self, name):
        value = self.cf.get("REPORT", name)
        return value

    def get_email(self, name):
        value = self.cf.get("EMAIL", name)
        return value

    def get_test_link(self, name):
        value = self.cf.get("TESTLINK", name)
        return value

    def get_file(self, name):
        value = self.cf.get("FILE", name)
        return value

    def get_log(self, name):
        value = self.cf.get("LOG", name)
        return value

    # 写入配置文件
    def write_config(self, host, app_version, case_module, version):
        pre = "https://"
        ending = ".lexue.com"
        host = pre + host + ending
        self.cf.set('PROJECT', 'host', host)
        self.cf.set('PROJECT', 'app_version', app_version)
        self.cf.set('PROJECT', 'module', case_module)
        self.cf.set('PROJECT', 'case_version', version)
        fp = open("../configs/config.ini", "w", encoding='utf-8')
        self.cf.write(fp)
        fp.close()

    def write_token(self, token):
        self.cf.set('PROJECT', 'token', token)
        fp = open("../configs/config.ini", "w", encoding='utf-8')
        self.cf.write(fp)
        fp.close()


if __name__ == "__main__":
    # 测试Service_url
    #test_url = http: // pycmstest.lexue.com
    # 灰度Service_url
    #tsl_url = http: // pycmstsl.lexue.com
    # 线上Service_url
    #dev_url = https: // pycms.lexue.com
    ReadConfig().write_config("pycmstest", "3.2.0", "0", "0")
    host = ReadConfig().get_project("host")
    app_version = ReadConfig().get_project("app_version")
    case_version = ReadConfig().get_project("case_version")
    module = ReadConfig().get_project("module")
    print(host)
    print(app_version)
    print(case_version)
    print(module)


