# encoding: utf-8
"""
@author: YuDc

@file: PandasTest.py

@time: 2017/6/1 20:37

@desc:
"""

import pandas as pd
import numpy as np


# index 定义行的名称，默认为0~n
s = pd.Series([1,3,5,54,np.nan,9], index=[1,3,5,7,9,11])
"""
0     1.0
1     3.0
2     5.0
3    54.0
4     NaN
5     9.0
dtype: float64
"""
# print(s)
# print(s[1])

dates = pd.date_range("20170101",periods=10)
"""
DatetimeIndex(['2017-01-01', '2017-01-02', '2017-01-03', '2017-01-04',
               '2017-01-05', '2017-01-06', '2017-01-07', '2017-01-08',
               '2017-01-09', '2017-01-10'],
              dtype='datetime64[ns]', freq='D')

"""
# print(dates)

df = pd.DataFrame(np.arange(20).reshape((5,4)),index=pd.date_range("20170101", periods=5),columns=['A','B','C','D'])
"""
             A   B   C   D
2017-01-01   0   1   2   3
2017-01-02   4   5   6   7
2017-01-03   8   9  10  11
2017-01-04  12  13  14  15
2017-01-05  16  17  18  19
"""
# print(df)

df2 = pd.DataFrame({
    'A':[i for i in range(4)],
    'B':pd.Timestamp('20170102'),
    'C':pd.Series([i for i in range(4)],index=[0,1,2,3],dtype='float32'),
    'D':pd.Categorical(["test","train","test","train"])
    # 'E':pd.Categorical(["test","train","test","train"]),
    # 'F':'foo'
})
# print(df2)
"""
         A    C    D
count  4.0  4.0  4.0
mean   1.0  1.0  3.0
std    0.0  0.0  0.0
min    1.0  1.0  3.0
25%    1.0  1.0  3.0
50%    1.0  1.0  3.0
75%    1.0  1.0  3.0
max    1.0  1.0  3.0
"""
# 会忽略非数字的列
# print(df.describe())

# 对索引名称排序
# axis = 1 表示对列排序
# sacending = False 表示降序， 默认为True
# print(df.sort_index(axis=1, ascending=False))

# 对值进行排序
print(df.sort_values(by="D",ascending=False))
"""
             A   B   C   D
2017-01-05  16  17  18  19
2017-01-04  12  13  14  15
2017-01-03   8   9  10  11
2017-01-02   4   5   6   7
2017-01-01   0   1   2   3

"""

print(sum(pd.isnull(s)))
# print(df)
# select by label : loc 通过标签名筛选
#print(df.loc[[0,1,2,3],['A','B']]) # 打印0到1行数据的A，B两列
# print(df2.loc[0][1])  # 打印第0行数据
# print(df.loc[["20170101","20170102"],["A","B"]]) # KeyError: "None of [['20170101', '20170102']] are in the [index]"
# print(df.loc[:,['A','B']])
"""
A    0
B    1
Name: 2017-01-01 00:00:00, dtype: int32
"""
"""
A    0
B    1
C    2
D    3
Name: 2017-01-01 00:00:00, dtype: int32
"""
# print(df.loc["20170102"]["A"])

# print(df.loc[["20170101"],['A','B']])
# select by position : iloc 通过索引筛选
#print(df2.iloc[1:3,1:3]) # 筛选1到3行(不包含第三行),1到3列(不包含第三列)的数据

# print(df.iloc[1:3,1:3])

# mixed selection : ix  混合筛选
print(df.ix[:2,["A","C"]]) # 筛选前2行(不包含末尾),A列，B列数据
"""
            A  C
2017-01-01  0  2
2017-01-02  4  6
"""
# Boolean indexing

# print(df2[df2.A>=1])

# print(df2['A'])
# print(df2[["A","B"]])
