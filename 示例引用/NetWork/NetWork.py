import random
import  numpy as np
class NetWork(object):
    def __index__(self,sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y,1) for y in sizes[1:]]
        self.weights = [np.random.randn(y,x) for x , y in zip(sizes[: -1],sizes[1:])]
    def feedforward(self,a):
        #return the ouput of the newwork if 'a' is input
        for b,w in zip(self.biases, self.weights):
            a = sigmoid(np.dot(w,a) + b)
        return a
    def SGD(self,training_data, epochs, mini_batch_size,eta, test_data=None):
        """
        :param training_data:  a list of tuples (x,y) representing the training inputs and desired outputs
        :param epochs:   
        :param mini_batch_size: 
        :param eta: 
        :param test_data: is provied then the network will be evaluated against the test data afer each epoch and partial progress printed out
        :return: 
        """
        if test_data: n_test = len(test_data)
        n = len(training_data)
        for j in xrange(epochs):
            random.shuffle(training_data)
        if test_data:
            print "Epoch{0}:{1}/{2}".format(j,self.evaluate(test_data),n_test)
        else:
            print "Epoch{0} complete".format(j)






        return

def sigmoid(z):
        return  1.0/(1.0 + np.exp(-z))
