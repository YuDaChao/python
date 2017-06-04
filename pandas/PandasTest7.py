# encoding: utf-8
"""
@author: YuDc
@file: PandasTest7.py
@time: 2017/6/3 15:37
@desc:
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# 使用 pd 产生一个序列

s = pd.Series(np.random.randn(1000), index=np.arange(1000))

# 默认打印前五个数
# print(s.head())

# 累加数据
# s.cumsum()

# pandas数据可以直接观看可视化数据
# s.plot()

# plt.show()

data = pd.DataFrame(
    np.random.randn(100,4),
    index=np.arange(100),
    columns=list("ABCD")
    )
# data.cumsum()
# data.plot()
# plt.show()

# 散点图
# ax = data.plot.scatter(x="A", y="B", color="DarkBlue", label="Class 1")
#
# data.plot.scatter(x="C", y="D", color="LightGreen", label="Class 2", ax=ax)
#
# plt.show()

# labels='frogs','hogs','dogs','logs'
# sizes=15,20,40,25
# colors='yellowgreen','gold','lightskyblue','lightcoral'
# explode=0,0.1,0,0

# 饼状图
# size 饼图每部分显示的大小
# explode : 突出显示那一部分
# labels : 需要显示的标签
# colors ：显示内容的颜色
# autopct ：显示数据保留的小数
# shadow ：显示阴影效果
# plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,startangle=80)
# plt.axis('equal')
# plt.show()



