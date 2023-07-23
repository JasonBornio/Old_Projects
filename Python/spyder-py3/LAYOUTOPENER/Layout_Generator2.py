# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 20:42:04 2022

@author: Jugwu
"""
import numpy as np
import layouGenerator as lay
import os
from pathlib import Path
import re
import DATA as d
import matplotlib.pyplot as plt
FOLDER = 'C:\\'

ratios = [
    [(960/1154),(480/1154),(480/1154),0, 0, 0, 0],
    [(960/577),(960/577),(960/1154),0,0, 0, 0],
    [(960/1154),(480/577),(480/577),(480/1154),0, 0, 0],
    [(960/577),(960/1154),(480/577),(480/577),0, 0, 0],
    [(480/1154),(480/1154),(480/1154),(480/1154),0, 0, 0],
    [(960/577),(960/577),(960/577),(960/577),0, 0, 0],
    [(960/577),(960/577),(480/1154),(480/1154),0, 0, 0],
    [(960/1154),(480/577),(480/577),(480/577),(480/577), 0, 0],
    [(480/577),(480/577),(480/1154),(480/1154),(480/1154), 0, 0],
    [(960/577),(480/577),(480/577),(480/1154),(480/1154), 0, 0],
    [(960/577),(960/577),(480/577),(480/577),(480/1154), 0, 0],
    [(960/577),(960/577),(960/577),(480/577),(480/577), 0, 0],
    [(480/577),(480/577),(480/577),(480/577),(480/1154), (480/1154), 0],
    [(960/577),(960/577),(480/577),(480/577),(480/577), (480/577), 0],
    [(480/577),(480/577),(480/577),(480/577),(480/577), (480/577), (480/1154)],
    [(960/577),(480/577),(480/577),(480/577),(480/577), (480/577), (480/577)]
]

labels = [
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
]
  
iteratione = 0
#-----------------------------
class Neuron(object):
    def __init__(self,state):
        self.state = state * 3 * iteratione
        #print(self.state)
        self.weights = []
        self.gradients = []
        self.deltas = []
        np.random.seed(self.state)
        self.bias = ((np.random.rand() * 2) -1)
        self.biasGradient = 1
        self.biasDelta = 1
        self.activation = 0
        self.weightsLength = 0
        self.LOSSVAL = 0
        return
    
    def initialWeights(self, previousLayer):
        np.random.seed(self.state + 1)
        self.weights = []
        self.gradients = []
        self.deltas = []
        self.weights = (np.random.rand(np.size(previousLayer)) * 2) -1
        self.weightsLength = np.size(previousLayer)
        self.gradients = np.ones(np.size(previousLayer)) 
        self.deltas = np.ones(np.size(previousLayer)) 
        #print(self.gradients)  
        return
    
    def shiftWeights(self, grad, rate):
        np.random.seed(self.state + 2)
        oldGrads = self.gradients
        self.gradients = ((np.random.rand(self.weightsLength) * 2) -1) * rate + np.multiply(oldGrads,0.6) 
        self.weights += self.gradients * grad 
        #self.weights = (np.random.rand(np.size(self.weightsLength)) * 5) -1
        oldbGrad = self.biasGradient
        self.biasGradient = ((np.random.rand() * 2) -1) * rate + np.multiply(oldbGrad,0.6) 
        self.bias += self.biasGradient * grad
        
    def getActivation(self):
        return self.activation
    
    def setActivation(self, inp):
        self.activation = inp
    
    def calculate(self, previousLayer):
        product = sum(a.getActivation() * w for a,w in zip(previousLayer, self.weights))
        self.activation = sigmoid(product + self.bias)
        #print(activation)
        return
#-----------------------------
class NeuralNet(object):
    def __init__(self, state):
        self.state = state
        self.network = []
        self.inputSize = 0
        self.outputSize = 0
        self.numLayers = 0
        self.layerSize = 0
        self.totalLength = 0
        return
    
    def create(self, inputSize, outputSize, numLayers, layerSize):
        self.inputSize = inputSize
        self.outputSize = outputSize
        self.numLayers = numLayers
        self.layerSize = layerSize
        self.totalLength = 2 + self.numLayers
        offset = ((self.layerSize * self.numLayers) + self.inputSize + self.outputSize) * self.state
        layer = [Neuron(i + offset) for i in range(self.inputSize)]
        self.network.append(layer)
        for i in range(self.numLayers):
            layer = [Neuron(j+self.inputSize+ offset) for j in range(self.layerSize)]
            self.network.append(layer)
        layer = [Neuron((k+self.inputSize+(self.layerSize*self.numLayers))+ offset) for k in range(self.outputSize)]
        self.network.append(layer)
        
        for i in range(self.totalLength):
            if i != 0:
                for neuron in self.network[i]:
                    neuron.initialWeights(self.network[i-1])
        return
    
    def feedforward(self, inputs):
        for i in range(self.totalLength):
            if i == 0:
                for neuron, inp in zip(self.network[0], inputs):
                    neuron.setActivation(inp)
            else:
                for neuron in self.network[i]:
                    neuron.calculate(self.network[i-1])

    def evolve(self, inputs):
        averageloss = 0
        size = 0

        for inp in inputs[3:]:
            if inp != 0:
                size += 1


        acts = []   
        for outputs in self.network[self.totalLength-1]:
            #print(outputs.getActivation()) 
            acts.append(outputs.getActivation())
                        
        maxVal = np.argmax(acts)
        #print("VECTOR:" +str(acts))
        #print("PREDICTION:" + str(acts[maxVal]))
        
        losi = 0
        #print("INPUTS:" + str(inputs[3:]))
        #print("RATIOS:"+ str(ratios[maxVal]))
        #print()
        for inp, rat in zip(inputs[3:], ratios[maxVal]):
            losi += self.loss(rat, inp)
        averageloss = losi / size
        self.LOSSVAL = 0
        self.LOSSVAL += averageloss
        #print(averageloss)
        
        for layer in self.network:
            for neuron in layer:
                neuron.shiftWeights(averageloss, 0.01)
        return
    
    def evolve2(self):
        i = 0
        los = 0
        for outputs in self.network[self.totalLength-1]:
            #print(outputs.getActivation()) 
            los += self.loss(labels[i], outputs.getActivation())
            i +=1

        self.LOSSVAL = 0
        self.LOSSVAL += (los / self.outputSize)
        #print(averageloss)
        
        for layer in self.network:
            for neuron in layer:
                neuron.shiftWeights(self.LOSSVAL, 0.01)
        return
    
    def predict(self, inputs):
        outputs = []
        
        for inp in inputs:
            self.feedforward(inp)
            
            outs = []
            for i in range(self.outputSize):
                outs.append(self.network[self.totalLength-1][i].getActivation())
            outputs.append(outs)
        return outputs
    
    def train(self, inp):
        
        self.feedforward(inp)
        self.evolve2()
        #print("LOSS: " +str(self.LOSSVAL))
            
        return
    
    def loss(self, template, inputs):
        return 1/2 *(template - inputs)**2
#-----------------------------
def sigmoid(x):
    return 1 / (1 + np.exp(-x)) 

# Print iterations progress
def printProgressBar (iteration, total,loss, prefix = '', suffix = '', decimals = 3, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    los = ("{0:." + str(10) + "f}").format(float(loss))
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% Loss: {los}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

#-----------------------------   
def GETDATA():
    
    count = 0
    urls = []
    
        
    for i in range(5):
        with open('FILES\\train.txt', 'a',encoding='utf-8') as f:
            f.write("\nDATA" + str(i+3) +" = [")
            f.close()

        files = sorted(Path(FOLDER).iterdir(), key = os.path.getctime)
        for file in files:
            filename = os.fsdecode(file)
            for ext in lay.EXTENSIONS:
                if ext in filename.lower():

                    fold = re.sub (r'\\','/', filename)
                    fold = re.sub (r'Ã³','ó', fold)
                    filepath = 'file:///' + fold

                    urls.append(filepath)

                    if count == i + 2:
                        count = -1
                        with open('FILES\\newLayout.txt', 'w',encoding='utf-8') as f:
                            for url in urls:
                                f.write(url)
                                f.write('\n')
                            f.close()
                        urls = []
            
                        widthVect, heightVect, num, urlzz = lay.getDimensions()
                        w_h_Ratios = np.divide(widthVect, heightVect)
                        #print(num)
                        if num == 3:
                            numBit = "0,0,0,"
                        if num == 4:
                            numBit = "1,0,0,"
                        if num == 5:
                            numBit = "0,1,0,"
                        if num == 6:
                            numBit = "0,0,1,"
                        if num == 7:
                            numBit = "1,1,1,"
                            
                        with open('FILES\\train.txt', 'a',encoding='utf-8') as f:
                            f.write("[")
                            f.write(numBit)
                            for ratio in w_h_Ratios:
                                f.write(str(ratio))
                                f.write(",")
                                
                            for x in range(7 - num):
                                f.write("0")
                                if x != (7- num) -1:
                                    f.write(",")
                            f.write("],\n")
                            f.close()
                    count += 1
        
        with open('FILES\\train.txt', 'a',encoding='utf-8') as f:
            f.write("]")
            f.close()   
    return

def TRAIN(networks, iterations):
    dataRange = 150
    data = []
    nets = networks
    size = np.size(nets)
    first = True
    lowestLoss = 10000
    bestNet = NeuralNet(size+1)
    for i in range(dataRange):
        data.append(d.DATA3[i])
        data.append(d.DATA4[i])
        data.append(d.DATA5[i])
        data.append(d.DATA6[i])
        data.append(d.DATA7[i])
        #######################
        #######################
    #print(data) 
    x = 0
    LENGTH = iterations * dataRange * 5 * size
    for j in range(iterations): 
        itrloss = 0
        los = 0
        count = 0
        for inp in data:
            #print("------------------------")
            for net in nets:
                net.train(inp)
                printProgressBar(x, LENGTH, lowestLoss, prefix = 'Progress:', suffix = 'Complete', length = 30)
                x+=1
            
            iteratione
            losses = []
            grad = 0
            for net in nets:
                grad += net.LOSSVAL
                losses.append(net.LOSSVAL)
            grad /= size
            acts =[]
            for net in nets:
                acts.append(net.network[2][1].getActivation())
            index = np.argmin(losses)
            #print("index:"+str(index))
            
            #print("los:" +  str(grad))#str(losses))
            if losses[index] < lowestLoss:
                #print("LOGGERS")
                bestNet = nets[index]
                first = False
                lowestLoss = 0
                lowestLoss += losses[index]
            
            #print("LOSS: " + str(lowestLoss))
            #print()
        
            if not (j == iterations - 1) and (count == dataRange - 1):
                firstNet = True
                for net in nets: 
                    if firstNet == True:
                        copyNet(bestNet, net,False)
                    else:
                        copyNet(bestNet, net,True)
            count += 1
            
            los += grad
        itrloss = los/(dataRange * 5)
        #print("ITERLOSS:" + str(itrloss))

    predictions = bestNet.predict(ratios)
    i = 0
    for pred in predictions:
        #print(pred)
        maxVal = np.argmax(pred)
        plt.figure() 
        plt.plot(pred)
        plt.plot(labels[i])
        plt.title(f"predictions vs labels: {i} chosen: {maxVal}")
        plt.xlabel('predicted')
        plt.ylabel('labels')
        plt.show()
        i+=1

    return

def copyNet(net, copy, mutate):

    for layer, clayer in zip (net.network, copy.network):
        for neuron, cneuron in zip(layer, clayer):
            for w, cw in zip(neuron.weights, cneuron.weights):
                if mutate==True:
                    mu = -1#((np.random.rand() * 2) -1)/1.5
                else:
                    mu = 0
                cw = 0
                cw += (w + mu)
            for g, cg in zip(neuron.gradients, cneuron.gradients):
                if mutate==True:
                    mu = -1#((np.random.rand() * 2) -1)/1.5
                else:
                    mu = 0
                cg = 0
                cg += (g + mu)
        if mutate==True:
            mu = -1#((np.random.rand() * 2) -1)/1.5
        else:
            mu = 0
        cneuron.bias = 0
        cneuron.bias += (neuron.bias + mu)
        if mutate==True:
            mu = -1#((np.random.rand() * 2) -1) /1.5
        else:
            mu = 0
        cneuron.biasGradient = 0
        cneuron.biasGradient += (neuron.biasGradient + mu)
            
    copy.LOSSVAL = net.LOSSVAL
    return
#-----------------------------
def main():
    netrs = []
    for i in range(50): 
        network = NeuralNet(i)
        netrs.append(network)
        netrs[i].create(10,16,1,3)
    print("hey")
        
    TRAIN(netrs, 1)
    
    return 0

if __name__ == "__main__":
    main()
    
    
    