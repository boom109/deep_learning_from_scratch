## 1.3.1 arithmetic operation
print(1 - 2)
print(4 * 5)
print(7 / 5)
print(3 ** 2)


## 1.3.2 Data type
print(type(10))
print(type(2.718))
print(type("hello"))


## 1.3.3 Variable
x = 10
print(x)

x = 100
print(x)

y = 3.14
print(x * y)
print(type(x * y))


## 1.3.4 List
a = [1, 2, 3, 4, 5]
print(a)
print(len(a))
print(a[0])
print(a[4])
a[4] = 99
print(a)
print(a[0:2])
print(a[1:])
print(a[:3])
print(a[:-1])
print(a[:-2])


## 1.3.5 Dictionary
me = {'height':180}
print(me['height'])
me['weight'] = 70
print(me)


## 1.3.6 bool
hungry = True
sleepy = False
print(type(hungry))
print(not hungry)
print(hungry and sleepy)
print(hungry or sleepy)


## 1.3.7 if statement
hungry = True
if hungry:
    print("I'm hungry")

hungry = False
if hungry:
    print("I'm hungry")
else:
    print("I'm not hungry")
    print("I'm sleepy")


## 1.3.8 for statement
for i in [1,2,3]:
    print(i)


## 1.3.9 function
def hello():
    print("Hello World!")

hello()

def hello(object):
    print("Hello " + object + "!")

hello("cat")


## 1.5.x
import numpy as np

## 1.5.2 create array in numpy
x = np.array([1.0, 2.0, 3.0])
print(x)
print(type(x))

## 1.5.3 operation in numpy
x = np.array([1.0, 2.0, 3.0])
y = np.array([2.0, 4.0, 6.0])
print(x + y)
print(x - y)
print(x * y)
print(x / y)

x = np.array([1.0, 2.0, 3.0])
print(x / 2.0)


## 1.5.4 N-dimension array in numpy
A = np.array([[1, 2], [3, 4]])
print(A)
print(A.shape)
print(A.dtype)

B = np.array([[3, 0], [0, 6]])
print(A + B)
print(A * B)

print(A)
print(A * 10)


## 1.5.5 broadcast
A = np.array([[1, 2], [3, 4]])
B = np.array([10, 20])
print(A * B)


## 1.5.6 access elements
X = np.array([[51, 55], [14, 19], [0, 4]])
print(X)
print(X[0])
print(X[0][1])

for row in X:
    print(row)

X = X.flatten()
print(X)
print(X[np.array([0, 2, 4])])

print(X > 15)
print(X[X>15])

