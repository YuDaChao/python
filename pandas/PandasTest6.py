# encoding: utf-8
"""
@author: YuDc
@file: PandasTest6.py
@time: 2017/6/3 11:30
@desc: merging
"""
import pandas as pd
import numpy as np

# df1 = pd.DataFrame({
#     "key":["k0","k1","k2","k3"],
#     "A":["A0","A1","A2","A3"],
#     "B":["B0","B1","B2","B3"]
# })
#
# df2 = pd.DataFrame({
#     "key":["k0","k1","k2","k3"],
#     "A":["A0","A1","A2","A3"],
#     "B":["B0","B1","B2","B3"],
#     "C":["C0","C1","C2","C3"]
# })
#
# print(df1)
# print(df2)

# 根据一个key合并
# res = pd.merge(df1,df2, on="key")

df1 = pd.DataFrame({
        "key1":["k10","k11","k12","k13"],
        "key2":["k20","k21","k22","k23"],
        "A":["A0","A1","A2","A3"],
        "B":["B0","B1","B2","B3"]
})

df2 = pd.DataFrame({
        "key1":["k10","k12","k13","k14",],
        "key2":["k20","k21","k22","k23"],
        "A":["A0","A1","A2","A3"],
        "B":["B0","B1","B2","B3"]
})

res = pd.merge(df1, df2, on=["key1","key2"], how="right", indicator=True)
# print(df1)
# print(df2)
# print(res)

#定义资料集并打印出
left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                     index=['K0', 'K1', 'K2'])
right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                      'D': ['D0', 'D2', 'D3']},
                     index=['K0', 'K2', 'K3'])

print(left)
print(right)

res = pd.merge(left, right, left_index=True, right_index=True, how="right")
print(res)

