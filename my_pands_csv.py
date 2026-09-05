# import pandas as pd

# df = pd.read_csv('整站书1000.csv')

# 预测 1：df.shape 会输出什么？
# print(df.shape) #是列表
#
# # 预测 2：df.columns 会输出什么？（列名是什么）
# print(df.columns) # 书名 价格 库存 星标 简介
#
# # 预测 3：df.dtypes 会输出什么？（哪列是数字，哪列是文字？）
# print(df.dtypes) # 除了价格都是文字，不过当时只replase了特殊字符没转float应该也是文字
#
# # 预测 4：下面这行会输出什么？
# print(df['星标数'].value_counts())# 原来是计算统计某类星标的书本有多少
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('整站书1000.csv')

# star_counts = df['星标数'].value_counts()
# print(star_counts)
# star_order = ['One', 'Two', 'Three', 'Four', 'Five']   # 想要的顺序
# star_counts = df['星标数'].value_counts().reindex(star_order)
#
#
# # 预测 1：下面这行会画出什么？（有几根柱子？顺序是什么？）
# star_counts.plot(kind='bar')
#
# plt.title('1000本书评分分布')
# plt.xlabel('评分')
# plt.ylabel('书本数量')
# plt.savefig('评分分布.png')
# plt.show()
# 预测：这行代码会输出什么？
# fx = df.groupby('星标数')['价格'].mean()
# print(fx)
# 预测：这段代码会得到什么？补全它
stock = df['库存'].str.extract(r'(\d+),expand = False').astype(int) # ,expand = False是为了返回series（列表值）而不是带表头的列表DataFrame
print(stock.head()) # 取出前五行看看效果
#     0  <-表名 有他在会多一次stock[0].mean()  没expand = False将默认以 DataFrame（多行带表头列表）输出就像本表
# 0  22
# 1  20
# 2  20
# 3  20
# 4  20

# 补全：算出平均库存（在下方写一行，用 .mean()）
# 提示：库存数字 已经是数字列了

stock_m=stock.mean()# 提示说已经是数字列，也就是说extract(r'(\d+)').astype(int)后变量stock里面存的是数字列表
# .mean()会将DataFrame转变为series
print(type(stock_m)) # Series序列相当于excel里的一行数据或一列数据吧(写expand = False之前）
print(f'平均库存：{stock_m}')  # 不写stock[0]会打印表头be like；平均库存：0    8.585

# 数每种库存有几本
# stock_how = df['库存'].value_counts()
# print(stock_how)# 平均库存有8.585是真实数据  In stock (3 available) 196。 In stock (22 available)      1
