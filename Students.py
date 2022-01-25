'''
Author: your name
Date: 2022-01-25 11:08:08
LastEditTime: 2022-01-25 15:15:27
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: /StudentsInfo/Students.py
'''
"""
学生类型，包括名字，年级，班级，父母姓名，家庭住址，手机号码
"""

class Students():
    def __init__(self, name, grade, classes, parent_name, phone, address, isOut):
        self.name = name
        self.name = grade
        self.classes = classes
        self.parent_name = parent_name
        self.phone = phone
        self.address = address
        self.isOut = isOut

    def get_name(self):
        return self.name

    def get_grade(self):
        return self.grade
    
    def get_classes(self):
        return self.classes

    def get_parent_name(self):
        return parent_name
    
    def get_phone(self):
        return phone
    
    def get_address(self):
        return address

    def get_isOut(self):
        return isOut

    def Insert