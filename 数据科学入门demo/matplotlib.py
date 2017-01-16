# -*- coding: utf-8 -*-


from matplotlib import pyplot as plt

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14985.3]

# 创建一副线图,x轴年份,y轴gdp
plt.plot(years, gdp, color='green', marker='o', linestyles='solid')
# 添加一个标题
plt.title("GDP")
# 给Y轴加标记
plt.ylabel("十亿美金")
plt.show()
