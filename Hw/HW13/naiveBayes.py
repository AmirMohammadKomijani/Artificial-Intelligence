import numpy as np
import pandas as pd
import statistics
import random





data = pd.read_csv("iris.data",sep = ",")

def findLen(name):
    cnt = 0
    for i in range(len(data)):
        if data.loc[i][4] == name:
            cnt+=1
    return cnt

randomset = set()
newLen = len(data) * 0.8
def randomChange():
    while len(randomset) < newLen:
        randomset.add(random.randint(1,149))
randomChange()
randomset = list(randomset)
for i in range(int(newLen)):
    data.loc[i] = data.loc[randomset[i]]

# print(data)

# data is changed now




setosaLen = findLen("Iris-setosa")
versicolorLen = findLen("Iris-versicolor")
virginicaLen = findLen("Iris-virginica")

setosa = np.ones((setosaLen,4))
versicolor = np.ones((versicolorLen,4))
virginica = np.ones((virginicaLen,4))



for i in range(int(newLen)):
    for k in range(setosaLen) :
        for j in range(4):
            if data.loc[i][4] == "Iris-setosa":
                setosa[k,j] = data.loc[k][j]

for i in range(int(newLen)):
    for k in range(versicolorLen) :
        for j in range(4):
            if data.loc[i][4] == "Iris-versicolor":
                versicolor[k,j] = data.loc[k][j]

for i in range(int(newLen)):
    for k in range(virginicaLen) :
        for j in range(4):
            if data.loc[i][4] == "Iris-virginica":
                virginica[k,j] = data.loc[k][j]

# print(setosa)
# print(versicolor)
# print(virginica)

# 1/ 
# we use variance for comparing and making model

var1 = [] # this is for setosa
mean1 = [] # this is for setosa
var2 = [] # this for versicolor
mean2 = [] # this for versicolor
var3 = [] # this for versicolor
mean3 = [] # this for virginica


ls = []
for i in range(4):
    for j in range(setosaLen):
        ls.append(setosa[j,i])
    var1.append(statistics.variance(ls))
    mean1.append(statistics.mean(ls))
    ls = []

for i in range(4):
    for j in range(versicolorLen):
        ls.append(versicolor[j,i])
    var2.append(statistics.variance(ls))
    mean2.append(statistics.mean(ls))
    ls = []

for i in range(4):
    for j in range(virginicaLen):
        ls.append(virginica[j,i])
    var3.append(statistics.variance(ls))
    mean3.append(statistics.mean(ls))    
    ls = []


print(var1)
print(mean1)
# # print(var2)
# # print(var3)


# 2/ changing numbers
changing = []
for i in range(4):
    changing.append(mean1[i] - var1[i]*mean1[i])
#print(changing)

for i in range(setosaLen):
    for j in range(4):
        setosa[i,j] += changing[j]

var1 = [] # this is for setosa
mean1 = [] # this is for setosa
ls = []
for i in range(4):
    for j in range(setosaLen):
        ls.append(setosa[j,i])
    var1.append(statistics.variance(ls))
    mean1.append(statistics.mean(ls))
    
print(var1)
print(mean1)








