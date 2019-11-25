# coding:utf-8

import xlrd
from configs.config_reader import ReadConfig

#读取Excel
class Excel:
    def __init__(self, excel_path, sheet):
        self.excel_path = excel_path
        self.sheet_name = sheet
        self.data = None
        self.table = None
        self.row = None
        self.row_id = None
        self.col_id = None
        self.curRowNo = 1

    def open_excel(self):
        self.data = xlrd.open_workbook(self.excel_path)
        self.table = self.data.sheet_by_name(self.sheet_name)
        self.keys = self.table.row_values(0)
        self.row_id = self.table.nrows
        self.col_id = self.table.ncols

    def read_excel(self):
        self.open_excel()
        if self.row_id <= 1:
            print("总行数小于1")
        else:
            r = []
            j = 1
            for i in list(range(self.row_id - 1)):
                s = dict()
                # 从第二行取对应values值
                s['row_id'] = i + 2
                values = self.table.row_values(j)
                for x in list(range(self.col_id)):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j += 1
            return r


if __name__ == "__main__":
    excel_cases_path = ReadConfig().get_cases("excel_cases_path")
    sheet_name = ReadConfig().get_cases("sheet_name")
    er = Excel(excel_cases_path, sheet_name)
    test_data = er.read_excel()
    print(test_data)





