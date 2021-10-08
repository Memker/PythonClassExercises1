#a = intput("hello")
#print(a)

#height,age = map(int,input("输入身高(170 34cm)+空格+年龄:").split(' '))
num1 = float(input("输入体重："))
num2 = float(input("输入运动时间："))
num3 = 1234
num4 = num1*num2*num3
print("每天消耗：%.2f" % num4)

height,age = map(int,input("手输入身高(cm)+空格+年龄：").split(' '));
weight = float(input("输入体重："))
K = float(input("输入运动系数："))
k = weight*K*height*age
print('消耗大卡：%.2f' % k)
apple = 83
num = k//apple
print('想减肥，每天只能吃{:.0f}个苹果'.format(num))