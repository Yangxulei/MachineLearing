import  numpy as np
import  pandas as pd
import  keras
import tensorflow as tf
import  matplotlib.pyplot as plt



from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('MNIST_data',validation_size=0)

img = mnist.train.images[2]
plt.imshow(img.reshape((28,28)),cmap='Greys_r')
plt.show()

encoding_dim = 32

image_size = mnist.train.images.shape[1]

#input and target placeholders
inputs_ = tf.placeholder(tf.float32,(None,image_size),name='inputs')
targets_ = tf.placeholder(tf.float32,(None,image_size),name='targets')

#output of hidden layer, single fully connected layer here with ReLU activation
encoded = tf.layers.dense(inputs_,encoding_dim,activation=tf.nn.relu)

#output layer logits,fully connected layer with no activation
logits = tf.layers.dense(encoded,image_size,activation=None)

#sigmoid output from logits
decoded = tf.nn.sigmoid(logits,name='output')

#sigmoid cross-entropy loss
loss = tf.nn.sigmoid_cross_entropy_with_logits(labels=targets_,logits=logits)
#mean of the loss

cost = tf.reduce_mean(loss)

#adam optimizer
#通过使用动量（参数的平均移动数）来改善传统梯度下降，促进超参数动态调整
opt = tf.train.AdamOptimizer(0.001).minimize(cost)

sess = tf.Session()

epochs = 20
batch_size = 200
sess.run(tf.global_variables_initializer())
for e in range(epochs):
    for ii in range(mnist.train.num_examples//batch_size):
        batch = mnist.train.num_batch(batch_size)
        feed = {inputs_:batch[0],targets_:batch[0]}
        batch_cost, _ = sess.run([cost,opt],feed_dict=feed)

        print("Epoch:{}/{}..".format(e+1,epochs),
              "Training loss:{:.4f}".format(batch_cost))



