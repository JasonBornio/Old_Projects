#pragma once
#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <Windows.h>
#include <array>
#include <stdlib.h> 

using namespace std;


class Neuron
{
public:

#pragma region publicFuncs

	Neuron();
	~Neuron();
	void Connect(vector<Neuron> previousLayer);
	void calculateActivation(vector<Neuron> previousLayer);
	float activationFunction(float input);
	float activationDerivative(float input);

	void setActivation(double input);
	float getActivation();
	void setBias(double input);
	float getBias();
	void setWeight(float input, int index);
	float getWeight(int index);
	void setDelta(float input, int index);
	float getDelta(int index);
	void setGradient(float input, int index);
	float getGradient(int index);

	void showWeights();
	void showGradients();
	void showDeltas();

	void calculateOutputGradients(vector<Neuron> previousLayer);
	void calculateHiddenGradients(vector<Neuron> previousLayer, vector<Neuron> nextLayer, vector<float> deltaCs);
	void updateWeights(float input, vector<Neuron> previousLayer);
	void updateHiddenWeights(vector<float> input);
#pragma endregion

private:

#pragma region privateFuncs

	void intialiseWeights();

#pragma endregion

#pragma region  parameters

	vector<float> weights;
	float activation;
	float bias;
	vector<float> gradients;
	vector<float> deltas;
	float weight_length;
	float biasGrad, oldBiasGrad;

#pragma endregion




};

