# books-analysis

用 pandas + matplotlib 分析 books.toscrape.com 全站 1000 本书的数据
（书名、价格、库存、评分、简介）。

## 分析结论

- 平均价格 35.07 英镑，最高 59.99，最低 10.00
- 价格分布均匀，无集中区间（教学站随机定价）
- 评分与价格无关：五星书均价 35.37，一星书均价 34.56，差距不足 2 英镑
- 库存悬殊：196 本书仅 3 本库存；22 本库存的全站只有 1 本（均值 8.585 被低库存拉低）

## 可视化

![价格分布图](价格分布.png)

## 技术栈

- Python 3
- pandas
- matplotlib

## 运行

python 你的分析代码文件名.py

## 数据来源

books.toscrape.com（教学练习站），由爬虫仓库
[books-spider](https://github.com/yanhuang166/books-spider) 采集
