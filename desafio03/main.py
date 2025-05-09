#####################################
#### SUA AREA DE TRABALHO ABAIXO ####
#####################################

rate = 1
usebias = False
batches = 1

def predict_one(X, pesos, usebias):
    return 0

def transform(x):
    return x

#####################################
#### FIM DA SUA AREA DE TRABALHO ####
#####################################

from math import exp
def gauss(x, u, s):
    return exp(-(x - u) * (x - u) / s)

def variation(X, Y, pesos, usebias):
    derivatives = [ 0 ] * len(pesos)

    for i in range(len(X)):
        predict = predict_one(X[i], pesos, usebias)
        error = predict - Y[i]
        for j in range(len(derivatives) - 1):
            derivatives[j] += error * X[i][j]
        if usebias:
            derivatives[-1] += error
    
    return [d / len(X) for d in derivatives]

def read():
    X = []
    Y = []
    with open("bike_sharing.csv", "r", encoding="utf-8") as file:
        next(file)
        for line in file:
            columns = line.strip().split(",")
            X.append([int(s) for s in columns[0:4]])
            Y.append(int(columns[4]))
    
    return (X, Y)

def predict(X, pesos, usebias):
    return [ predict_one(x, pesos, usebias) for x in X ]

def error(X, Y, pesos, usebias):
    P = predict(X, pesos, usebias)
    total = 0
    for y, p in zip(Y, P):
        diff = y - p
        total += diff if diff > 0 else -diff
    return total / len(Y)

def train(X, Y, pesos, usebias, rate):
    var = variation(X, Y, pesos, usebias)
    for i in range(len(pesos)):
        pesos[i] -= var[i] * rate

X, Y = read()
for i in range(len(X)):
    X[i] = transform(X[i])
pesos = [ 0 ] * (len(X[0]) + (1 if usebias else 0))

batchsize = int(len(X) / batches)
print(f"Initial error = {error(X, Y, pesos, usebias)}")
for i in range(100):
    for k in range(batches):
        train(X[k*batchsize:(k+1)*batchsize], Y[k*batchsize:(k+1)*batchsize], pesos, usebias, rate)
    print(f"Epoch: {i + 1}, error = {error(X, Y, pesos, usebias)}")