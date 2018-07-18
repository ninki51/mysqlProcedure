# coding:utf-8
import matplotlib.pyplot as plt
import math

# 初二数学作业：求两点到直线的最小距离和
# 清空画布
plt.clf()
k = -1.0
b = 40.0

x = range(0, 41)
y = [k * t + b for t in x]

# F点(0,2)
# E点(1,0)
fx = 0
fy = 20
# F'是F的对称点
fx0 = 20
fy0 = 40

ex = 10
ey = 0

# 最短距离
minD = 1000
# 要得到的最佳位置(x0,y0)
x0 = 0
y0 = 0

for px in range(0, 41):
    py = k * px + b
    # 计算E,F两点到直线kx+b的距离和
    d1 = math.sqrt((px - fx) * (px - fx) + (py - fy) * (py - fy))
    d2 = math.sqrt((px - ex) * (px - ex) + (py - ey) * (py - ey))
    d = d1 + d2
    # print(px, py, d1, d2, d)
    if d < minD:
        minD = d
        x0 = px
        y0 = py

print("E,F两点到直线kx+b的最短距离是：", x0, y0)
print(minD, math.sqrt(17.0))

# plt.plot(x, y)
plt.plot(x, y, linewidth='1', color='r', linestyle='-')
plt.plot([ex, x0], [ey, y0], linewidth='1', color='g', linestyle='-', marker='.')
plt.plot([fx, x0], [fy, y0], linewidth='1', color='b', linestyle='-', marker='.')

# F'为F的对称点
plt.plot([fx0, x0], [fy0, y0], color='b', linestyle='--', marker='.')
# 连接 F和F'
plt.plot([fx0, fx], [fy0, fy], color='#AAAAAA', linestyle='--', marker='.')

plt.annotate("F", xy=(fx, fy), xytext=(fx+.2, fy+.2))
plt.annotate("F'", xy=(fx0, fy0), xytext=(fx0+.2, fy0+.2))
plt.annotate("E", xy=(ex, ey), xytext=(ex+.2, ey+.2))
plt.annotate("P", xy=(x0, y0), xytext=(x0+.3, y0))

# 在屏幕上显示
plt.title("y=kx+b")
plt.xlabel('x')
plt.ylabel('y')
ax = plt.gca()
# 宽高比=1
ax.set_aspect(1)
plt.grid()
plt.show()
