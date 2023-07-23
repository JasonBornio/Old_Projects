using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class network : MonoBehaviour
{
    public int inputLength = 0;
    public int outputLength = 0;
    public int layers = 0;
    public int layerLength = 0;
    public int fullLength = 0;
    public List<List<Neuron>> fullNet = new List<List<Neuron>>();
    public List<Neuron> outputs  = new List<Neuron>();
    public List<Neuron> inputs = new List<Neuron>(); 
    public float learningrate = 0.1f;
    

    private void create(){

        fullLength = 1 + layers;

        for(int i = 0; i < inputLength; i++){
            Neuron node = new Neuron();
            inputs.Add(node);
        }

        
        fullNet.Add(inputs);
        
        if(layers == 0){
            for(int i = 0; i < outputLength; i++){
                Neuron node = new Neuron();
                outputs.Add(node);
            }

            fullNet.Add(outputs);

            for(int i = 0; i < outputLength; i++){
                fullNet[fullLength][i].connect(fullNet[fullLength-1]);
            }
        }
        else{
            for(int j = 0; j < layers; j++){
                List<Neuron> temp = new List<Neuron>();
                for(int i = 0; i < layerLength; i++){
                    Neuron node = new Neuron();
                    temp.Add(node);
                }

                fullNet.Add(temp);

            }

            for(int i = 0; i < outputLength; i++){
                Neuron node = new Neuron();
                outputs.Add(node);
            }

            fullNet.Add(outputs);

            //CONNECT--------------------------------

            for(int j = 0; j < fullLength - 1; j++){
                for(int i = 0; i < layerLength; i++){
                    fullNet[j+1][i].connect(fullNet[j]);
                }
            }
            
            for(int i = 0; i < outputLength; i++){
                fullNet[fullLength][i].connect(fullNet[fullLength-1]);
            }

        }



    }

    public void copy(network copy){
        learningrate = 0;
        learningrate += copy.learningrate;
        inputLength += copy.inputLength;
        outputLength += copy.outputLength;
        layers += copy.layers;
        layerLength += copy.layerLength;
        fullLength += copy.fullLength;

        for(int i = 0; i < inputLength; i++){
            Neuron node = new Neuron();
            node.weightsLength += copy.fullNet[0][i].weightsLength;
            node.bias =0f;
            node.deltaBias =0f;
            node.activation = 0f;
            node.activation += copy.fullNet[0][i].getActivation();
            node.setBias(copy.fullNet[0][i].bias);
            node.setDeltaBias(copy.fullNet[0][i].deltaBias);
            inputs.Add(node);
        }

        
        fullNet.Add(inputs);
        
        if(layers == 0){
            for(int i = 0; i < outputLength; i++){
                Neuron node = new Neuron();
                node.weightsLength += copy.fullNet[1][i].weightsLength;
                node.bias =0f;
                node.deltaBias =0f;
                node.activation = 0f;
                node.activation += copy.fullNet[1][i].getActivation();
                node.setBias(copy.fullNet[1][i].bias);
                node.setDeltaBias(copy.fullNet[1][i].deltaBias);
                for (int k = 0; k < node.weightsLength; k++){
                    node.weights.Add(0f);
                    node.deltaWeights.Add(0f);                    
                    node.setWeight(k,copy.fullNet[1][i].weights[k]);
                    node.setDeltaWeight(k,copy.fullNet[1][i].deltaWeights[k]);
                }
            }

            fullNet.Add(outputs);
        }
        else{
            for(int j = 0; j < layers; j++){
                List<Neuron> temp = new List<Neuron>();
                for(int i = 0; i < layerLength; i++){
                Neuron node = new Neuron();
                node.weightsLength += copy.fullNet[j+1][i].weightsLength;
                node.bias =0f;
                node.deltaBias =0f;
                node.activation = 0f;
                node.activation += copy.fullNet[j+1][i].getActivation();
                node.setBias(copy.fullNet[j+1][i].bias);
                node.setDeltaBias(copy.fullNet[j+1][i].deltaBias);
                for (int k = 0; k < node.weightsLength;k++){
                    node.weights.Add(0f);
                    node.deltaWeights.Add(0f);
                    node.setWeight(k,copy.fullNet[j+1][i].weights[k]);
                    node.setDeltaWeight(k,copy.fullNet[j+1][i].deltaWeights[k]);
                }
                temp.Add(node);
                }

                fullNet.Add(temp);

            }

            for(int i = 0; i < outputLength; i++){
                Neuron node = new Neuron();
                node.weightsLength += copy.fullNet[fullLength][i].weightsLength;
                node.bias =0f;
                node.deltaBias =0f;
                node.activation = 0f;
                node.activation += copy.fullNet[fullLength][i].getActivation();
                node.setBias(copy.fullNet[fullLength][i].bias);
                node.setDeltaBias(copy.fullNet[fullLength][i].deltaBias);
                for (int j = 0; j < node.weightsLength; j++){
                    node.weights.Add(0f);
                    node.deltaWeights.Add(0f);                    
                    node.setWeight(j,copy.fullNet[fullLength][i].weights[j]);
                    node.setDeltaWeight(j,copy.fullNet[fullLength][i].deltaWeights[j]);
                }
                outputs.Add(node);
            }

            fullNet.Add(outputs);

        }



    }


    public network(int inLength, int outLength, int lay, int layLength, bool init){
        inputLength = inLength;
        outputLength = outLength;
        layers = lay;
        layerLength = layLength;
        if(init){
            create();
        }
    }

    public network(){
        
    }

    public List<Neuron> feedForward(List<float> inputs){

        for(int i = 0; i < inputLength; i++){
            fullNet[0][i].setActivation(inputs[i]);
        }

        for(int j = 0; j < fullLength - 1; j++){
            for(int i = 0; i <layerLength; i++){
                fullNet[j+1][i].calculate(fullNet[j]);
            }
        }

        for(int i = 0; i <outputLength; i++){
            fullNet[fullLength][i].calculate(fullNet[fullLength-1]);
        }

        return outputs;

    }

    public float loss(float distance){
        float loss = 0f;
        return loss;
    }

    public void evolve(int x){

        for(int j = 0; j< fullLength-1; j++){
            for(int i = 0; i < layerLength; i++){
                fullNet[j+1][i].updateWeights(fullNet[j], 0.5f * learningrate, x);
            }
        }
        for(int i = 0; i<outputLength; i++){
            fullNet[fullLength][i].updateWeights(fullNet[fullLength-1], 0.5f * learningrate, x);
        }

    }
    
}
