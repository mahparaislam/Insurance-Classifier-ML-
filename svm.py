import csv
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

test=[]
title=[]
train=[]
train_title=[]


    
def read_csv(filename):
    f=csv.reader(open(filename, 'r'))
    global test
    global title
    for i in f:
        test.append(i)
    title = test[0]
    for i in range(1,len(test)):
        if(test[i][1]=="Female"):
            test[i][1]=float(0)
        else:
            test[i][1]=float(1)
    for i in range(1,len(test)):
        for j in range(2,6):
            test[i][j]=float(test[i][j])
    for i in range(1,len(test)):
        if(test[i][6]=="< 1 Year"):
            test[i][6]=float(0)
        elif(test[i][6]=="1-2 Year"):
            test[i][6]=float(1)  
        elif(test[i][6]=="> 2 Years"):
            test[i][6]=float(2)
    for i in range(1,len(test)):
        if(test[i][7]=="Yes"):
            test[i][7]=float(1)
        elif(test[i][7]=="No"):
            test[i][7]=float(0) 
    for i in range(1,len(test)):
        for j in range(8,11):
            test[i][j]=float(test[i][j])
    test=test[1:]
    
def read_traincsv(filename):
    f=csv.reader(open(filename, 'r'))
    global train
    global train_title
    for i in f:
        train.append(i)
    train_title = train[0]
    for i in range(1,len(train)):
        if(train[i][1]=="Female"):
            train[i][1]=float(0)
        else:
            train[i][1]=float(1)
    for i in range(1,len(train)):
        for j in range(2,6):
            train[i][j]=float(train[i][j])
    for i in range(1,len(train)):
        if(train[i][6]=="< 1 Year"):
            train[i][6]=float(0)
        elif(train[i][6]=="1-2 Year"):
            train[i][6]=float(1)  
        elif(train[i][6]=="> 2 Years"):
            train[i][6]=float(2)
    for i in range(1,len(train)):
        if(train[i][7]=="Yes"):
            train[i][7]=float(1)
        elif(train[i][7]=="No"):
            train[i][7]=float(0) 
    for i in range(1,len(train)):
        for j in range(8,11):
            train[i][j]=float(train[i][j])
    train=train[1:]
   
    
def svm():
   C = [0.01, 0.1, 0.2, 0.5, 0.8, 1, 5, 10, 20, 50]
   SVMtrainAcc = []
   SVMtestAcc = []
   ytrain=[]
   xtrain=[]
   for i in range(len(train)):
        ytrain.append(xtrain)
   for i in range(len(train)):
        xtrain.append(xtrain)
   for param in C:

    #clf = SVC(C=param,kernel='linear',gamma='auto') # Linear Support Vector Machine
    clf = SVC(C=param,kernel='rbf',gamma='auto') # Nonlinear Support Vector Machine
    clf.fit(xtrain, ytrain)
    predictions = clf.predict(test)
        
def write_csv(filename):
    f=open(filename, 'w', encoding='utf8', newline='')
    global test
    global title
    writer=csv.writer(f)
    writer.writerow(title)

    #assert len(test)==len(predictions)

    for i in range(len(test)):
        test[i][-1]=int(predictions[i])
        writer.writerow(test[i])
    f.close()

read_csv("./insurance-test.csv")
read_traincsv("./insurance-train.csv")
svm()
write_csv("./svm.csv")

