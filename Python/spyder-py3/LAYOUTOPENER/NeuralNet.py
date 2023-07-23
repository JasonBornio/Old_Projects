import math
import matplotlib.pyplot as plt

import numpy as np


DATAPATH = "models\\"

class MultiLayerPerceptron(object):
    def __init__(self,dim_input, dim_output,dim_layer,dim_length):
        self.inputLength = dim_input
        self.outputLength = dim_output
        self.layers = dim_layer
        self.layerLength = dim_length
        self.weightVector = []
        self.biasVector = []
        self.activations = []
        self.gradients = []
        self.delta = []
        self.Biasdelta = []
        self.Biasgradients = []
        self.currentInputs = []
        self.intildelta = True
        self.eta = 0.001
        self.alpha = 0.0008
        self.threshold = 0.0001
        self.intialiseWeights()

            
          ##################################################
          
    def save(self,file):
        with open(DATAPATH + file, 'w', encoding="utf-8") as f:
            f.write(str(self.inputLength) + "\n")
            f.write(str(self.outputLength) + "\n")
            f.write(str(self.layers) + "\n")
            f.write(str(self.layerLength) + "\n")
            for x in range(3):
                if x == 0:
                    for j in range(self.layerLength):
                        f.write(str(self.biasVector[0][j])+ "\n")
                        f.write(str(self.Biasdelta[0][j])+ "\n")
                        f.write(str(self.Biasgradients[0][j])+ "\n")
                        for i in range(self.inputLength):
                            f.write(str(self.weightVector[0][i][j])+ "\n")
                elif x == 1:
                    for k in range(self.layers):
                        for j in range(self.layerLength):
                            f.write(str(self.biasVector[1][k][j])+ "\n")
                            f.write(str(self.Biasdelta[1][k][j])+ "\n")
                            f.write(str(self.Biasgradients[1][k][j])+ "\n")
                            for i in range(self.layerLength):
                                f.write(str(self.weightVector[1][k][i][j])+ "\n")
                elif x == 2:
                    for j in range(self.outputLength):
                        f.write(str(self.biasVector[2][j])+ "\n")
                        f.write(str(self.Biasdelta[2][j])+ "\n")
                        f.write(str(self.Biasgradients[2][j])+ "\n")
                        for i in range(self.layerLength):
                            f.write(str(self.weightVector[2][i][j])+ "\n")
            #f.write("DELTAS\n")
            for k in range(self.layers+2):
                if k == 0: 
                    for i in range(self.inputLength):
                        f.write(str(self.delta[0][i])+ "\n")
                elif k == self.layers + 1:
                    for i in range(self.layerLength):
                        f.write(str(self.delta[k][i]) + "\n")
                else:
                    for i in range(self.layerLength):
                        f.write(str(self.delta[k][i]) +"\n") 
                        
            #f.write("GRADS\n")    
            for k in range(self.layers + 2):
                if k == self.layers + 1:
                    for i in range(self.outputLength):
                        #f.write("POGGERG\n")
                        f.write(str(self.gradients[k][i])+ "\n")
                else:
                    for i in range(self.layerLength):
                        #f.write("POG\n")
                        f.write(str(self.gradients[k][i])+ "\n")
        f.close()
        return
    
    def load(self,file):
                
        self.weightVector = []
        self.biasVector = []
        
        with open(DATAPATH + file, 'r') as f:
            self.inputLength = int(f.readline())
            self.outputLength = int(f.readline())
            self.layers = int(f.readline())
            self.layerLength =int(f.readline())
            self.intialiseWeights()
            for x in range(3):
                if x == 0:
                    for j in range(self.layerLength):
                        self.biasVector[0][j] = 0
                        self.biasVector[0][j] += float(f.readline())
                        #print(self.biasVector[0][j])
                        self.Biasdelta[0][j] = 0
                        self.Biasdelta[0][j] += float(f.readline())
                        #print(self.Biasdelta[0][j])
                        self.Biasgradients[0][j] = 0
                        self.Biasgradients[0][j] += float(f.readline())
                        #print(self.Biasgradients[0][j])
                        for i in range(self.inputLength):
                            self.weightVector[0][i][j] = 0
                            self.weightVector[0][i][j] += float(f.readline())
                elif x == 1:
                    for k in range(self.layers):
                        for j in range(self.layerLength):
                            self.biasVector[1][k][j] = 0
                            self.biasVector[1][k][j] += float(f.readline())
                            self.Biasdelta[1][k][j] = 0
                            self.Biasdelta[1][k][j] += float(f.readline())
                            self.Biasgradients[1][k][j] = 0
                            self.Biasgradients[1][k][j] += float(f.readline())
                            for i in range(self.layerLength):
                                self.weightVector[1][k][i][j] =0
                                self.weightVector[1][k][i][j] +=float(f.readline())
                elif x == 2:
                    for j in range(self.outputLength):
                        self.biasVector[2][j] = 0
                        self.biasVector[2][j] += float(f.readline())
                        self.Biasdelta[2][j] = 0
                        self.Biasdelta[2][j] += float(f.readline())
                        self.Biasgradients[2][j] = 0
                        self.Biasgradients[2][j] += float(f.readline())
                        for i in range(self.layerLength):
                            self.weightVector[2][i][j] = 0
                            self.weightVector[2][i][j] += float(f.readline())
            
            if self.intildelta == True:
                a1Vector = []
                for j in range(self.layerLength):
                    i, a1 = 0, 0
                    for x in range(self.inputLength):
                        a1 += 1 * 1
                        i+=1
                    a1 += self.biasVector[0][j]
                    a1Vector.append(a1)
                self.activations.append(a1Vector)
                #layers
                a2VectLarge = []
                for k in range(self.layers):
                    a2Vector = []
                    for j in range(self.layerLength):
                        a2 = 0
                        for i in range(self.layerLength):
                            a2 += 1 * 1
                        a2 += self.biasVector[1][k][j]
                        #print(j)
                        a2Vector.append(a2)
                    self.activations.append(a2Vector)
                    a2VectLarge.append(a2Vector)
                    #print(self.activations)
                #output
                a3Vector = []
                for j in range(self.outputLength):
                    a3 = 0
                    for i in range(self.layerLength):
                        a3 += 1 * 1
                    a3 += self.biasVector[2][j]
                    a3Vector.append(a3)
                self.activations.append(a3Vector)
                
                self.delta =[]
                self.gradients =[]
                v0 = (np.random.rand(self.inputLength))
                self.delta.append(v0)
                self.delta.append(a1Vector)
                self.gradients.append(a1Vector)
                for i in range(self.layers):
                    self.delta.append(a2VectLarge[i])
                    self.gradients.append(a2VectLarge[i])
                self.delta.append(a3Vector)
                self.gradients.append(a3Vector)
                    #print("POGGGGGGGGGGGGGGGGGGGGGGGERRRRRRRRRRRRRS")
                    
                self.intildelta = False
                
            #f.write("DELTAS\n")
            for k in range(self.layers+2):
                if k == 0: 
                    for i in range(self.inputLength):
                        self.delta[0][i]= 0
                        self.delta[0][i] += float(f.readline())
                elif k == self.layers + 1:
                    for i in range(self.layerLength):
                        self.delta[k][i]= 0
                        self.delta[k][i] += float(f.readline())
                else:
                    for i in range(self.layerLength):
                        self.delta[k][i] = 0
                        self.delta[k][i] += float(f.readline())
                        
            #f.write("GRADS\n")    
            for k in range(self.layers + 2):
                if k == self.layers + 1:
                    for i in range(self.outputLength):
                        #f.write("POGGERG\n")
                        self.gradients[k][i]= 0
                        self.gradients[k][i] += float(f.readline())
                else:
                    for i in range(self.layerLength):
                        #f.write("POG\n")
                        self.gradients[k][i]= 0
                        self.gradients[k][i] += float(f.readline())
        f.close()
        return
   
    def setEtaAplha(self, et,alp):
        self.eta = et
        self.alpha = alp
        return
    
    def setThreshold(self, thres):
        self.threshold = thres
        return
    
    def intialiseWeights(self):
        inputWeights = (np.random.rand(self.inputLength, self.layerLength ) * 2) -1
        outputWeights = (np.random.rand(self.layerLength,self.outputLength) * 2) -1
        layerWeights = (np.random.rand(self.layers,self.layerLength,self.layerLength)*2) -1
        self.weightVector.append(inputWeights)
        #print(self.weightVector)
        #print("...............") 
        #print(self.inputLength)
        self.weightVector.append(layerWeights)
        #print(self.weightVector)
        #print("...............") 
        
        self.weightVector.append(outputWeights)
        #print(self.weightVector)
        #print("...............") 
        
        inputBias = ((np.random.rand(self.layerLength) * 2) - 1)#/1000000 
        outputBias = ((np.random.rand(self.outputLength) * 2) - 1)#/1000000
        layerBias = ((np.random.rand(self.layers, self.layerLength)*2) - 1)#/1000000
        
        self.biasVector.append(inputBias)
        self.biasVector.append(layerBias)
        self.biasVector.append(outputBias)
        
        self.Biasdelta.append(inputBias)
        self.Biasdelta.append(layerBias)
        self.Biasdelta.append(outputBias)
        
        self.Biasgradients.append(inputBias)
        self.Biasgradients.append(layerBias)
        self.Biasgradients.append(outputBias)
        #print("PINGPONG")
        #index 1: inputs 0, layers 1, outputs 2
        #inputs index 2 input length and so on 
        return
    
    ##################################################
    def feedforward(self, inputs):
        #intialise
        self.activations = []
        
        #inputs           
        a1Vector = []
        for j in range(self.layerLength):
            i, a1 = 0, 0
            for inp in inputs:
                a1 += inp * self.weightVector[0][i][j]
                i+=1
            a1 += self.biasVector[0][j]
            a1Vector.append(sigmoid(a1))
        self.activations.append(a1Vector)
        
        #layers
        a2VectLarge = []
        for k in range(self.layers):
            a2Vector = []
            for j in range(self.layerLength):
                a2 = 0
                for i in range(self.layerLength):
                    a2 += self.activations[k][i] * self.weightVector[1][k][i][j]
                a2 += self.biasVector[1][k][j]
                #print(j)
                a2Vector.append(sigmoid(a2))
            self.activations.append(a2Vector)
            a2VectLarge.append(a2Vector)
        #print(self.activations)
                
        #output
        a3Vector = []
        for j in range(self.outputLength):
            a3 = 0
            for i in range(self.layerLength):
                a3 += self.activations[self.layers][i] * self.weightVector[2][i][j]
            a3 += self.biasVector[2][j]
            a3Vector.append(sigmoid(a3))
        self.activations.append(a3Vector)
        #print("DELTAAA")
        #print(self.delta)
        if self.intildelta == True:
            print("INITIALISING")
            self.intial(a1Vector, a2VectLarge,a3Vector)
          
        #print(self.activations[self.layers+1])
        return self.activations[self.layers+1]   
    ######################################
    def intial(self, v1, v2, v3):
        v0 = (np.random.rand(self.inputLength))
        self.delta.append(v0)
        self.delta.append(v1)
        self.gradients.append(v1)
        for i in range(self.layers):
            self.delta.append(v2[i])
            self.gradients.append(v2[i])
        self.delta.append(v3)
        self.gradients.append(v3)
        #print("POGGGGGGGGGGGGGGGGGGGGGGGERRRRRRRRRRRRRS")
        
        self.intildelta = False
    
    def derivative(self, inp):
        return 1 - inp * inp
        #return inp * (1 - inp)
    
    def sumDow(self, layerNum, index):
        summ = 0
        if layerNum == self.layers:
            for i in range(self.outputLength):
                summ += self.weightVector[2][index][i] * self.gradients[layerNum+1][i]
        else:
            for i in range(self.layerLength):
                summ += self.weightVector[1][layerNum][index][i] * self.gradients[layerNum+1][i]
        return summ
        
    def gradient(self, label, index):
        quotient = label - self.activations[self.layers+1][index]
        grad = quotient * self.derivative(self.activations[self.layers +1][index])
        self.gradients[self.layers + 1][index] = grad
        return grad
    
    def hiddenGradient(self, layerNum, index):
        dow = self.sumDow(layerNum, index)
        grad = dow * self.derivative(self.activations[layerNum][index])
        self.gradients[ layerNum][index] = grad
        return grad
    
    
    def sumDowBIAS(self, layerNum, index):
        summ = 0
        if layerNum == self.layers:
            for i in range(self.outputLength):
                summ += self.weightVector[2][index][i] * self.gradients[layerNum+1][i]
        else:
            for i in range(self.layerLength):
                summ += self.weightVector[1][layerNum][index][i] * self.gradients[layerNum+1][i]
        return summ
        
    def gradientBIAS(self, label, index):
        quotient = label - self.activations[self.layers+1][index]
        grad = quotient * self.derivative(self.activations[self.layers +1][index])
        self.Biasgradients[2][index] = grad
        return grad
    
    def hiddenGradientBIAS(self, layerNum, index):
        dow = self.sumDow(layerNum, index)
        grad = dow * self.derivative(self.activations[layerNum][index])
        if layerNum == 0:
            self.Biasgradients[0][index] = grad
        else:
            self.Biasgradients[1][layerNum - 1][index] = grad
        return grad
    
    
    def updateBiases(self, layerNum):
        if layerNum == 0: 
            for i in range(self.layerLength):
                oldDw = self.Biasdelta[0][i] 
                newDw = self.eta * self.Biasgradients[0][i]  + self.alpha * oldDw
                self.Biasdelta[0][i] = newDw
                self.biasVector[0][i]  += newDw
                #print("input")
                #print(newDw)
        elif layerNum == self.layers + 1:
            for i in range(self.outputLength):
                oldDw = self.Biasdelta[2][i] 
                newDw = self.eta  * self.Biasgradients[2][i]  + self.alpha * oldDw
                self.Biasdelta[2][i]  = newDw
                self.biasVector[2][i]  += newDw
                #print("outputs")
                #print(newDw)
        else:
            for i in range(self.layerLength):
                oldDw = self.Biasdelta[1][layerNum -1][i] 
                newDw = self.eta * self.Biasgradients[1][layerNum -1][i]  + self.alpha * oldDw
                self.Biasdelta[1][layerNum - 1][i]  = newDw
                self.biasVector[1][layerNum -1][i]  += newDw
                #print("layers")
                #print(newDw)
            
        return
    
    
    def updateWeigths(self, layerNum, index):
        if layerNum == 0: 
            for i in range(self.inputLength):
                oldDw = self.delta[0][i] 
                #print(np.shape(self.currentInputs))
                #print(np.shape(self.gradients[layerNum]))
                #print("DOOOONE")
                #print(self.inputLength)
                newDw = self.eta * self.currentInputs[i] * self.gradients[layerNum][index] + self.alpha * oldDw
                self.delta[0][i] = newDw
                self.weightVector[0][i][index] += newDw
                #print("input")
                #print(newDw)
        elif layerNum == self.layers + 1:
            for i in range(self.layerLength):
                oldDw = self.delta[layerNum][i] 
                newDw = self.eta * self.activations[self.layers][i] * self.gradients[layerNum][index] + self.alpha * oldDw
                self.delta[layerNum][i] = newDw
                self.weightVector[2][i][index] += newDw
                #print("outputs")
                #print(newDw)
        else:
            for i in range(self.layerLength):
                oldDw = self.delta[layerNum][i] 
                newDw = self.eta * self.activations[layerNum-1][i] * self.gradients[layerNum][index] + self.alpha * oldDw
                self.delta[layerNum][i] = newDw
                self.weightVector[1][layerNum-1][i][index] += newDw
                #print("layers")
                #print(newDw)
            
        return
    
    def loss(self,preds, labels):
        loss = 0
        #print(preds)
        if self.outputLength > 1:
            for i in range(self.outputLength):
                loss += 1/2 * (labels[i] - preds[i])**2
        else:
            loss = 1/2 * (labels - preds)**2
        return loss
    
    ###################################################
    def backprop(self, label):
        
        #output grads
        if self.outputLength > 1:
            #self.Biasgradients[2] = 0
            for i in range(self.outputLength):
                self.gradient(label[i], i)
                self.gradientBIAS(label[i], i)
        else:
            self.gradient(label, 0)
            self.gradientBIAS(label, 0)

        #hidden grads
        
        for k in range(self.layers + 1):
            if k == self.layers:
                for i in range(self.layerLength):
                    self.hiddenGradient(k, i)
                    self.hiddenGradientBIAS(k, i)
            else:
                for i in range(self.layerLength):
                    self.hiddenGradient(k, i)
                    self.hiddenGradientBIAS(k, i)
                    
        #############################CHECK 
        #update weights
        self.updateBiases(self.layers+1)
        for i in range(self.outputLength):
            self.updateWeigths(self.layers+1, i)
            
        for k in range(self.layers+1):
            #if k != self.layers+1:
            self.updateBiases(k)
            for i in range(self.layerLength):
                self.updateWeigths(k, i)
        
        

        #return
        return
        
    ###################################################
    def train(self,iterations, training_inputs, labels, stopCondition = False, lossPlot = False, batch = 0):
        lossVector = [] 
        printProgressBar(iterations, iterations, 0, prefix = 'Progress:', suffix = 'Complete', length = 30)
        avloss = 0
        i = 0
        training_inputs = shuffle(training_inputs)
        for _ in range(iterations):
            los = 0
            for inputs, label in zip(training_inputs, labels): 
                prediction = self.feedforward(inputs)
                self.currentInputs = inputs
                self.backprop(label)
                self.currentInputs = []
                i+=1
                printProgressBar(i , iterations * len(labels) ,avloss, prefix = 'Progress:', suffix = 'Complete', length = 30)
                loss = self.loss(prediction, label)
                los+=loss
            avloss = los/len(labels)
            lossVector.append(avloss)
        if lossPlot == True:
            plt.plot(lossVector)
            plt.plot(lossVector)
            plt.title("Loss Function")
            plt.xlabel('iterations')
            plt.ylabel(f'Average loss')
            return

    ####################################################              
    def predict(self, test_inputs,labels, show = False):
        output = []
        i = 0
        for inputs, label in zip(test_inputs, labels): 
            prediction = self.feedforward(inputs)
            if show == True:
                print("-------------------------")
                print("inNodes:")
                print(inputs)
                print("label:")
                print(label)
                print("prediction:")
                print(prediction)
                print("-------------------------")
            i += 1
            #printProgressBar(i, np.size(labels), 0, prefix = 'Progress:', suffix = 'Complete', length = 30)
            output.append(prediction)
        return output
#Functions/////////////////////////////////////
def sigmoid(x):
    result = 1 / (1 + math.exp(-x))
    if False: #result < 0.00001:
        return 0
    else:
        return result
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
#
def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    list1, j = [], 0
    i = 0
    while i < len(lst):
        if len(lst[i:i + n]) == 5:
            list1.append(lst[i:i+n])
            #print(lst[i:i+n])
            i += n
        else:
            j+=1
            i += n
    return list1, j

def shuffle(datas):
    datas2 = []
    for data in datas:
        data2 = []
        for d in data:
            rand = ((np.random.rand() * 2) -1) * (d *0.25)
            d = d + rand
            data2.append(d)
        datas2.append(data2)
    return datas2