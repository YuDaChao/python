# encoding: utf-8
"""
@author: YuDc
@file: pandasTest2.py
@time: 2017/6/2 16:55
@desc: 缺失值
"""

import pandas as pd
import numpy as np

s = pd.Series([
    1,3,5,7,45,
    11,23,np.nan,34,
    np.nan,23,12,34,
    11,np.nan,np.nan,34
])
# print(s)

# 输出序列中有多少Nan的值
count = sum(pd.isnull(s))
# print(count) # 4

# 直接删除缺省值
df = pd.DataFrame([
    [1,23,45,33],
    [12,34,np.nan,28],
    [32,np.nan,90,np.nan],
], columns=["A","B","C","D"])

print(df)
"""
    A     B     C     D
0   1  23.0  45.0  33.0
1  12  34.0   NaN  28.0
2  32   NaN  90.0   NaN
"""
# df = df.dropna()  # 默认情况下(axis=0, how="any")只要行中存在有nan值，该行就会被删除
"""
   A     B     C     D
0  1  23.0  45.0  33.0
"""
# df = df.dropna(axis=1, how="all") # 删除全部是nan的列
# """
#     A     B     C     D
# 0   1  23.0  45.0  33.0
# 1  12  34.0   NaN  28.0
# 2  32   NaN  90.0   NaN
# """

# df = df.drop("A", axis=1) # 删除A列
"""
      B     C     D
0  23.0  45.0  33.0
1  34.0   NaN  28.0
2   NaN  90.0   NaN
"""

# df =df.drop([0,1]) # 删除0,1两行数据
"""
    A   B     C   D
2  32 NaN  90.0 NaN
"""

# 填充缺失值
# df = df.fillna(0)  # 使用 0 来替换nan的值
"""
    A     B     C     D
0   1  23.0  45.0  33.0
1  12  34.0   0.0  28.0
2  32   0.0  90.0   0.0
"""


#采用前项填充或后项填充

# 后项填充 等价于 df.fillna(method="bfill")
# df = df.bfill()  # meth:`DataFrame.fillna(method='bfill') <DataFrame.fillna>`
"""
    A     B     C     D
0   1  23.0  45.0  33.0
1  12  34.0  90.0  28.0
2  32   NaN  90.0   NaN
"""
# 前项填充
# df = df.fillna(method="ffill")
"""
    A     B     C     D
0   1  23.0  45.0  33.0
1  12  34.0  45.0  28.0
2  32  34.0  90.0  28.0
"""

# 使用常亮填充不同列
# df = df.fillna({"A":1, "B":2, "C":3, "D":4})
"""
    A     B     C     D
0   1  23.0  45.0  33.0
1  12  34.0   3.0  28.0
2  32   2.0  90.0   4.0
"""

# 使用均值或中位数填充各自的列

A_median = df["A"].median()
B_median = df["B"].median()
C_median = df["C"].median()
D_median = df["D"].median()

print(A_median, B_median, C_median, D_median)
# 12.0 28.5 67.5 30.5

df = df.fillna({"A":A_median, "B":B_median, "C":C_median, "D":D_median})
"""
    A     B     C     D
0   1  23.0  45.0  33.0
1  12  34.0  67.5  28.0
2  32  28.5  90.0  30.5
"""

print(df)


