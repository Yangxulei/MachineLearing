from numpy import*
import operator
import matplotlib
def creatDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group,labels

#以下函数主要是使用欧氏距离公式,计算两个向量点之间的距离,如果数据集存在n个特征值就用相应的法则计算

def classify0(inX,dataSet,labels,k): #inX用于分类的输入向量,dataSet:输入的训练样本集,labels:标签向量,k:用于选择最近邻居的数目
    #距离计算
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX,(dataSetSize,1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()

    #选择距离最小的K个点
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1

    #排序
    sortedClassCount = sorted(classCount.iteritems(),
                              key = operator.itemgetter(1),
                              reverse = True
                              )

    return sortedClassCount[0][0]

    #Test
    #test =  kNN.classify0([0,0],group,labels,3)
    #print(test)

#将文本记录转换为Numpy的解析程序
def file2matrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines) #得到文件行数
    returnMat = zeros((numberOfLines,3)) #创建返回的NumPy矩阵
    classLabelVector = []
    index = 0
    for line in arrayOLines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]  #解析文件数据到列表
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat.classLabelVector
    #Test
    #datingDataMat,datingLabels = kNN.file2matrix('datingTestSet.txt')





