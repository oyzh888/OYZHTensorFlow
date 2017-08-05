import numpy as np

# sigmoid function
def nonlin(x,deriv=False):
    if(deriv==True):
        return x*(1-x)
    return 1/(1+np.exp(-x))
    
# input dataset
X = np.array([  [0,0,1],
                [0,1,1],
                [1,0,1],
                [1,1,1] ])
    
# output dataset            
y = np.array([[0,0,1,1]]).T

# seed random numbers to make calculation
# deterministic (just a good practice)
np.random.seed(1)

# initialize weights randomly with mean 0
syn0 = 2*np.random.random((3,1)) - 1

for iter in xrange(10000):

    # forward propagation
    l0 = X
    l1 = nonlin(np.dot(l0,syn0))

    # how much did we miss?
    l1_error = y - l1

    # multiply how much we missed by the 
    # slope of the sigmoid at the values in l1
    l1_delta = l1_error * nonlin(l1,True)

    # update weights
    syn0 += np.dot(l0.T,l1_delta)
    if(iter%1000 == 0):
		print(syn0)


print "Output After Training:"
print l1

l = [1,2,3,4,5]
print(l[0:2])


# fileName = "C:\\Users\\v-zhou\\simple-examples\\data\\ptb.train.txt"
# res = os.path.isdir(r"C:\Users\v-zhou\PycharmProjects\OYZHTensorFlow\TensorFlowLearn")
# print(res)
# print(os.getcwd())
# file = open(r"C:/Users/v-zhou/simple-examples/data/ptb.train.txt",'r')
#
# print(file.readline())
#
# str = "aasd||456%%1das"
# str2 = str.split("%%")
# print (str)
# print(str.find("456"))
#
# for element in str2:
#     print(element)