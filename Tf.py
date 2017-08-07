# import tensorflow as tf
#
# n_steps = 10
# sess = tf.Session()
#
# arr = tf.constant([[1,2,3],[4,5,6]])
# res = tf.unstack(arr, axis = 1)
# sess.run(res)
list = [ [['runoob'], [786], [2.23]],[[111],[222],[333],[444]]]
print(list)

# import tensorflow as tf
# a = tf.constant([1,2,3])
# b = tf.constant([4,5,6])
# c = tf.stack([a,b],axis=1)
# d = tf.unstack(c,3,axis=0)
# e = tf.unstack(c,2,axis=1)
# print(c.get_shape())
# with tf.Session() as sess:
#     print(sess.run(c))
#     print(sess.run(d))
#     print(sess.run(e))