import turtle as t
from pyecharts.charts import Bar
import random
import math
from numpy import *
import copy
import jieba
import requests

#class Car:
#    price = 100000
#    __price2=20
#    _price3=20

#    def __init__(self,c):
#        self.color = c
#car1=Car("Red")
#car2=Car("Blue")
#print(car1.color,Car.price)


#class Car1:
#    price = 10
#    __price2=20
#    _price3=20
#    def __init__(self,value1=1,value2=2):
#        self._value1=value1
#        self.__value2=value2
#    def setValue(self,value1,value2):
#        self._value1=value1
#        self.__value2=value2
#    def show(self):
#        print(self._value1)
#        print(self.__value2)
#car=Car1()
#print(car._value1)
#print(car._Car1__value2)
#print(Car1.price)

#class Root:
#    __total=0
#    def __init__(self,v):
#        self.__balue=v
#        Root.__total+=1
#    def show(self):
#        print("self.value:",self,__value)
#        print("Root.__total1:",Root.__total)
#    @classmethod
#    def classShowTotal(cls):
#        print(cls.__total)
#    @staticmethod
#    def staticShowTotal(cls):
#        print(Root.__total)
#r=Root(3)
#r.classShowTotal
#r.staticShowTotal()
#r.show()
#r1 = Root(3)
#R1.show()
#print(r)

#class Money(object):
#    def __init__(self):
#        self.__money=0
#    def getMonety(self):
#        return self.__money
#    def setMoney(self, value):        
#        if isinstance(value, int):            
#           self.__money = value       
#        else:            
#           print("error:不是整型数字")    

#    money = property(getMoney, setMoney)
#a = Money() 
#print(a.money)
#a.money = 100
#print(a.money)

#class Student(object):
#    def __init__(self):
#        self.__id=""
#        self.__name=""
#        self.__age=""
#        self.__gender=""
#        self.__address=""
#    def getStudent(self):
#        return [self.__id,self.__name,self.__age,self.__gender,self.__address]
#    def setStudent(self,a,b,c,d,e):
#        self.__id=a
#        self.__name=b
#        self.__age=c
#        self.__gender=d
#        self.__address=e
#    student=property(getStudent,setStudent)
#s=Student()
#s.setStudent("1","小明","20","男","软件园路8号")
#print(s.student)


#class A(object):
#    def __init__(self):
#        self.__private()
#        self.public()
#    def __private(self):
#        print("__private() method in A")
#    def public(self):
#        print("public() Method in A")
#class B(A):
#    def __private(self):
#        print("__private() method in 8")
#    def public(self):
#        print("public() method in 8")
#b=B()
#__private() method in A
#public() method in B


#x=[item() for item in (Animal,Cat,Dog,Tiger,Test)]
#for item in x:
#    item.show()

#class Person(object):
#    def __init__(self,name,work):
#        self.name=name
#        self.work=work
#    def doWork(self):
#        if self.work=="teacher":
#            print(self.name+"is teacher")
#class Teacher(Person):
#    pass
#p1=Person("小明","teacher")
#p1.doWork()
#class Teacher(Person):
#    def doWork(self):
#        if self.work=="teacher":
#            print(self.name+"is teach student")
#class Person(Teacher):
#    pass
#p1=Person("小明","teacher")
#p1.doWork()

