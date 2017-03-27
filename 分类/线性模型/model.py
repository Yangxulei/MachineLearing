
from scipy.ndimage import standard_deviation, mean
from scipy.spatial.distance import correlation
#yi = βxi + α + ɛi
#我们假设y是用户i每天花在网站上的分钟数，xi是用户i已有的朋友数，而ɛi是误差项，我们求出alpha和beta就可以进行预测了

#预测



def predict(alpha,beta,x_i):
    return beta * x_i + alpha

#计算误差
def error(alpha,beta,x_i,y_i):
    return y_i - predict(alpha,beta,x_i)

#单纯吧各个误差加起来不是很合理，因为有的预测太高，有的太低，相加会抵消，因此求误差的平方和
def sum_of_squared_errors(alpha,beta,x,y):
    return sum(error(alpha,beta,x_i,y_i)**2
               for x_i, y_i in zip(x,y))

#也可利用最小二乘法选择alpha和beta，使得sum_of_squared_errors 尽可能小

#利用微积分求：
def least_squares_fit(x,y):
    beta = correlation(x,y) * standard_deviation(y) / standard_deviation(x)
    alpha = mean(y) - beta* mean(x)
    return alpha,beta



#用决定系数(coefficient of determination)R^2 这一指标来评估模型对数据的拟合效果
def total_sum_of_squares(y):
    return sum(v**2 for v in  de_mean(y))
def r_squared(alpha,beta,x,y):
    return 1.0 - (sum_of_squared_errors(alpha,beta,x,y) / total_sum_of_squares(y))

#利用梯度下降法：

theta = [alpha,beta]

def squared_error(x_i,y_i,theata):
    alpha,beta = theta
    return error(alpha,beta,x_i,y_i) ** 2

def squared_error_gradient(x_i,y_i,theta):
    alpha, beta = theta
    return [-2*error(alpha,beta,x_i,y_i),  #alpha偏导数
            -2*error(alpha,beta,x_i,y_i)*x_i] #beta偏导数

