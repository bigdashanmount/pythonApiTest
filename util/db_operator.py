# coding:utf-8


import pymysql
from configs.config_reader import ReadConfig


def db_values(sql):
    db_host = ReadConfig().get_db("host")
    db_user = ReadConfig().get_db("user")
    db_pw = ReadConfig().get_db("password")
    db_name = ReadConfig().get_db("name")
    if db_host and db_user and db_pw and db_name:
        db = None
        try:
            db = pymysql.connect(host=db_host, user=db_user, password=db_pw, db=db_name)
            cursor = db.cursor()
            cursor.execute(sql)
            db.commit()
            return cursor.fetchall()
        except Exception as e:
            print(e)
            raise Exception('数据库操作失败')
        finally:
            if db:
                db.close()
    else:
        raise Exception('数据库连接参数错误')


def check_data_equal_db(exp, sql):
    data = db_values(sql)
    if data:
        if exp == data[0][0]:
            print("验证通过，数据库中存在：", exp)
        else:
            print("验证失败，数据库中不存在：", exp)
    else:
        print("sql执行错误：", sql)


if __name__ == '__main__':
    exp_data = "108745###10分"
    pre_sql = "select content from sms where mobile = 13241411941 order by smsid limit 1"
    check_data_equal_db(exp_data, pre_sql)

