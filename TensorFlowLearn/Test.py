import sys

def hello():
    hello2()
    print("Hello")

def hello2():
    print(2)

if sys.argv[1]!= None:
    print sys.argv[1]
    hello()



