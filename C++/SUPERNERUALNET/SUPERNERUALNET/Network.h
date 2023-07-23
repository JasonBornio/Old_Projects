#pragma once
#include "Neuron.h"

using namespace std;


class Network
{
public:

#pragma region publicFuncs

	Network(int inputs, int outputs, int num_layers, int layerNodes);
	~Network();
	void Train(vector<vector<float>> inputs, vector<vector<float>> labels , int iterations, bool show);

#pragma endregion

private:

#pragma region privateFuncs

	void Create();
	vector<float> FeedForward(vector<float> inputs);
	void BackPropagate(vector<float> predictions, vector<float> labels);
	float LossFucntion(vector<float> predictions, vector<float> labels);
	float lossDerivative(float prediciton, float label);
	float nextSUM(vector<Neuron> nextLayer);

	
#pragma endregion

#pragma region  parameters

	int input_length;
	int output_length;
	int layers;
	int layer_length;
	vector<Neuron> input_nodes;
	vector<Neuron> output_nodes;
	vector<vector<Neuron>> layer_nodes;
	int iterations = 10;

#pragma endregion




};

