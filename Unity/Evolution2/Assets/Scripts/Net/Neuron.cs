using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Neuron : MonoBehaviour
{
    public List<float> weights =  new List<float>();
    public float activation = 0;
    public float bias = 0;
    public int weightsLength = 0;
    public List<float> deltaWeights = new List<float>();
    public float deltaBias = 0.5f;


    public void connect(List<Neuron> previousLayer){
        //float rand = 0f;
        weightsLength = previousLayer.Count;
        for(int i = 0; i < weightsLength; i++){
            weights.Add(Random.Range(-1.0f, 1.0f));
            deltaWeights.Add(Random.Range(-1.0f, 1.0f));
            //Debug.Log(weights);
        }
        bias = Random.Range(-1.0f, 1.0f);  
    }

    public void calculate(List<Neuron> previousLayer){
        float sum = 0;
        for(int i = 0; i < weightsLength; i++){
            sum += previousLayer[i].getActivation() * weights[i];
        }
        activation = function(sum + bias);
    }

    public float function(float value){
        return 1/(1 + Mathf.Exp(-value));
    }

    public float getActivation(){
        return activation;
    }

    public void setActivation(float input){
        activation = function(input);
    }

    public float getWeight(int index){
        return weights[index];
    }

    public void updateWeights(List<Neuron> previousLayer, float gradient, int x){

        float grad = 0;
        float oldDelta = 0;

        for(int i = 0; i < weightsLength; i++){
            oldDelta = deltaWeights[i];

            grad = ((oldDelta * 1.0f) + (Random.Range(-1.0f, 1.0f) * previousLayer[i].getActivation())) * gradient;
            
            deltaWeights[i] = grad;
            weights[i] += deltaWeights[i]; //+ x*0.1f;;
        }

        oldDelta = deltaBias;
        grad = ((oldDelta * 1.0f) + (Random.Range(-1.0f, 1.0f))) * gradient;
        deltaBias = grad;
        bias += deltaBias; //+ x*0.1f;

    }

    public void setDeltaWeight(int index, float input){
        deltaWeights[index] += input;
    }

    public void setWeight(int index, float input){
        weights[index] += input;
    }

    public void setDeltaBias(float input){
        deltaBias += input;
    }

    public void setBias(float input){
        bias += input;
    }
}

