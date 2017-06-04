# encoding: utf-8
"""
@author: YuDc
@file: PandasTest4.py
@time: 2017/6/2 19:44
@desc: 读写文件
"""
import pandas as pd

# data = pd.read_csv("F:/test.csv")
# 读取json格式文件
data = pd.read_json("test.json")
print(data)
# 写文件
data.to_pickle("test.pickle")




