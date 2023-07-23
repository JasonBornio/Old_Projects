# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 17:32:59 2022

@author: Jugwu
"""
import NeuralNet as nn
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import pandas_datareader as web
import pandas as pd 
import datetime as dt
import matplotlib.pyplot as plt

scaler = MinMaxScaler(feature_range= (0,1))

def loadData():
    #Load Data

    #chose stock data from facebook
    company = 'FB'
    #from 2012 to 2021
    start = dt.datetime(2012, 1, 1)
    end = dt.datetime(2021, 1, 1)

    #use yahoo
    data = web.DataReader(company, 'yahoo', start,end)
    
    #prepare Data
    scaled_data = scaler.fit_transform(data['Close'].values.reshape(-1,1))

    prediction_days = 60

    X_train = []
    Y_train = []

    for x in range(prediction_days,len(scaled_data)):
        X_train.append(scaled_data[x-prediction_days:x, 0])
        Y_train.append(scaled_data[x, 0])
    
    X_train = np.array(X_train)
    X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1]))#, 1))
    
    test_start = dt.datetime(2018, 1, 1)
    test_end = dt.datetime.now()

    test_data = web.DataReader(company, 'yahoo',test_start, test_end)
    total_dataset = pd.concat((data['Close'], test_data['Close']), axis = 0)

    model_inputs = total_dataset[len(total_dataset) - len(test_data)-prediction_days:].values
    model_inputs = model_inputs.reshape(-1,1)
    model_inputs = scaler.transform(model_inputs)

    X_test = []
    Y_test = []

    for x in range(prediction_days, len(model_inputs)):
        X_test.append(model_inputs[x-prediction_days:x,0])
        Y_test.append(model_inputs[x, 0])

    X_test = np.array(X_test)
    X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1]))#,1))
    #//////////////////////////////////////////////////

    return X_train, Y_train, X_test, Y_test

def main():
    
    training_inputs, labels, test_inputs, test_labels = loadData()
    #print(training_inputs.shape[1])
    #print(training_inputs[0][0])
    #print(labels)
    MLP = nn.MultiLayerPerceptron(training_inputs.shape[1],1,0,80)
    MLP.load("stocksFULL.txt")
    #MLP.load("stocksFULL2.txt")
    #MLP.setThreshold(0.000004)
    #MLP.setEtaAplha(0.02, 0.003)
    MLP.setEtaAplha(0.5, 0.1)
    MLP.setEtaAplha(0.007, 0.005)
    MLP.train(500, training_inputs, labels, lossPlot=True)#, stopCondition=True)
    MLP.save("stocksFULL.txt")
     
    predicted_prices = MLP.predict(test_inputs,test_labels)
    predicted_prices = scaler.inverse_transform(predicted_prices)
    
    test_start = dt.datetime(2018, 1, 1)
    test_end = dt.datetime.now()
    
    company = 'FB'
    test_data = web.DataReader(company, 'yahoo',test_start, test_end)
    actual_prices = test_data['Close'].values
    
    plt.figure()
    plt.plot(actual_prices,color="black",label=f"Actual {company} Price")
    plt.plot(predicted_prices,color="blue",label=f"Predicted {company} Price")
    plt.title(f"{company} Share Price")
    plt.xlabel('Time')
    plt.ylabel(f'{company} Share Price')
    plt.legend()
    plt.show()

    return 0
    
if __name__ == "__main__":
    main()