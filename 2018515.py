import datetime
import numpy as np
import matplotlib.pyplot as plt

print('请输入文件所在位置：')
str=input()#"C:\\Users\\lenovo\\Desktop\\car.csv"

all=np.loadtxt(str,delimiter=',',skiprows=1,usecols=(1,2,3,4))
a=all[:,0]
b=all[:,1]
time = np.loadtxt(str,dtype='str', delimiter=',', skiprows=1, usecols=(0))

c=all.shape
a1=[]#最低价正序列表
b1=[]#均价正序列表
x=[]#日期列表
y=[]
y1=[]#数据个数 计数列表
for i in range(0,c[0]):
    x.append(datetime.datetime.strptime(time[i],'%Y年%m月%d日'))
    y.append(c[0]-i)
for i in range(0,c[0]):
    a1.append(a[c[0]-1-i])
    b1.append(b[c[0]-1-i])
    y1.append(i+1)
# print(a)
# print(b)
# print(x)
# print(y)
#画图
plt.scatter(y,a,label='low',color='red',linewidth=0.8)
plt.scatter(y,b,label='aver',color='blue',linewidth=0.8)
plt.plot(y,a,label='low',color='red',linewidth=0.8)
plt.plot(y,b,label='aver',color='blue',linewidth=0.8)
# plt.scatter(x,a,label='low',color='red',linewidth=0.8)
# plt.scatter(x,b,label='aver',color='blue',linewidth=0.8)
# plt.plot(x,a,label='low',color='red',linewidth=0.8)
# plt.plot(x,b,label='aver',color='blue',linewidth=0.8)
#plt.plot(time,,label='aver',color='blue',linewidth=0.8)
plt.xlabel("date")
plt.ylabel("value")
plt.title("car")
plt.legend()
plt.show()
#观察数据之后，取上升段的数据，生成要用的拟合列表
while(1):
    print('input start')
    start=int(input())
    print('input over')
    over=int(input())
    print('最低价',a1[start:over])
    print('均价',b1[start:over])
    print(y1[start:over])