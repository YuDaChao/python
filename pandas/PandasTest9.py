# encoding: utf-8
"""
@author: YuDc
@file: PandasTest9.py
@time: 2017/6/4 15:04
@desc: matplotlib
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 准备数据,产生0~9是个数据
x = np.arange(10)
# 以画一条直线为例
y = 2*x +1
# 在 -3 和 3 之间产生50个数
x1 = np.linspace(-3,3,50)
y1 = x1**2 + 1
# 我们可以定义图像窗口的编号, 大小
plt.figure(num=2, figsize=(7,5))
# 使用plt 的 plot()方法画(x, y)
# color : 设置线的颜色
# linewidth : 设置线的宽度
# linestyle : 设置线的样式, 这里为虚线样式
line1, = plt.plot(x, y, color="red", linewidth=1.0, linestyle="--", label="straight line")
line2, = plt.plot(x1, y1, color="green", linewidth=1.0, label="curve line")
# 设置x轴, y轴的范围
# plt.xlim((1,5))
# plt.ylim(1,12)
# 设置x轴, y轴的名称
plt.xlabel("i am x")
plt.ylabel("i am y")
# 让图例生效显示

"""
loc : 设置图例的位置
        best ： 系统会自动选择合适的位置
        upper right : 右上
        upper left  ：左上
        lower left  ：左下
        lower right ：右下
        right       ：右
        center left ：左中
        center right：右中
        lower center：中下
        upper center：中上
        center      ：中
"""
# plt.legend(loc="best",handles=[line1, line2], labels=["straight line 1","curve line 2"])
plt.legend(loc="best")
# 设置y轴值对应的名称
# 这里的数值和名称是一一对应的
# plt.yticks([1,3,5,7,9,11],["p","y","t","h","o","n"])
# 用通用的方式我们也可以设置x轴
# plt.xticks()
# 设置坐标轴
# 使用plt.gca()获取当前坐标轴信息
ax = plt.gca()
# 使用plt.spines设置边框, set_color()设置边框的颜色
# 设置上边框
ax.spines["top"].set_color("none") # 让上边框不显示
# 设置右边框
ax.spines["right"].set_color("none") # 让右边框不显示
# 使用ax.xaxis.set_ticks_position() 设置x坐标的刻度位置
# 可选值 : top bottom both default none
ax.xaxis.set_ticks_position("bottom")
# 使用ax.yaxis.set_ticks_position() 设置y坐标的刻度位置
ax.yaxis.set_ticks_position("left")
# 将x轴的位置移动到 y = 5
ax.spines["bottom"].set_position(("data",0))
# 将y轴的位置移动到 x = 2
ax.spines["left"].set_position(("data",0))

# 使用Annotation 标注
# 先在线上成一个点
x = 4
y = 2*x + 1
# s ： 、生成点的大小， c ：生成点的颜色
plt.scatter(x, y, s=20, c="k")
# 根据点画线
# [x,x],[y,0] ： 画线的坐标
# linewidth ：线的宽度
# linestyle ：线的样式
# color ：线的颜色
# 可以简写 ： plt.plot([x,x],[y,0], linewidth=2.0, linestyle="k--")
plt.plot([x,x],[y,0], linewidth=2.0, linestyle="--",color="black")
"""
"2*x+1=%s" % y : 需要标注的内容
xy : 对那个坐标进行标注
xycoords : "data"表示是基于数据的值来选定位置
xytext : 标注内容的坐标位置,(+25,-15)->(x+25,y-15)
textcoords : 标书位置的描述
fontsize ： 标注内容的字体大小
arrowprops ： 对途中标注箭头的设置
"""
plt.annotate("2*x+1=%s" % y, xy=(x, y), xycoords="data",
             xytext=(+25,-15), textcoords="offset points",
             fontsize=15,arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

# 使用text()标注
plt.text(2,12,"$this\ is\ a\ text$", fontdict={"fontsize":14, "color":"red"})

# 显示图像
plt.show()

"""
解释以下参数的含义：
loc：float
    此概率分布的均值（对应着整个分布的中心centre）
scale：float
    此概率分布的标准差（对应于分布的宽度，scale越大越矮胖，scale越小，越瘦高）
size：int or tuple of ints
    输出的shape，默认为None，只输出一个值
"""
x = np.random.normal(loc=0.0, scale=1.0, size=100)
y = np.random.normal(loc=0.0, scale=1.0, size=100)
C = np.arctan2(x, y)
# x, y ： 生成点的坐标
# s : 点的大小
# alpha : 点的透明度
# c ：点的颜色
plt.scatter(x, y, s=75, alpha=0.5, c=C)
plt.show()


df = pd.DataFrame(np.arange(12).reshape((3,4)),columns=["A","B","C","D"])
plt.show(df.plot(kind="bar"))

x = np.arange(5)
# uniform : 在 0.0 ~ 1.0 之间随机生成5个数
y = np.random.uniform(low=0.0, high=1.0, size=5)

#  facecolor : 设置颜色
#  edgecolor : 设置边框颜色
plt.bar(x, y, facecolor="#9999ff", edgecolor="white")

# 标示信息
# x,y+0.01,"%.2f" % y ： 标示的坐标和值保留两位小数
# ha: horizontal alignment
# va: vertical alignment
for x,y in zip(x, y):
    plt.text(x,y+0.01,"%.2f" % y, ha="center", va="bottom")

plt.show()

def f(x, y):
    return (1 - x/2 + x**5 + y**3) * np.exp(-x**2-y**2)

n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
X, Y = np.meshgrid(x, y)

plt.contourf(X, Y, f(X, Y), 10, alpha=0.75, cmap=plt.cm.hot)

C = plt.contour(X, Y, f(X, Y), 10, colors="black", linewidth=.5)

plt.clabel(C, inline=True, fontsize=10)

plt.show()

# 未完待续......