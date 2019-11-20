# coding:utf-8

import unittest
from util.HTMLTestRunner3 import HTMLTestRunner
from configs.config_reader import ReadConfig


def add_py_case(case_path, rule):
    # 定义discover方法的参数
    discover = unittest.defaultTestLoader.discover(case_path, pattern=rule)
    return discover


def custom_report(all_case):
    html_report_path = ReadConfig().get_report("html_report_path")
    html_report_title = ReadConfig().get_report("html_report_title")
    html_report_description = ReadConfig().get_report("html_report_description")
    tester = ReadConfig().get_report("html_report_tester")
    project_name = ReadConfig().get_project("project_name")
    app_version = ReadConfig().get_project("app_version")
    title = f'{project_name}{html_report_title}'
    description = f'{html_report_description}{app_version}'
    fp = open(html_report_path, "wb")
    HTMLTestRunner(stream=fp, title=title, description=description, tester=tester).run(all_case)
    fp.close()


if __name__ == "__main__":
    py_file_path = ReadConfig().get_cases("py_file_path")
    case_source = ReadConfig().get_cases("case_source")
    file_rule = f'{case_source}{"*"}'
    cases = add_py_case(py_file_path, file_rule)
    custom_report(cases)
