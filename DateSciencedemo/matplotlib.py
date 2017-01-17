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

#简单的条形图
movies = ["Annie Hall","Ben-Hur","Casablanca","Gandhi","West Side Story"]
num_oscars = [5,11,3,8,10]

#条形的默认宽度是0.8，因此在左侧坐标加上0.1
xs = [i + 0.1 for i, _ in enumerate(movies)]

#使用左侧xs坐标【xs】和高度【num_oscars】画条形图
plt.bar(xs,num_oscars)

plt.ylabel("我所获奥斯卡金像奖数量")
plt.title("我最喜欢的电影")

#使用电影的名字标记X轴，位置在x轴上条形的中心
plt.xticks([i + 0.5 for i, _ in enumerate(movies)],movies)
plt.show()