# encoding: utf-8
"""
@author: YuDc
@file: PandasTest8.py
@time: 2017/6/3 16:12
@desc:
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# -----------------------------------------------------------
#                          线形图 1
# -----------------------------------------------------------

# 创建数据
# Series和DataFrame都有一个用于生成各类图标的plot方法，默认情况下，
# 他们所生成的是线型图，该Series的索引会被传给matplotlib，并用于绘制x轴
# data = pd.Series(np.random.random(10), index=np.arange(10))

# DataFrame的plot方法会在一个subplot中为各列绘制一条直线，并自动创建图例：
# data = pd.DataFrame(np.random.randn(10,4), columns=list("ABCD"), index=np.arange(10))

# 为了显示好看，我们将数据进行累加
# data.cumsum()
#
# p = data.plot()
#
# plt.show(p)

# -----------------------------------------------------------
#                          线形图 2
# -----------------------------------------------------------

# 在-3 和 3 之间生成50个数
x = np.linspace(-3,3,50)
y1 = 3*x + 3
y2 = x**2 +1

# 创建一个figure, 名称为 figure 2   大小为10, 10
plt.figure(num=2, figsize=(5,5))

# 切记 line1 line2一定要加上 ","
line1, = plt.plot(x, y1, label="up")
line2, = plt.plot(x, y2, color="red", linewidth=1.0, linestyle="--", label="down")

"""
    当设置labels时， 上面定义的label="up", label="down"就会被下面的labels覆盖
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
plt.legend(handles=[line1, line2], labels=["AAA","BBB"], loc="best")

# 设置x轴y轴的区间限定
# plt.xlim((-1,2))
# plt.ylim((-2,2))
# 设置x,y轴的描述
plt.xlabel("i am x")
plt.ylabel("i am y")

# 修改x，y轴的单位长度
# new_ticks = np.linspace(-1,2,5)
# plt.xticks(new_ticks)
# plt.yticks([-2,-1.8,-1,1.22,3],
#            ["really bad","bad","normal","good","really good"])


# 获取当前的坐标轴 get current axis
ax = plt.gca()

# 去除右边和上边的轴
ax.spines["right"].set_color("none")
ax.spines["top"].set_color("none")

ax.xaxis.set_ticks_position("bottom")
ax.yaxis.set_ticks_position("left")
# 将x轴的位置设置到y轴的 0 位置
ax.spines["bottom"].set_position(("data",0))
# 将y轴的位置设置到x轴的 0 位置
ax.spines["left"].set_position(("data",0))

# 设置tick能见度
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(12)
    label.set_bbox(dict(facecolor='green', edgecolor='None', alpha=.7))

#    设置标注
x0 = 1
y0 = 3*x0 + 3

# 设置一个点
# s : 表示点的大小(size)
# color : 颜色 "b"-->"blue"
plt.scatter(x0, y0, s=30, color="b")

# 画线(两点确定一条直线)
# (1,6),(1,0)
# "k--" : k 表示颜色是黑色 "--" 表示虚线
plt.plot([x0,x0],[y0,0],"k--")

# 显示标注
# 'r"$2x+1=%s$" % y0' : 表示需要显示标注
# xy : 表示显示标注的坐标位置
# xycoords : 表示以坐标xy为基准
# xytext : 表示标注的位置是基于(x,y)横坐标+20， 纵坐标-20
# arrowprops : 设置箭头
# connectionstyle ： 箭头的样式
plt.annotate(r"$2x+1=%s$" % y0, xy=(x0,y0), xycoords="data",
             xytext=(+20,-20), textcoords="offset points",
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

plt.text(1,3,r"$This\ is\ the\ some\ text.\ \mu\ \sigma_i\ \alpha_t$")

plt.show()



# -----------------------------------------------------------
#                          柱状图
# -----------------------------------------------------------

# 在生成的线型图的代码中加上kind='bar'(垂直树状图) 此时，Series和DataFrame的索引将会被用作X或Y的刻度。

# 定义DataFrame对象
# df = pd.DataFrame(np.random.rand(6,4), index=np.arange(1,7), columns=["A","B","C","D"])
# print(df)
"""
          A         B         C         D
1  0.497904  0.328244  0.645223  0.678750
2  0.315770  0.544352  0.894848  0.995442
3  0.755586  0.127364  0.269211  0.640939
4  0.209429  0.300002  0.909044  0.564771
5  0.901727  0.090296  0.569479  0.603802
6  0.020938  0.331144  0.586158  0.723000
"""
# plt.show(df.plot(kind="bar"))



# -----------------------------------------------------------
#                          散点图
# -----------------------------------------------------------

X = np.random.normal(0,1,100)
Y = np.random.normal(0,1,100)
T = np.arctan2(Y, X)
plt.scatter(X, Y, s=75, c=T, alpha=.5)

# 什么也不给就是去除x， y的刻度
plt.xticks(())
plt.yticks(())
plt.show()

# -----------------------------------------------------------
#                          柱状图
# -----------------------------------------------------------


X = np.arange(12)
Y = (1 - X/float(12)) * np.random.uniform(0.5, 1.0, 12)
# print(Y1)

# 设置柱状图的颜色
plt.bar(X, Y, facecolor="#9999ff", edgecolor="white")

# 去除上，you边框
ax = plt.gca()
ax.spines["top"].set_color("none")
ax.spines["right"].set_color("none")

for x, y in zip(X, Y):
    plt.text(x, y +0.01, "%.2f" % y, ha="center", va="bottom")

plt.show()


# -----------------------------------------------------------
#                          等高线
# -----------------------------------------------------------

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























