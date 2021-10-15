
import turtle as t
from pyecharts.charts import Bar
import random
import math
from numpy import *
import copy
import jieba
import requests

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

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++2021.10.8

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

    #tuple1=tuple(range(20))
    #for i in tuple1:
    #    print(i)
    #print(tuple1[:14:-1])
    
    #a_tuple=tuple(range(20))
    #for i in a_tuple:
    #    print(i,end=' ')
    #print("")
    #b_tuple=a_tuple[19:19-5:-1]
    #for i in b_tuple:
    #    print(i,end=' ')
    #print("")

    #dict1={'a':1,'b':2,'c':3}
    #for i in dict1.items():
    #    print(i)
    #for key,value in dict1.items():
    #    print(key,value)
    #print(dict1.keys())
    #print(dict1.values())

    #x=['A','B','C','D']
    #y=['a','b','b','c']
    #dict2=dict(zip(x,y))
    #print(dict2)

    #x1=['name','phone','address']
    #y1=['小明','123','某路1号']
    #dict3=dict(zip(x1,y1))
    #print(dict3)

    #dict4 = {'广东':{'广州':{'白云区'},
    #            '深圳':{'龙岗区'},
    #            '佛山':{'禅城区'},
    #            },
    #         '辽宁':{'大连':{'甘井子区'},
    #            '沈阳':{'和平区'},
    #            '盘锦':{'大洼区'},
    #            }
    #     }
    #print(dict4)
    #print(dict4.get('广东'))
    #print(dict4.get('广东').get('佛山'))

    #import random
    #listRandom=[random.choice(range(10000)) for i in range(100)]
    #newSet=set(listRandom)
    #print(listRandom)
    #print(newSet)

    #aList=[3,5,7]
    #bList=aList[::]
    #print(aList==bList)
    #print(aList is bList)
    #print(id(aList)==id(bList))
    #bList[1]=8
    #print(bList)
    #print(aList)

    #x=[1,2,[3,4]]
    #y=copy.deepcopy(x)
    #x[0]=5
    #print(x)
    #print(y)
    #x[2].append(6)
    #print(x)
    #print(y)

    #x=[1,2,[3,4]]
    #y=copy.deepcopy(x)
    #print(x)
    #print(y)


    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++10.15

    #s1="下午上课中"
    #print(s1.encode('gb2312'))
    ##print(s1.encode('gb2312').decode('utf-8'))
    #print(s1.encode('gb2312').decode('gb2312'))

    #x1=1.2345
    #print("%+010.3f"%x1)

    #data1=(102.11,444.3,13.111)
    #print("A:{0[0]};B:{0[1]};C{0[2]}".format(data1))

    #print(s1)
    #print(s1[::-1])
    #print(s1[1::2])
    #s2="Python语言程序设计"
    #for i in s2[::2]:
    #    print(i,end=" ")
    #print("")

    s3="AA#23.8#35%#1#BB"
    #if s3[:2]=="AA":
    #    s3a=s3.split("#")
    #    print("室内温度：",s3a[1],"度")
    #    print("室内温度：",s3a[2])
    #    if(s3a[3]=="1"):
    #        print("防盗检测：有外人闯入")
    #    else:
    #        print("无效数据")

    #s4="《战狼二》是吴京指导的阿巴阿巴阿巴阿巴阿巴阿巴阿巴阿巴阿巴阿巴阿巴吴京阿巴"
    #print(s4.find("吴京"))
    #print(s4.find("吴京",8))
    #print(s4.find("吴京",8,29))
    #print(s4.rfind("吴京"))

    #print(s4.index("吴京"))
    #print(s4.index("吴京",8))
    #print(s4.rindex("吴京"))

    #print(s4.count("阿巴"))
    #print(s4.count("演员"))

    #print(len(s4))

    #s5="下午 \n 课 \n \n 是 \t 满课"
    #print(s5)
    #print(s5.split())

    #if s3[:2]=="AA":
    #    print(s3.split("#"))
    #    print(s3.split("A#"))
    #print(s5.split(maxsplit=2))

    #x = '中文分词的准确性影响后续判断'
    #test_string = jieba.lcut(x)
    #print(test_string)

