'''
A Recurrent Neural Network (LSTM) implementation example using TensorFlow library.
This example is using the MNIST database of handwritten digits (http://yann.lecun.com/exdb/mnist/)
Long Short Term Memory paper: http://deeplearning.cs.cmu.edu/pdfs/Hochreiter97_lstm.pdf
Author: Aymeric Damien
Project: https://github.com/aymericdamien/TensorFlow-Examples/
'''

from __future__ import print_function

import tensorflow as tf
import numpy as np
from tensorflow.contrib import rnn

# Import MNIST data
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data", one_hot=True)

'''
To classify images using a recurrent neural network, we consider every image
row as a sequence of pixels. Because MNIST image shape is 28*28px, we will then
handle 28 sequences of 28 steps for every sample.
'''

# Parameters
learning_rate = 0.001
training_iters = 50000
batch_size = 128
display_step = 1000

# Network Parameters
n_input = 28  # MNIST data input (img shape: 28*28)
n_steps = 28  # timesteps
n_hidden = 128  # hidden layer num of features
n_classes = 10  # MNIST total classes (0-9 digits)

# tf Graph input
x = tf.placeholder(tf.float32, [None, n_input, n_steps])
y = tf.placeholder(tf.float32, [None, n_classes])
# Define weights
weights = {
    'out': tf.Variable(tf.random_normal([n_hidden, n_classes]))
}
biases = {
    'out': tf.Variable(tf.random_normal([n_classes]))
}

def RNN(x, weights, biases):
    # Prepare data shape to match `rnn` function requirements
    # Current data input shape: (batch_size, n_steps, n_input)
    # Required shape: 'n_steps' tensors list of shape (batch_size, n_input)

    # Unstack to get a list of 'n_steps' tensors of shape (batch_size, n_input)
    x = tf.unstack(x, axis = 1)

    # Define a lstm cell with tensorflow
    lstm_cell = rnn.BasicLSTMCell(n_hidden, forget_bias=1.0)

    # Get lstm cell output
    outputs, states = rnn.static_rnn(lstm_cell, x, dtype=tf.float32)

    # Linear activation, using rnn inner loop last output
    return tf.matmul(outputs[-1], weights['out']) + biases['out']
    # x = tf.nn.softmax(tf.matmul(outputs[-1], weights['out']) + biases['out'])
    # return x


pred = RNN(x, weights, biases)

# Define loss and optimizer
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=pred, labels=y))
optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)

# Evaluate model
correct_pred = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

# Initializing the variables
init = tf.global_variables_initializer()

train_loss_ave = tf.placeholder(tf.float32)
train_accuracy_ave = tf.placeholder(tf.float32)
test_loss_ave = tf.placeholder(tf.float32)
test_accuracy_ave = tf.placeholder(tf.float32)
log_dir = './TB_RRRNN'
tf.summary.scalar('train_loss', train_loss_ave)
tf.summary.scalar('train_accuracy', train_accuracy_ave)
tf.summary.scalar('test_loss', test_loss_ave)
tf.summary.scalar('test_accuracy', test_accuracy_ave)

merged = tf.summary.merge_all()


# Launch the graph
with tf.Session() as sess:
    sess.run(init)
    tf_board_writer = tf.summary.FileWriter(log_dir, sess.graph)
    step = 1
    # Keep training until reach max iterations
    while step * batch_size < training_iters:
        batch_x, batch_y = mnist.train.next_batch(batch_size)
        # Reshape data to get 28 seq of 28 elements
        batch_x = batch_x.reshape((batch_size, n_steps, n_input))
        # Run optimization op (backprop)
        sess.run(optimizer,{x:batch_x, y:batch_y})
        if step % display_step == 0:
            # Calculate batch accuracy
            acc, prediction = sess.run([accuracy,pred], feed_dict={x: batch_x, y: batch_y})
            print(prediction)
            # print(tf.argmax(prediction,1))
            print(np.argmax(prediction,1))
            print(batch_y)
            # print(tf.argmax(batch_y, 1))
            print(np.argmax(batch_y, 1))
            # Calculate batch loss
            loss = sess.run(cost, feed_dict={x: batch_x, y: batch_y})
            print ("Iter " + str(step*batch_size) + ", Minibatch Loss= " + \
                  "{:.6f}".format(loss) + ", Training Accuracy= " + \
                  "{:.5f}".format(acc))

            # Calculate accuracy for 128 mnist test images
            test_len = 128
            test_data = mnist.test.images[:test_len].reshape((-1, n_steps, n_input))
            test_label = mnist.test.labels[:test_len]
            test_acc, test_loss = sess.run([accuracy, pred], feed_dict={x: test_data, y: test_label})
            print("Testing Accuracy and loss:",test_acc, test_loss)

            tf_board_result = sess.run(merged,feed_dict={train_loss_ave:loss,train_accuracy_ave:acc,
                                                         test_accuracy_ave: test_acc, test_loss_ave: test_loss})
            tf_board_writer.add_summary(tf_board_result, step)

        step += 1
    print ("Optimization Finished!")

