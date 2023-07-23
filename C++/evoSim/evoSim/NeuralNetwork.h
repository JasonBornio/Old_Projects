#pragma once
#include <vector>
#include <algorithm> // for find()
#include "neuron.h"
#include <iostream>
#include <SFML/Graphics.hpp>
#include "globalItems.h"
class NeuralNetwork
{
public:
	std::vector<neuron*>neurons;
	std::vector<int> indexList;
	NeuralNetwork();
	~NeuralNetwork();
	void addNeuron(int type);
	void connectNeurons(int input, int output, float value);
	void feedFoward();
	std::string displayNet(float fit);
	void drawNet(sf::RenderWindow& win);
	void deleteNeurons();
	//0-15 inputs
	//16-31 outputs
	//32-47 hidden
	//48-32 hidden2
private:
	std::vector<neuron*> hidden1;
	std::vector<neuron*> hidden2;
	std::vector<neuron*> inputs;
	std::vector<neuron*> outputs;
	std::vector<int> outTAGS;
	std::vector<int> inTAGS;
	std::vector<int> h1TAGS;
	std::vector<int> h2TAGS;
	std::vector<std::string> inNames = { "age", "naturalfreq", "velocityX", "velocityY", "fitness", "positionX", "positionY", "FphermoneIn", "HphermoneIn", "angle", "", "", "", "", "", "",""};
	std::vector<std::string> outNames = { "forward", "backward", "rotleft", "rotright", "vibrate", "moveSpeed", "rotSpeed", "freqMult", "left", "right", "", "", "", "", "", "" ,""};

};

