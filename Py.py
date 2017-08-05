# -*- coding: UTF-8 -*-
import numpy as np

a = np.arange(15).reshape(3, 5)
print(a.shape)
print(a.dtype.name)
print(a.itemsize)
print(type(a))

a = np.array([1,2,3,4])    # WRONG

x = np.linspace( 0, 2 * np.pi, 100 )
print(x)
f = np.sin(x)
print(f)

c = np.arange(30)

c = c.reshape(2,3,5)
c = np.linspace(0,2,9)
c = c<10
print(c)

print("你好")

list = ['runoob', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']
del list[0]
list.remove(786)
print(list)

# list_2d = [[0 for col in range(list)] for row in range(list)]
# print(list_2d)

path = r"/doc"
print (path[1:len(path)])

sum = lambda x,y:x-y

lll = [ len(list) for seq in list]
print(111111111)
print(lll)


import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 5, 0.1);
y = np.sin(x)
plt.plot(x, y)
plt.show()
input()