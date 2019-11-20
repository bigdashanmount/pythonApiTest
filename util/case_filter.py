# coding:utf-8

from configs.config_reader import ReadConfig
from util.excel_parser import Excel


def get_test_cases():
    """
        active: 用例状态(0:全部,1:启用,2:禁用)
        module: 模块(0:全部,1:首页,2:学习,3:发现,4:我的)
        case_version: 用例版本(0:全部,1:旧版本,2:新版本)
    """
    excel_cases_path = ReadConfig().get_cases("excel_cases_path")
    sheet_name = ReadConfig().get_cases("sheet_name")
    er = Excel(excel_cases_path, sheet_name)
    all_cases = er.read_excel()
    # host = ReadConfig().get_project("host")
    # app_version = ReadConfig().get_project("app_version").replace(".", "")
    case_version = ReadConfig().get_project("case_version")
    module = ReadConfig().get_project("module")
    test_cases = [case for case in all_cases if case["active"] == "1"
                  if module == "0" or module == case["module"]
                  if case_version == "0" or case_version == case["case_version"]]
    return test_cases


if __name__ == '__main__':
    cases = get_test_cases()
    for c in cases:
        print(c)
        # print("case_id:", cases["case_id"])
        # print("case_name:", cases["case_name"])
