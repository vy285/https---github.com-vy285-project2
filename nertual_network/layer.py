import numpy as np

x = np.array([
    [0,1],
    [1,1],
    [2,1]
])
y=  np.random.rand(2,4) 
z=  np.random.rand(4,1)
a = np.dot(x,y)
print(a.shape)
print(a)
b= np.dot(a,z)
print(b.shape)
print(b)
# print(([0,1]+[1,1]+[2,1])*[1])