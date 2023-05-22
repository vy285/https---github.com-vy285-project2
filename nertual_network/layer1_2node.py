import numpy as np
def sigmod(x):
    return 1/(1+np.exp(-x))
def sigmod_back(x):
    return x*(1-x)

# Đầu vào
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

# Đầu ra mong muốn
y = np.array([[0], [1], [1], [0]])

echops   = 10000
apha = 0.1

w1 = np.random.random((2,2))
b1 = np.random.random((1))

w2= np.random. random((2,1))
b2 = np.random.random((1))

for i in range(echops):
    f1 = sigmod(np.dot(X,w1) + b1)
    f2 = sigmod(np.dot(f1,w2) + b2)
    
    loss = y- f2
    chung2 = loss*1*1*sigmod_back(f2)
    denta_w2 = np.dot(f1.T,chung2)
    denta_b2 = np.sum(chung2)
    
    chung1 = np.dot(chung2,w2.T)*sigmod_back(f1)
    denta_w1 = np.dot(X.T,chung1)
    denta_b1 = np.sum(chung1)

    w2 += apha*denta_w2
    b2 += apha*denta_b2
    w1 += apha*denta_w1
    b1 += apha*denta_b1
    
f1 = sigmod(np.dot(X,w1) + b1)
f2 = sigmod(np.dot(f1,w2) + b2)
print(f2)
