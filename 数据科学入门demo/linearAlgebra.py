import math
#一、使用列表来表示向量

#用列表解析来实现向量的相应元素想加减乘、均值
def vector_add(v,w):
    return [v_i + w_i for v_i,w_i in zip(v,w)]

def vector_subtract(v,w):
    return [v_i - w_i for v_i, w_i in zip(v, w)]

def scalar_multiply(c,v):
    #c is a number ,v is a  vector
    return [c * v_i
            for v_i in v
            ]

def vector_mean(vectors):
    n = len(vectors)
    return scalar_multiply(1/n,vector_sum(vectors))
#点乘
def dot(v,w):
    return sum(v_i * w_i
               for v_i,w_i in zip(v,w)
               )
#通过点乘求向量的平方和
def sum_of_squares(v):
    return dot(v,v)

#也可求向量的长度
def magnitude(v):
    return math.sqrt(sum_of_squares(v))

#求两点的距离
# def squared_distance(v,w):
#     return sum_of_squares(vector_subtract(v,w))
# def distance(v,w):
#     return math.sqrt(squared_distance(v,w))
def distance(v,w):
    return magnitude(vector_subtract(v,w))



#对一系列向量做加法，生成一个新向量，每次递加一个向量
def vector_sum(vectors):
    result = vectors[0]
    for vector in vectors[1:]:
        result = vector_add(result,vector)
    #return result
    return reduce(vector_add,vectors)  #更高级的实现方法
    #或者
    #vector_sum = partial(reduce,vector_add)

#二、矩阵   列表的列表

A = [[1,2,3], #A行两行三列
     [4,5,6]
     ]


