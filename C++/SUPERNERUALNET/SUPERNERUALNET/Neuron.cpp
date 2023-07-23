#include "Neuron.h"

#pragma region publicFuncs

Neuron::Neuron() {
	activation = 0;
	bias = 0;
	weight_length = 0;
	biasGrad = 0;
}

Neuron::~Neuron() {

}

void Neuron::Connect(vector<Neuron> previousLayer) {

	double random;
	for (int i = 0; i < previousLayer.size(); i++) {
		random = rand() % 201;
		weights.push_back((random - 100)/100);
		deltas.push_back(0.01);
		gradients.push_back(0.01);
	}

	random = rand() % 201;
	bias = (random - 100) / 100;
	weight_length = weights.size();
	
}

void Neuron::calculateActivation(vector<Neuron> previousLayer) {
	float sum = 0;
	for (int i = 0; i < previousLayer.size(); i++) {
		sum = sum + (previousLayer[i].getActivation() * weights[i]);

	}
	activation = activationFunction(sum + bias);		
}

float Neuron::activationFunction(float input) {
	return 1 / (1 + exp(-input));
}

float Neuron::activationDerivative(float input){
	return input * (1 - input);
}

void Neuron::setActivation(double input) {
	activation = input;
}

float Neuron::getActivation() {
	return activation;
}

void Neuron::setBias(double input) {
	bias = input;
}

float Neuron::getBias() {
	return bias;
}

void Neuron::setWeight(float input, int index) {
	weights[index] = input;
}

float Neuron::getWeight(int index) {
	return weights[index];
}

void Neuron::setDelta(float input, int index) {
	deltas[index] = input;
}

float Neuron::getDelta(int index) {
	return deltas[index];
}

void Neuron::setGradient(float input, int index) {
	gradients[index] = input;
}

float Neuron::getGradient(int index) {
	return gradients[index];
}

void Neuron::showWeights() {

	cout << "\nWEIGHTS:-------------------";
	for (int i = 0; i < weights.size(); i++) {
		cout << "\n";
		cout.width(3);
		cout << i << ": " << weights[i];
	}

	cout << "\n";
	cout << "bias: " << bias;

}

void Neuron::showGradients() {

	cout << "\nGRADIENTS:-----------------";
	for (int i = 0; i < gradients.size(); i++) {
		cout << "\n";
		cout.width(3);
		cout << i << ": " << gradients[i];
	}

}

void Neuron::showDeltas() {

	cout << "\nDELTAS:--------------------";
	for (int i = 0; i < deltas.size(); i++) {
		cout << "\n";
		cout.width(3);
		cout << i << ": " << deltas[i];
	}

}


void Neuron::calculateOutputGradients(vector<Neuron> previousLayer) {
	//cout << "\ngrads";
	float deltaActivation = activationDerivative(activation);
	float deltaSum = 0;
	for (int i = 0; i < previousLayer.size(); i++) {
		deltaSum = previousLayer[i].getActivation();
		setGradient(deltaSum * deltaActivation, i);
	}

	biasGrad = deltaActivation;
}

void Neuron::calculateHiddenGradients(vector<Neuron> previousLayer, vector<Neuron> nextLayer, vector<float> deltaCs) {
	
	
	
	float deltaActivation1 = activationDerivative(activation);
	float deltaSum = 0;
	for (int i = 0; i < previousLayer.size(); i++) {
		deltaSum = previousLayer[i].getActivation();
		setGradient(deltaSum * deltaActivation1, i);
	}
}

void Neuron::updateWeights(float input, vector<Neuron> previousLayer) {

	float oldDW, newDW;
	//cout << "\nweigths";
	for (int i = 0; i < weight_length; i++) {
		oldDW = deltas[i];
		newDW = previousLayer[i].getActivation() * gradients[i] * input * 0.1 + oldDW * 0.05;
		weights[i] += newDW;
		deltas[i] = newDW;
	}
	oldBiasGrad = biasGrad;
	float newBiasGrad = biasGrad * input * 0.1 + oldBiasGrad * 0.05;
	bias += newBiasGrad;
	biasGrad = newBiasGrad;
}

void Neuron::updateHiddenWeights(vector<float> input) {

	float oldDW, newDW;
	//cout << "\nweigths";
	for (int i = 0; i < weight_length; i++) {
		oldDW = deltas[i];
		//newDW = gradients[i] * input;
		newDW = 0;
		weights[i] += newDW;
		deltas[i] = newDW;
	}

	//bias += biasGrad * input;
}

#pragma endregion


#pragma region privateFuncs

void Neuron::intialiseWeights() {

}

#pragma endregion

