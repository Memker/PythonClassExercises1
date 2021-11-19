import time

import datetime

#s="1234567890"
#f1=open("序列总结.txt","w")
#if(f1.write(s)):
#    print("1")
#else:
#    print("2")
#f1.close()
#f2=open("序列总结.txt","r")
#print(f2.read())
#f2.seek(0)
#print(f2.read(5))
##f2.seek(3)
#print(f2.read(5))
#f2.close()

#from openpyxl import Workbook
#wb=Workbook()
#from openpyxl import load_workbook
#wb2=load_workbook("新建 Microsoft Excel 工作表.xlsx")
#ws=wb2.active
#rows=[]
#for row in ws.iter_rows():
#    rows.append(row)
#print(rows)
#print(rows[0])
#print(rows[0][0])
#print(rows[0][0].value)
#print(rows[len(rows)-1])
#print(rows[len(rows)-1][len(rows[0])-1])
#print(rows[len(rows)-1][len(rows[0])-1].value)

#class Cat:
#    def sayHello(self):
#        print("喵-----1")

#class Bosi(Cat):
#    def sayHello(self):
#        print("喵喵----2")
#bosi = Bosi()
#bosi.sayHello()

#def fibonacci(n,w=0):
#    a, b, counter = 0, 1, 0
#    while True:
#        if (counter > n): 
#            return
#        yield a
#        a, b = b, a + b
#        print('%d,%d' % (a,b)) 
#        counter += 1
#f = fibonacci(10,0)
#print (next(f))

#class Car:
#    price = 10  #定义类属性
#    __price2=20   
#    _price3=20 
#    def __init__(self, value1 = 1, value2 = 2):
#        self._value1 = value1
#        self.__value2 = value2
#car = Car(10)
#print(car._value1,car.__value2)

#class Car:
#    price = 10  #定义类属性
#    price2=20   
#    _price3=30 
#car = Car()
#print(car.price2)

class Car:
    price = 100000  #定义类属性
    def __init__(self, c):
        self.price = c #定义实例属性

car1 = Car(10)
Car.price =20
print('{0}#{1}'.format(car1.price,Car.price))
