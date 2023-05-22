import numpy as np

def sigmod(x):
    return 1/(1+np.exp(-x))
def sigmod_back(x):
    return x*(1-x)

# Đầu vào
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

# Đầu ra mong muốn
y = np.array([[0], [1], [1], [0]])

#he so weights khoi tao
weights = np.random.random((2,1))
#he so bias mac dinh
bias = np.random.random((1))
a = np.dot(X, weights)

# so lan lap
epochs = 10000
#he so hoc 
anpha = 0.1
# print(X.T)



for i in range(epochs):
    y_predict = sigmod(np.dot(X, weights) + bias)
    lost_function =y- y_predict 
    a = lost_function*sigmod_back(y_predict)
    d_weights = np.dot(X.T, a)
    d_bias = np.sum(a)
     
    weights += anpha*d_weights
    bias += anpha*d_bias

# In ra trọng số và bias
print("Trọng số: ", weights)
print("Bias: ", bias)

# Dự đoán đầu ra
predicted_output = sigmod(np.dot(X, weights) + bias)

# So sánh kết quả dự đoán với đầu ra mong muốn
print("Kết quả dự đoán: ")
print(predicted_output)
print("Đầu ra mong muốn: ")
print(y)
