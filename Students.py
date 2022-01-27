'''
Author: your name
Date: 2022-01-25 11:08:08
LastEditTime: 2022-01-27 11:10:55
LastEditors: ywyz
Description:学生类型，包括名字，年级，班级，父母姓名，家庭住址，手机号码
FilePath: /StudentsInfo/Students.py
'''

import pymysql
# 打开数据库链接
db = pymysql.connect(host="localhost",
                     user="StudentInfo",
                     password="yw980924@163.com",
                     database="StudentInfo")
cursor = db.cursor()


class Students():
    def __init__(self, name, sex, grade, classes, parent_name, phone, address,
                 employer, isOut):
        self.name = name
        self.grade = grade
        self.classes = classes
        self.parent_name = parent_name
        self.phone = phone
        self.address = address
        self.isOut = isOut
        self.sex = sex
        self.employer = employer

    def get_name(self):
        return self.name

    def get_sex(self):
        return self.sex

    def get_grade(self):
        return self.grade

    def get_classes(self):
        return self.classes

    def get_parent_name(self):
        return self.parent_name

    def get_phone(self):
        return self.phone

    def get_address(self):
        return self.address

    def get_isOut(self):
        return self.isOut

    def get_employer(self):
        return self.employer

    def InsertIntoSql(self):
        sqlInsert = "Insert into basicinfo (name, sex, grade, classes, parentname, phone, address, employer, isOut) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (
            self.name, self.sex, self.grade, self.classes, self.parent_name,
            self.phone, self.address, self.employer, self.isOut)

        cursor.execute(sqlInsert)
        db.commit()
