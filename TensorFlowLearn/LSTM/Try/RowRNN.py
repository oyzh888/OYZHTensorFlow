import tensorflow as tf

input = [1,2,3,4,5,6,7,8,9,10]
output = input
inputSize = range(input)
outputSize = range(output)
lstm_size = 20


softmax_b1 = tf.Variable([lstm_size],dtype=tf.float32)
softmax_w1 = tf.Variable([1,lstm_size],dtype=tf.float32)

softmax_b2 = tf.Variable([outputSize],dtype=tf.float32)
softmax_w2 = tf.Variable([outputSize,lstm_size],dtype=tf.float32)

inputFunc = tf.sparse_softmax(tf.matmul(input,softmax_w1) + softmax_b1)
outputFunc = tf.matmul(input,softmax_w2) + softmax_b2


lstm = tf.contrib.rnn.BasicLSTMCell(lstm_size)
# Initial state of the LSTM memory.
state = tf.zeros([batch_size, lstm.state_size])
probabilities = []
loss = 0.0
for _ in range(1000):
    # The value of state is updated after processing each batch of words.
    output, state = lstm(current_batch_of_words, state)

    # The LSTM output can be used to make next word predictions
    logits = tf.matmul(output, softmax_w) + softmax_b
    probabilities.append(tf.nn.softmax(logits))
    loss += loss_function(probabilities, target_words)