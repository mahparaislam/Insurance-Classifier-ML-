import csv
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics 

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
   
    
def decisiontree():
    ytrain=[]
    xtrain=[]
    for i in range(len(train)):
        ytrain.append(xtrain)
    for i in range(len(train)):
        xtrain.append(xtrain)
    # Create Decision Tree classifer object
    clf = DecisionTreeClassifier()

    # Train Decision Tree Classifer
    clf = clf.fit(xtrain,ytrain)

#Predict the response for test dataset
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
decisiontree()
write_csv("./decisiontree.csv")
