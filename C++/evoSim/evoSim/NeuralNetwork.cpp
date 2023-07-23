#include "NeuralNetwork.h"

NeuralNetwork::NeuralNetwork()
{
}

NeuralNetwork::~NeuralNetwork()
{
}
int counter = 0;
int count = 0;
void NeuralNetwork::addNeuron(int type)
{
	//std::cout << "\n" << counter << ": " << type;
	if (hid2 == false && type >= 48)
		type -= 16;

	std::vector<int>::iterator it = std::find(indexList.begin(), indexList.end(), type);
	if (it != indexList.end()) {
		return;
	}
	
	//
	indexList.push_back(type);
	neurons.push_back(new neuron);
	//
	if (type < 16) {
		inputs.push_back(neurons[neurons.size() - 1]);
		neurons[neurons.size() - 1]->tag = type;
		inTAGS.push_back(type);
	}
	else if (type < 32) {
		outputs.push_back(neurons[neurons.size() - 1]);
		neurons[neurons.size() - 1]->tag = type;
		outTAGS.push_back(type);
		//std::cout << "\nOUTED:"<<count;
		count += 1;
	}
	else if (type < 48) {
		hidden1.push_back(neurons[neurons.size() - 1]);
		neurons[neurons.size() - 1]->tag = type;
		h1TAGS.push_back(type);
	}
	else {
		hidden2.push_back(neurons[neurons.size() - 1]);
		neurons[neurons.size() - 1]->tag = type;
		h2TAGS.push_back(type);
	}
}

void NeuralNetwork::connectNeurons(int input, int output, float value)
{
	if (hid2 == false) {
		if (input >= 48)
			input -= 16;
		if (output >= 48)
			output -= 16;
	}

	//counter += 1;
	for (int i = 0; i < neurons.size(); i++) {
		if (indexList[i] == input) {
			neuron* inputNode = neurons[i];
			for (int j = 0; j < neurons.size(); j++) {
				if (indexList[j] == output) {
					neuron* outputNode = neurons[j];
					outputNode->addWeight(value);
					//std::cout << "\nvalue:" << value;
					outputNode->addInput(inputNode);
					return;
				}
			}

		}
	}
}

void NeuralNetwork::deleteNeurons() {
	
	for (int i = 0; i < hidden1.size(); i++) {
		if (hidden1[i]->outputted == false) {
			hidden1.erase(hidden1.begin() + i);
			h1TAGS.erase(h1TAGS.begin() + i);
		}
	}
	for (int i = 0; i < hidden2.size(); i++) {
		if (hidden2[i]->outputted == false) {
			hidden2.erase(hidden2.begin() + i);
			h2TAGS.erase(h2TAGS.begin() + i);
		}
	}

	for (int i = 0; i < neurons.size(); i++) {
		if (neurons[i]->outputted == false) {
			neurons[i]->~neuron();
			neurons.erase(neurons.begin() + i);
			indexList.erase(indexList.begin() + i);

		}
	}
}

void NeuralNetwork::feedFoward()
{
	//std::cout << "\nweightsLL: ";
	//for (int i = 0; i < inputs.size(); i++) {
		//inputs[i]->setActivation(1.f);
	//	std::cout << "\ninputACT " << inTAGS[i] << ": " << inputs[i]->getActivation();
	//}

	for (int i = 0; i < hidden1.size(); i++) {
		hidden1[i]->calculate();
		//std::cout << "\nhidden1act " << i << ": " << hidden1[i]->getActivation();
	}

	for (int i = 0; i < hidden2.size(); i++) {
		hidden2[i]->calculate();
		//std::cout << "\nhidden2act " << i << ": " << hidden2[i]->getActivation();
	}
	for (int i = 0; i < outputs.size(); i++) {
		outputs[i]->calculate();
		//std::cout << "\nouptputACT " << outTAGS[i] << ": " << outputs[i]->getActivation();
	}

}

std::string NeuralNetwork::displayNet(float fit)
{
	//std::cout << "YOOO";
	std::string info_vect = "\n";
	info_vect += "INPUTS::-----------------------";
	for (int i = 0; i < inputs.size(); i++) {
		if (inNames[inTAGS[i]] != "")
			info_vect +="\n" + inNames[inTAGS[i]] + ":: " + std::to_string(inputs[i]->getActivation());
	}
	//std::cout << "YOOO2";
	info_vect += "\nHIDDEN::----------------------";
	for (int i = 0; i < hidden1.size(); i++) {
		info_vect +="\nhidden1ACT " + std::to_string(i) + ": " + std::to_string(hidden1[i]->getActivation());
	}
	//for (int i = 0; i < hidden2.size(); i++) {
		//info_vect += "\nhidden2ACT " + std::to_string(i) + ": " + std::to_string(hidden2[i]->getActivation());
	//}
	info_vect += "\nOUTPUTS::----------------------";
	for (int i = 0; i < outputs.size(); i++) {
		if(outNames[outTAGS[i] - 16] != "")
			info_vect +="\n" + outNames[outTAGS[i]-16] + ":: " + std::to_string(outputs[i]->getActivation());
	}
	//std::cout << "YOOO3";
	info_vect += "\n-------------------------------";
	info_vect += "\nFITNESS:: " + std::to_string(fit);
	return info_vect;
}

void NeuralNetwork::drawNet(sf::RenderWindow& win)
{
	sf::Vector2f position(CENTER.x + 850, 200);
	sf::Vector2f offset = {};
	sf::Color color = {};
	std::vector<sf::Vector2f> pos;
	std::vector<int> indexs;
	float rader = 15.f;
	sf::Vector2f radOff(rader, rader);
	float seperation = 50.f;
	float spacing = 70.f;
	std::vector<sf::CircleShape> shapez;

	float outLEN = (outputs.size() - 1) * (seperation);
	float h1Off = outLEN - ((hidden1.size() - 1) * (seperation));
	float h2Off = outLEN - ((hidden2.size() - 1) * (seperation));
	float inOff = outLEN - ((inputs.size() - 1) * (seperation));

	for (int i = 0; i < outputs.size(); i++) {
		offset = { spacing, float(seperation * i) };
		sf::CircleShape shape(rader);
		color = sf::Color(230 * outputs[i]->getActivation() + 25, 230 * outputs[i]->getActivation() + 25, 230 * outputs[i]->getActivation() + 25);
		shape.setFillColor(color);
		shape.setPosition(position + offset);
		shapez.push_back(shape);
		pos.push_back(position + offset + radOff);
		indexs.push_back(outTAGS[i]);
	}
	for (int i = 0; i < hidden2.size(); i++) {
		offset = { 0.f, float(seperation * i) + h2Off / 2 };
		sf::CircleShape shape(rader);
		color =  sf::Color(230 * hidden2[i]->getActivation() + 25, 230 * hidden2[i]->getActivation() + 25, 230 * hidden2[i]->getActivation() + 25);
		shape.setFillColor(color);
		shape.setPosition(position + offset);
		shapez.push_back(shape);
		pos.push_back(position + offset + radOff);
		indexs.push_back(h2TAGS[i]);
	}
	for (int i = 0; i < hidden1.size(); i++) {
		offset = { -spacing, float(seperation * i) + h1Off / 2 };
		sf::CircleShape shape(rader);
		color = sf::Color(230 * hidden1[i]->getActivation() + 25, 230 * hidden1[i]->getActivation() + 25, 230 * hidden1[i]->getActivation() + 25);
		shape.setFillColor(color);
		shape.setPosition(position + offset);
		shapez.push_back(shape);
		pos.push_back(position + offset + radOff);
		indexs.push_back(h1TAGS[i]);
	}
	for (int i = 0; i < inputs.size(); i++) {
		offset = { -spacing * 2, float(seperation * i) + inOff / 2 };
		sf::CircleShape shape(rader);
		color = sf::Color(230 * inputs[i]->getActivation() + 25, 230 * inputs[i]->getActivation() + 25, 230 * inputs[i]->getActivation() + 25);
		shape.setFillColor(color);
		shape.setPosition(position + offset);
		shapez.push_back(shape);
		pos.push_back(position + offset + radOff);
		indexs.push_back(inTAGS[i]);
	}	

	//

	for (int i = 0; i < outputs.size(); i++) {

		std::vector<sf::Vector2f> tempPos;
		std::vector<sf::Color> col;

		for (int k = 0; k < outputs[i]->inputs.size(); k++) {
			for (int x = 0; x < indexs.size(); x++) {
				if(outputs[i]->inputs[k]->tag == indexs[x])
					tempPos.push_back(pos[x]);
			}

			if(outputs[i]->getWeight(k) > 0)
				col.push_back(sf::Color(0, (48 * outputs[i]->getWeight(k) + 15), 0));
			else
				col.push_back(sf::Color((48 * outputs[i]->getWeight(k) + 15), 0, 0));

		}

		for (int k = 0; k < tempPos.size(); k++) {
			sf::Vertex line[] =
			{
				sf::Vertex(pos[i]),
				sf::Vertex(tempPos[k])
			};
			line[0].color = col[k];
			line[1].color = col[k];

			win.draw(line, 2, sf::Lines);
		}
	}

	for (int i = 0; i < hidden2.size(); i++) {

		std::vector<sf::Vector2f> tempPos;
		std::vector<sf::Color> col;

		for (int k = 0; k < hidden2[i]->inputs.size(); k++) {
			for (int x = 0; x < indexs.size(); x++) {
				if (hidden2[i]->inputs[k]->tag == indexs[x])
					tempPos.push_back(pos[x]);
			}

			if (hidden2[i]->getWeight(k) > 0)
				col.push_back(sf::Color(0, (48 * hidden2[i]->getWeight(k) + 15), 0));
			else
				col.push_back(sf::Color((48 * hidden2[i]->getWeight(k) + 15), 0, 0));

		}

		for (int k = 0; k < tempPos.size(); k++) {
			sf::Vertex line[] =
			{
				sf::Vertex(pos[i]),
				sf::Vertex(tempPos[k])
			};
			line[0].color = col[k];
			line[1].color = col[k];

			win.draw(line, 2, sf::Lines);
		}
	}

	for (int i = 0; i < hidden1.size(); i++) {

		std::vector<sf::Vector2f> tempPos;
		std::vector<sf::Color> col;

		for (int k = 0; k < hidden1[i]->inputs.size(); k++) {
			for (int x = 0; x < indexs.size(); x++) {
				if (hidden1[i]->inputs[k]->tag == indexs[x])
					tempPos.push_back(pos[x]);
			}

			if (hidden1[i]->getWeight(k) > 0)
				col.push_back(sf::Color(0, (48 * hidden1[i]->getWeight(k) + 15), 0));
			else
				col.push_back(sf::Color((48 * hidden1[i]->getWeight(k) + 15), 0, 0));

		}

		for (int k = 0; k < tempPos.size(); k++) {
			sf::Vertex line[] =
			{
				sf::Vertex(pos[i]),
				sf::Vertex(tempPos[k])
			};
			line[0].color = col[k];
			line[1].color = col[k];

			win.draw(line, 2, sf::Lines);
		}
	}

	for (int i = 0; i < shapez.size(); i++) {
		win.draw(shapez[i]);
	}
}
