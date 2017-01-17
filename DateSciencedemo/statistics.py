#统计学相关的代码

#当数据规模大时，要同统计来提炼和表达数据相关特征
from collections import Counter
from numpy import mean, math
from DateSciencedemo.linearAlgebra import sum_of_squares
from matplotlib import pyplot as plt

num_fridens = [100,49,41,40,25,20,56,78,23,54]

#对朋友做直方图
friden_counts = Counter(num_fridens)
xs = range(101) #最大值为100
ys = [friden_counts[x] for  x in xs]   #height 刚好是朋友的个数
plt.bar(xs,ys)
plt.bar(xs,ys)
plt.axis([0,101,0,25])
plt.title("朋友数的直方图")
plt.xlabel("朋友的个数")
plt.ylabel("个数")
plt.show()


#上面的很难交流，提炼统计量

num_points = len(num_fridens) #数据点的个数
largest_value = max(num_fridens)  #数据集最大值
smallest_value = min(num_fridens) #最小值

sorted_values = sorted(num_fridens)
smallest_value = sorted_values[0] #特定位置的值


#中位数
def median(v):
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n // 2
    if n%2 == 1:
        #如果是奇数返回中间值
        return sorted_v[midpoint]
    else:
        #如果是偶数返回中间两个值的均值
        lo = midpoint - 1
        hi = midpoint
        return (sorted_v[lo] + sorted_v[hi]) / 2
        median(num_fridens)

#分位数是泛化概念的中位数，表示少于数据中特定百分比的一个值（中位数是少于百分之五十）
def quantitle(x,p):
    p_index = int(P * len(x))
    return sorted(x)[p_index]
quantitle(num_fridens,0.10)
quantitle(num_fridens,0.25)

#众数（mode）
def mode(x):
    counts = Counter(x)
    max_count = max(counts.values())
    return [
        x_i for x_i, count in counts.iteritems()
        if  count == max_count
            ]
mode(num_fridens)

#离散度：如果它统计的值接近0，表示数据聚集一起，期中简单的度量是极差（range），最大元素与最小元素的差，另一个是方差（variance)
def data_range(x):
    return max(x) - min(x)
data_range(num_fridens)

#方差
def de_mean(x):
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]
def variance(x):
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n - 1)
variance(num_fridens)

#标准差（standard deviation）
def standard_deviation(x):
    return math.sqrt(variance(x))
standard_deviation(num_fridens)

#在均值计算中常遇到异常值，稳健的方案是计算百分之七十五的分位数和百分之25的分位数差
def interquartile_range(x):
    return quantitle(x,0.75) - quantitle(x,0.25)
interquartile_range(num_fridens)

#协方差（covariance）衡量了两个变量对均值的串联偏离程度：
def covariance(x,y):
    n = len(x)
    return dot(de_mean(x),de_mean(y)) / (n - 1)
covariance(num_fridens)

#相关，由协方差除以两个变量的标准差
def correlation(x,y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if  stdev_x > 0 and stdev_y > 0:
        return covariance(x,y) / stdev_x / stdev_y
    else:
        return 0   #如果没有变动，相关系数为零
covariance(num_fridens,daily_minutes)







