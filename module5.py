import  pymysql
class student(object):
    def __init__(self):
        self.conn = pymysql.connect(host="localhost",user="root",password="q916263561",database="pyclass")
        self.cursor = self.conn.cursor()
    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def selectStudent(self):
        self.cursor.execute("select * from student")
        data=self.cursor.fetchall()
        print(data)
        pass
    def insert_one_student(self, id, name, age):
        try:
            self.cursor.execute("insert into student(id,name,age) values(%s,'%s',%s)" % (id,name,age))
            self.conn.commit()
            print("添加成功")
        except Exception as e:
            print(e)
            self.conn.rollback()
        pass
    def update_studentByName(self,name,age):
        try:
            self.cursor.execute("update student set age=%s where name='%s'" % (age,name))
            self.conn.commit()
            print("修改成功")
        except Exception as e:
            print(e)
            self.conn.rollback()
        pass
    def delet_studentByName(self,name):
        try:
            self.cursor.execute("delete from student where name='%s'" % (name))
            self.conn.commit()
            print("删除成功")
        except Exception as e:
            print(e)
            self.conn.rollback()
        pass
    def run(self):
        while(True):
            print("1.所有学生")
            print("2.添加学生")
            print("3.删除学生")
            print("4.修改学生信息")
            print("0.退出")
            num = input("请输入功能编号：")

            if num == "1":
                self.selectStudent()
            elif num == "2":
                id = int(input("请输入学号："))
                name= input("请输入姓名：")
                age = int(input("请输入年龄："))
                self.insert_one_student(id, name, age)
            elif num == "3":
                name = input("请输入姓名：")
                self.delet_studentByName(name)
            elif num == "4":
                name = input("请输入姓名：")
                age = input("请输入年龄：")
                self.update_studentByName(name,age)
            elif num == "0":
                break;
            else:
                print("输入有误")
            


if __name__ == '__main__':
    stu = student()
    stu.run() #调用增删改查的函数

