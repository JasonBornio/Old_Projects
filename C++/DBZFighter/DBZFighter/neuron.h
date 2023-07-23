#pragma once
#include<vector>

class neuron
{
private:
	std::vector<float> weights;
	float activation;
	float bias;
protected:
public:
	neuron();
	~neuron();
	void setWeight(int index, float value);
	float getWeight(int index);
	void addWeight(float value);
	void calculate();
	float getActivation();
	void setActivation(float act);
	void addInput(neuron* node);
	int weightLength;
	std::vector<neuron*> inputs;
	int tag;
	bool outputted;
	void outSet();
};
