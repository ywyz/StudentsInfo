'''
Author: ywyz
Date: 2022-01-25 09:52:01
LastEditTime: 2022-01-27 11:46:48
LastEditors: ywyz
Description: 将数据导出至mysql数据库
FilePath: /StudentsInfo/ImportDataToSQL.py
'''

from openpyxl import load_workbook
from Students import Students


def InsertOldInfo():
    # 插入旧表
    filepath = '2020.9.1防疫信息表.xlsx'
    wb = load_workbook(filename=filepath)
    sheetName = "学生"
    ws = wb[sheetName]

    for row in ws.rows:
        if row[0].value == "序号":
            continue

        else:

            student = Students(row[3].value, '男', row[7].value, row[8].value,
                               row[4].value, row[5].value, row[11].value, ' ',
                               '0')
            student.InsertIntoSql()
    print("插入成功")


InsertOldInfo()


def insertNewInfo():
    """插入新表"""
