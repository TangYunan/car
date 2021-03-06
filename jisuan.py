##列表
# 最低价 [11600.0, 14000.0, 18700.0, 23900.0]
# 均价 [12627.0, 15743.0, 20631.0, 26599.0]
# [10, 11, 12, 13]
# 最低价 [12000.0, 13200.0, 14500.0, 16800.0, 20200.0, 26000.0, 35000.0]
# 均价 [13137.0, 14331.0, 15436.0, 17798.0, 21506.0, 27672.0, 37805.0]
# [30, 31, 32, 33, 34, 35, 36]
# 最低价 [16000.0, 19000.0, 24600.0]
# 均价 [17487.0, 20609.0, 27077.0]
# [39, 40, 41]
# 最低价 [17300.0, 18900.0, 21500.0, 23900.0, 25000.0, 26800.0, 28800.0, 30000.0, 30700.0]
# 均价 [18358.0, 20127.0, 22996.0, 25498.0, 26668.0, 28561.0, 30535.0, 32449.0, 34046.0]
# [56, 57, 58, 59, 60, 61, 62, 63, 64]
# 最低价 [22800.0, 25300.0, 32100.0]
# 均价 [24560.0, 26939.0, 34455.0]
# [67, 68, 69]
#最低价预计价格 对应拟合列表
# 30949 [11600.0, 14000.0, 18700.0, 23900.0]
# 43100 [12000.0, 13200.0, 14500.0, 16800.0, 20200.0, 26000.0, 35000.0]
# 32799 [16000.0, 19000.0, 24600.0]
# 31919 [17300.0, 18900.0, 21500.0, 23900.0, 25000.0, 26800.0, 28800.0, 30000.0, 30700.0]
# 43200 [22800.0, 25300.0, 32100.0]
#均价预计价格 对应拟合列表
#34166 [12627.0, 15743.0, 20631.0, 26599.0]
#46733 [13137.0, 14331.0, 15436.0, 17798.0, 21506.0, 27672.0, 37805.0]
#36891 [17487.0, 20609.0, 27077.0]
#35505 [18358.0, 20127.0, 22996.0, 25498.0, 26668.0, 28561.0, 30535.0, 32449.0, 34046.0]
#47108 [24560.0, 26939.0, 34455.0]
#
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import leastsq

num=np.array([24560.0, 26939.0, 34455.0])  #每次修改这里的用来拟合的数据 得到预计价格
n=num.shape
list=[]
for i in range(0,n[0]):
    list.append(i+1)

plt.figure(figsize=(9,9))

x=np.linspace(0,10,1000)
X=np.array(list)
Y=np.array(num)

def f(p):
    a,b,c=p
    return(Y-(a*X*X + b*X +c))

r=leastsq(f,[1,0,0])
a,b,c=r[0]
print('a=',a,'b=',b,'c=',c)

y=a*x*x + b*x +c
ax=plt.gca()
def out(x):
    global a,b,c
    return(a*x*x + b*x +c)
print(n[0])
print(out(n[0]+1))    ##预计价格

print('最低价预测平均值',(30949+43100+32799+31919+43200)/5)
print('均价预测平均值',(34166+46733+36891+35505+47108)/5)
