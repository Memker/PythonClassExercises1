import pymysql
con = pymysql.connect(host="localhost",user="root",password="q916263561",database="pyclass")
cus=con.cursor()
try:
    cus.execute("insert into student(name) values('小明')")
    cus.execute("update student set name='小红' where name='小明'")
    cus.execute("delete from student where name='小红'")
    con.commit()
except Exception as e:
    con.rollback()
    print(e)
cus.execute("select * from student")
data=cus.fetchall()
print(data)
cus.close()
con.close()


