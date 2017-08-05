import numpy as np
import tensorflow as tf

x = tf.Variable(tf.zeros([5]), dtype=tf.float32)
c = tf.constant( [ [1,2,3,4,5],[11,22,33,44,55],[12,23,34,45,56] ])

emb = tf.nn.embedding_lookup(c,[1],partition_strategy='mod')


sess = tf.InteractiveSession()
tf.global_variables_initializer().run()

res = sess.run(emb)
print(res)


x =tf.constant([[True,True,True,True],
     [False,False,True,False]])
yy = tf.reduce_all(x,0)
res = sess.run(yy)
print(res)





matrix = np.random.random([1024, 1])  # 64-dimensional embeddings
print(type(matrix))
ids = np.array([0, 5, 17, 33])
print (matrix[ids])  # prints a matrix of shape [4, 64]

# tf.nn.embedding_lookup(a,[0,1]).eval()
