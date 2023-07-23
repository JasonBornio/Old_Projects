#include "neuron.h"

float sigmoid(float input) {
	return 1 / (1 + exp(-input));
}

float ReLU(float input) {
	if (input < 0)
		return 0;
	else
		return input;
}

float ThresHold = 1000.f;

float clippedReLU(float input) {
	if (input < 0)
		return 0;
	else if (input > ThresHold)
		return ThresHold;
	else
		return input;
}

neuron::neuron() {
	bias = 0;
	activation = 0;
	weightLength = 0;
	outputted = false;
}
neuron::~neuron() {

}
void neuron::setWeight(int index, float value) {
	weights[index] = value;
}
float neuron::getWeight(int index)
{
	return weights[index];
}
void neuron::addWeight(float value) {
	weights.push_back(value);
	weightLength += 1;
}
void neuron::calculate() {
	float sum = 0.f;
	for (int i = 0; i < weightLength; i++) {
		sum += weights[i] * inputs[i]->getActivation();
	}
	activation = sigmoid(sum + bias);
}
float neuron::getActivation() {
	return activation;
}
void neuron::setActivation(float act) {
	activation = act;
}
void neuron::addInput(neuron* node) {
	inputs.push_back(node);
	node->outSet();
}

void neuron::outSet() {
	outputted = true;
}