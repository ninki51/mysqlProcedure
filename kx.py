#coding:utf-8
import matplotlib.pyplot as plt
import math

# 清空画布
plt.clf()
k = 1.2
b = 2.0

x = range(-20,20)
y = [k * t + b for t in x]
#plt.plot(x, y)
plt.plot(x, y, linewidth='2', color='r', linestyle='-', marker='.')

# 在屏幕上显示
plt.title("y=kx+b")
plt.xlabel('x')
plt.ylabel('y')
ax = plt.gca()
#宽高比=1
ax.set_aspect(1)
plt.grid()
plt.show()
