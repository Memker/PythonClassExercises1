
import turtle as t
from pyecharts.charts import Bar
import random
import math
from numpy import *

#def curveMove():
#    for i in range(100):
#        t.right(2)
#        t.forward(1)
#def curveHeart():
#    t.color('purple', 'red')
#    t.begin_fill()
#    t.left(140)
#    t.forward(55)
#    curveMove()
#    t.left(120)
#    curveMove()
#    t.forward(55)
#    t.end_fill()
#    t.done()
#    t.bye()
#if __name__=="__main__":
#    t.screensize (400,300,'#FFFF99')
#    t.title('绘制多彩的心')
#    curveHeart()


#def demo1():
#    bar = Bar()
#    bar.add_xaxis(["泰坦尼克号","阿凡达", "星球大战7：原力觉醒"])
#    bar.add_yaxis("电影排名", [22,27,21])
#    bar.render()


if __name__ == '__main__':
#    demo1()
    #x = math.sqrt(9) if 5>3 else random.randint(1,100)
    #x = math.sqrt(9) if 5>3 else random.randint(1,100)


    #a,b = map(int,input().split(' '))
    #if a>b:
    #    a,b=b,a
    #print(a,b)


    #a = int(input())
    #if a%2==0:
    #   print("a是偶数,a=%d" % a) 
    #else:
    #    print("a=%d" % a)

    #height,weight = map(float,input("请输入身高+空格+体重：").split( ' ' ))
    #b = float(weight/(height**2))
    #if b<18.5:
    #    print("过轻")
    #elif 18.5 <= b <= 23.9:
    #    print("正常")
    #elif 24 <= b <= 27:
    #    print("过重")
    #elif 28 <= b <=32:
    #    print("肥胖")
    #elif b>32:
    #    print("非常肥胖")
    
    #def test():
    #    for n in range(100,1,-1):
    #        for i in range(2,n):
    #            if n%i ==0:
    #                break
    #            else:
    #                print(n)
    #                return
    #test()
    #print("==========================================")
    #for n in range(100,1,-1):
    #        for i in range(2,n):
    #            if n%i ==0:
    #                break
    #            else:
    #                print(n,end=' ')
    #                break
    #print("")
    #print("==========================================")
    #for i in range(10):
    #    if i%2==0:
    #        continue
    #    print(i,end=' ')
    #print("")
    #print("==========================================")

    #i=int(input("输入次数："))
    #for j in range(i):
    #    r = int(input("输入成绩："))
    #    if r>=90:
    #        print("A")
    #    elif 80<=r<90:
    #        print("B")
    #    elif 70<=r<80:
    #        print("C")
    #    elif 60<=r<70:
    #        print("D")
    #    elif r<60:
    #        print("E")
    #print("==========================================")

    #for i in range(1,10):
    #   for j in range(1, i +1 ):
    #       print("%d*%d=%d" % (i,j,i*j),end = ' ')
    #   print("")

    #a_list = ['a','b','mpilgtim','z','example']
    #print(a_list)

    #aList=[1,2,3,4,5]
    #aList.insert(4,6)
    #print(aList)

    #a_list = [1,2,3,4,5,6]
    #del a_list[3]
    #print(a_list)

    #list2 = [1,2,3,1,1,1,1,1]
    #for i in range(len(list2)-1,-1,-1):
    #    if list2[i] == 1:
    #        del list2[i]
    #        print(list2)
    #for j in list2:
    #    print(j,end=' ')

    #print()

    #list1 = [1,2,3,3,2,1]
    #list1.remove(2)
    #print(list1)

    #list3 = [3,4,5,6,7,9,11,13,15,17]
    #print(list3[::])
    #print(list3[::-1])
    #print(list3[::2])
    #print(list3[1::2])
    #print(list3[3::])
    #print(list3[3::6])
    #print(list3[0:100:1])
    #print(list3[100:])
    ##list3[100]
    
    #list4=[1,2,3]
    #list5=[4,5,6]
    #list6=zip(list4,list5)

    #list7=[['Apple','Google','Microsoft'],
    #       ['java','python','ruby','php'],
    #       ['adm','bart','lisa']
    #       ]
    #print(list7[-3][0])
    #print(list7[-2][1])
    #print(list7[-1][1])

    #list8=['Apple','Google','Microsoft','java','python','ruby','php','adm','bart','lisa']
    #for i in range(len(list8)):
    #    print(list8[i])

    #list9=[]
    #num=0
    #while(1):
    #    list9.append(int(input()))
    #    if list9[num]==-1:
    #        del list9[num]
    #        break
    #    num+=1
    #print(mean(list9))
    #list9.sort()
    #print(list9[len(list9)-1])
    #print(list9[0])
    #list9.sort(reverse=True)
    #print(list9)
    #list9.sort()
    #print(list9)
        
    #list10=[x*x for x in range(10)]
    #print(list10)

    #vec=[[1,2,3],[4,5,6],[7,8,9]]
    #[num for elem in vec for num in elem]
    
    #list11[-1,-4,6,7,5,-2,3,9,-11]
    #[i for ]
    #print(list11)

    #print(2.5+7%3*int(2.5+4.7)%2/4)

    #print(float(2+3)/2+int(3.5)%int(2.5))

    #+++++++++++++++++++++++++++++++++++++++++++2021.10.8

    #v_typle = (False,3.5,'exp')
    #(x,y,z)=v_typle
    #x,y,z=v_typle
    #x,y,z=[0,1,2]
    #x.y.z=1,2,3
    #x,y,zz=range(3)

    #keys=['a','b','c','d']
    #values=[1,2,3,4]
    #for k,v in zip(keys,values):
    #    print((k,v),end=' ')

    #aList=[1,2,3]
    #bList=[4,5,6]
    #cList=[7,8,9]
    #dList=zip(aList,bList,cList)
    #for index,value in enumerate(dList):
    #    print(index,':',value)

    tuple1=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
    for i in tuple1:
        print(i)
    print(tuple1[:14:-1])
