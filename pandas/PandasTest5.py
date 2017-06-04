# encoding: utf-8
"""
@author: YuDc
@file: PandasTest5.py
@time: 2017/6/3 10:34
@desc: pandas合并
"""
import pandas as pd
import numpy as np

# df1 = pd.DataFrame(np.ones((3,4)) * 0, columns=["A","B","C","D"])
# df2 = pd.DataFrame(np.ones((3,4)) * 1, columns=["A","B","C","D"])
# df3 = pd.DataFrame(np.ones((3,4)) * 2, columns=["A","B","C","D"])

# 上下合并
# res = pd.concat([df1,df2,df3], axis=0)

# 观察下面的结果，我们发现它的行的索引是 0 1 2 0 1 2
# 如果我们需要让他是有序的呢？我们可以使用 ignore_index=True
# res = pd.concat([df1,df2,df3], axis=0, ignore_index=True)
"""
     A    B    C    D
0  0.0  0.0  0.0  0.0
1  0.0  0.0  0.0  0.0
2  0.0  0.0  0.0  0.0
0  1.0  1.0  1.0  1.0
1  1.0  1.0  1.0  1.0
2  1.0  1.0  1.0  1.0
0  2.0  2.0  2.0  2.0
1  2.0  2.0  2.0  2.0
2  2.0  2.0  2.0  2.0
"""

# print(res)


# df1 = pd.DataFrame(np.ones((3,4)) * 0, columns=["A","B","C","D"], index=[1,3,5])
# df2 = pd.DataFrame(np.ones((3,4)) * 2, columns=["B","C","D","E"], index=[0,3,5])
# print(df1)
# print(df2)
#
# res = pd.concat([df1,df2], join="outer", axis=0, ignore_index=True)
# 如果以默认的join="outer"合并, 那么对于不同列会用NaN来补充
# 如果是join=inner，那么只会合并共有部分
"""
     A    B    C    D    E
1  0.0  0.0  0.0  0.0  NaN
3  0.0  0.0  0.0  0.0  NaN
5  0.0  0.0  0.0  0.0  NaN
0  NaN  2.0  2.0  2.0  2.0
3  NaN  2.0  2.0  2.0  2.0
5  NaN  2.0  2.0  2.0  2.0
--------------------------
     B    C    D
0  0.0  0.0  0.0
1  0.0  0.0  0.0
2  0.0  0.0  0.0
3  2.0  2.0  2.0
4  2.0  2.0  2.0
5  2.0  2.0  2.0
"""
# print(res)


df1 = pd.DataFrame(np.ones((3,4)) * 0, columns=["A","B","C","D"], index=[1,3,5])
df2 = pd.DataFrame(np.ones((3,4)) * 2, columns=["B","C","D","E"], index=[0,3,5])

res = df1.append(df2,ignore_index=True)
print(res)