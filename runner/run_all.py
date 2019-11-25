# coding:utf-8

import os
import sys
current_working_directory = os.path.abspath(os.path.dirname(os.getcwd()))
sys.path.append(current_working_directory)

from util.html_reporter import add_py_case, custom_report
from util.email_sender import Email
from configs.config_reader import ReadConfig


def run_all_case():
    py_file_path = ReadConfig().get_cases("py_file_path")
    case_source = ReadConfig().get_cases("case_source")
    # 若从配置文件读取收件人，先要将str转换为list
    receive_users = eval(ReadConfig().get_email("receive_users"))
    email_title = ReadConfig().get_email("email_title")
    html_report_path = ReadConfig().get_report("html_report_path")
    html_report_name = ReadConfig().get_report("html_report_name")
    project_name = ReadConfig().get_project("project_name")
    title = f'{project_name}{email_title}'
    rule = f'{case_source}{"*"}'
    cases = add_py_case(py_file_path, rule)
    custom_report(cases)
    # 注意：建议调试代码时，屏蔽发邮件功能
    # Email().send_attach(receive_users, title, html_report_path, html_report_name)


if __name__ == "__main__":
    '''
    :param param1: host
    :param param2: app_version
    :param param3: module(0:全部,1:首页,2:学习,3:发现,4:我的)
    :param param4: case_version(0:全部,1:旧版本,2:新版本) 
    '''
   # ReadConfig().write_config(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    run_all_case()
