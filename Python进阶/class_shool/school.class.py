# -*-coding:utf-8 -*-
# @Author   ：pr1s0n
# @Time     : 2020/6/16 22:50
# @FileNAme : school.class.py
# @Blog     : http://www.pr1s0n.com

class School:
    school_name = 'Shengda EDU'
    def __init__(self,nickname,addr):
        self.nickname = nickname
        self.addr = addr
        self.classes = []

    def related_Class(self,class_obj):
        self.classes.append(class_obj)

    def tell_class(self):
        print('\n'+self.nickname.center(60,'='))

        for class_obj in self.classes:
            class_obj.tell_course()

school_obj1 = School('Shenda EDU zhengzhou','郑州')
school_obj2 = School('Henan EDU kaifeng','开封')

class Class:
    def __init__(self,name):
        self.name = name
        self.Course = None

    def related_course(self,course_obj):
        self.course = course_obj

    def tell_course(self):
        print('%s' % self.name,end = ' ')
        # self.course.tell_info()

# 创建一个班级
class_obj1 = Class('工程造价')
class_obj2 = Class('土木工程')
class_obj3 = Class('计算机科学与技术')

# 为班级关联一个课程
class_obj1.related_course('平法识图')
class_obj2.related_course('工程测量')
class_obj3.related_course('C语言程序开发')

school_obj1.related_Class(class_obj1)
school_obj1.related_Class(class_obj2)
school_obj2.related_Class(class_obj3)


# school_obj1.tell_class()
# school_obj2.tell_class()



class Course:
    pass

class Student:
    pass