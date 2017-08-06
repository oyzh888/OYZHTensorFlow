# import tensorflow as tf
#
# input = [1,2,3,4,5,6,7,8,9,10]
# output = input
# outputSize = range(output)
# batch_size = 5
#
#
# softmax_b = tf.Variable([outputSize],dtype=tf.ffloat32)
# softmax_w = tf.Variable([batch_size, batch_size],dtype=tf.ffloat32)
#
# lstm_size = range(input)
# lstm = tf.contrib.rnn.BasicLSTMCell(lstm_size)
# # Initial state of the LSTM memory.
# state = tf.zeros([batch_size, lstm.state_size])
# probabilities = []
# loss = 0.0
#
# sess = tf.InteractiveSession()
# tf.global_variables_initializer().run()
#
# def loss_function(probabilities, target_words):
#     return tf.reduce_mean(-tf.reduce_sum((target_words * tf.log(probabilities)), reduction_indices=1)
#
# # Train
# def loopFunc():
#     i = 0
#     while(i<range(input)):
#         current_batch = input[i:i+batch_size]
#         target_words = output[i:i+batch_size]
#         # The value of state is updated after processing each batch of words.
#         output, state = lstm(current_batch, state)
#
#         # The LSTM output can be used to make next word predictions
#         logits = tf.matmul(output, softmax_w) + softmax_b
#         probabilities.append(tf.nn.softmax(logits))
#         loss += loss_function(probabilities, target_words)
#
