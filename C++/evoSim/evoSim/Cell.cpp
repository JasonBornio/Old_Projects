#include "Cell.h"

int bitsToInt(std::vector<int>& input) {
	int sum = 0;
	for (int i = 0; i < input.size(); i++) {
		if (input[i] == 1)
			sum += pow(2, i);
	}
	return sum;
}

void Cell::decodeDNA()
{
	for (int i = 0; i < DNA.size(); i++) {
		if (DNA[i][0] == 0 || true) {

			int source1 = DNA[i][1];
			int layer1 = DNA[i][2];
			int source2 = DNA[i][14];
			int layer2 = DNA[i][15];

			std::vector<int> temp = {};

			temp = std::vector<int>(DNA[i].begin()+3, DNA[i].begin() +3 + 4);
			int inputNodeType = bitsToInt(temp);

			temp = std::vector<int>(DNA[i].begin() + 7, DNA[i].begin() + 7 + 7);
			int inputNodeID = bitsToInt(temp);

			temp = std::vector<int>(DNA[i].begin() + 16, DNA[i].begin() + 16 + 4);
			int outputNodeType = bitsToInt(temp);

			temp = std::vector<int>(DNA[i].begin() + 20, DNA[i].begin() + 20 + 7);
			int outputNodeID = bitsToInt(temp);

			temp = std::vector<int>(DNA[i].begin() + 27, DNA[i].begin() + 21 + 27);
			float weight = (((float)bitsToInt(temp)-1048576)/262144);
			
			int offset = 0;
			int outoffset = 0;
			if (source1==0) {
				brain.addNeuron(inputNodeType);
			}
			else {
				if (layer1 == 0) {
					offset = 32;
					brain.addNeuron(inputNodeType+ offset);
				}
				else {
					offset = 48;
					brain.addNeuron(inputNodeType + offset);
				}
			}
			//
			if (source2==0) {
				if (layer2==0) {
					outoffset = 32;
					brain.addNeuron(outputNodeType + outoffset);
				}
				else {
					outoffset = 48;
					brain.addNeuron(outputNodeType + outoffset);
				}
			}
			else {
				outoffset = 16;
				brain.addNeuron(outputNodeType + outoffset);
			}
			//
			brain.connectNeurons(inputNodeType + offset, outputNodeType + outoffset, weight);
		}
	}
	//brain.deleteNeurons();
}

void Cell::handleInputs(std::vector<pheromone*>& global_pher)
{
	//input funcs
	age();
	//

	std::vector<int>& list = brain.indexList;

	std::vector<int>::iterator it = std::find(list.begin(), list.end(), 0);
	if (it != list.end()) {
		int index = it - list.begin();
		brain.neurons[index]->setActivation(_age/1000);
	}

	it = std::find(list.begin(), list.end(), 1);
	if (it != list.end()) {
		int index = it - list.begin();
		brain.neurons[index]->setActivation(naturalVibration());
	}

	it = std::find(list.begin(), list.end(), 2);
	if (it != list.end()) {
		int index = it - list.begin();
		brain.neurons[index]->setActivation(velocity.x/(RADIUS*2));
	}

	it = std::find(list.begin(), list.end(), 3);
	if (it != list.end()) {
		int index = it - list.begin();
		brain.neurons[index]->setActivation(velocity.y/(RADIUS * 2));
	}

	it = std::find(list.begin(), list.end(), 4);
	if (it != list.end()) {
		int index = it - list.begin();
		brain.neurons[index]->setActivation(fitness/100);
	}

	it = std::find(list.begin(), list.end(), 5);
	if (it != list.end()) {
		int index = it - list.begin();
		brain.neurons[index]->setActivation(position_current.x / (RADIUS * 2));
	}

	it = std::find(list.begin(), list.end(), 6);
	if (it != list.end()) {
		int index = it - list.begin();
		brain.neurons[index]->setActivation(position_current.y / (RADIUS * 2));
	}

	it = std::find(list.begin(), list.end(), 7);
	if (it != list.end()) {
		int index = it - list.begin();
		brain.neurons[index]->setActivation(friendlyPhermoneIntensity(global_pher));
	}

	it = std::find(list.begin(), list.end(), 8);
	if (it != list.end()) {
		int index = it - list.begin();
		brain.neurons[index]->setActivation(hostilePhermoneIntensity(global_pher));
	}

	it = std::find(list.begin(), list.end(), 9);
	if (it != list.end()) {
		int index = it - list.begin();
		brain.neurons[index]->setActivation(angle);
	}

	brain.feedFoward();

}

//sensors
float Cell::age() {
	_age = _age + 1;
	return _age;
}

float Cell::naturalVibration() {
	return sin(_age * natural_frequency * frequency_mult);
}

void Cell::resetActions() {
	move_forward = false;
	move_backward = false;
	rotate_left = false;
	rotate_right = false;
	release_energy = false;
	produce_light = false;
	contract_muscles = false;
	_vibrate = false;
	release_pheromone = false;
	move_left = false;
	move_right = false;
}

void Cell::handleOutputs(std::vector<pheromone*>& global_pher) {

	resetActions();
	std::vector<int>& list = brain.indexList;

	std::vector<int>::iterator it = std::find(list.begin(), list.end(), 16);
	if (it != list.end()) {
		int index = it - list.begin();
		if (brain.neurons[index]->getActivation() > activation_threshold)
			move_forward = true;
	}

	it = std::find(list.begin(), list.end(), 17);
	if (it != list.end()) {
		int index = it - list.begin();
		if (brain.neurons[index]->getActivation() > activation_threshold)
			move_backward = true;
	}

	it = std::find(list.begin(), list.end(), 18);
	if (it != list.end()) {
		int index = it - list.begin();
		if (brain.neurons[index]->getActivation() > activation_threshold)
			rotate_left = true;
	}

	it = std::find(list.begin(), list.end(), 19);
	if (it != list.end()) {
		int index = it - list.begin();
		if (brain.neurons[index]->getActivation() > activation_threshold)
			rotate_right = true;
	}

	it = std::find(list.begin(), list.end(), 20);
	if (it != list.end()) {
		int index = it - list.begin();
		if (brain.neurons[index]->getActivation() > activation_threshold)
			_vibrate = true;
	}

	it = std::find(list.begin(), list.end(), 21);
	if (it != list.end()) {
		int index = it - list.begin();
		move_speed = brain.neurons[index]->getActivation();
		if (brain.neurons[index]->getActivation() > activation_threshold)
			release_energy = true;
	}

	it = std::find(list.begin(), list.end(), 22);
	if (it != list.end()) {
		int index = it - list.begin();
		rotation_speed = brain.neurons[index]->getActivation();
		if (brain.neurons[index]->getActivation() > activation_threshold)
			produce_light = true;
	}

	it = std::find(list.begin(), list.end(), 23);
	if (it != list.end()) {
		int index = it - list.begin();
		frequency_mult = brain.neurons[index]->getActivation();
		if (brain.neurons[index]->getActivation() > activation_threshold)
			contract_muscles = true;
	}

	it = std::find(list.begin(), list.end(), 24);
	if (it != list.end()) {
		int index = it - list.begin();
		if (brain.neurons[index]->getActivation() > activation_threshold)
			release_pheromone = true;
	}

	it = std::find(list.begin(), list.end(), 25);
	if (it != list.end()) {
		int index = it - list.begin();
		if (brain.neurons[index]->getActivation() > activation_threshold)
			move_left = true;
	}

	it = std::find(list.begin(), list.end(), 26);
	if (it != list.end()) {
		int index = it - list.begin();
		if (brain.neurons[index]->getActivation() > activation_threshold)
			move_right = true;
	}

	sf::Vector2f vect = { cos(angle), sin(angle) };
	float dist = sqrt((movement_vector.x * movement_vector.x) + (movement_vector.y * movement_vector.y));
	sf::Vector2f vect2 = { cos(angle + (float)(M_PI / 4)), sin(angle + (float)(M_PI / 4)) };
	float dist2 = sqrt((movement_vector2.x * movement_vector2.x) + (movement_vector2.y * movement_vector2.y));
	movement_vector = vect / dist;
	movement_vector2 = vect2 / dist2;

	//ouput funcs
	if (move_forward)
		moveForward();
	if (move_backward)
		moveBackward();
	if (rotate_left)
		rotateLeft();
	if (rotate_right)
		rotateRight();
	if (_vibrate)
		vibrate();
	if (release_energy)
		releaseEnergy();
	if (produce_light)
		produceLight();
	if (contract_muscles)
		contractMuscle();
	if (release_pheromone)
		releasePhermone(global_pher);
	if (move_left)
		moveLeft();
	if (move_right)
		moveRight();
}

//actions
//1
void Cell::moveForward() {
	this->accelerate(movement_vector * move_speed * max_move_speed);
	//std::cout << "\nMOVE forward";
}
//2
void Cell::moveBackward() {
	this->accelerate(movement_vector * -move_speed * max_move_speed);
	//std::cout << "\nMOVE back";
}

void Cell::moveLeft() {
	this->accelerate(movement_vector2 * move_speed * max_move_speed);
	//std::cout << "\nMOVE forward";
}
//2
void Cell::moveRight() {
	this->accelerate(movement_vector2 * -move_speed * max_move_speed);
	//std::cout << "\nMOVE back";
}
//3
void Cell::rotateLeft() {
	angle += -rotation_speed * max_rotation_speed;
	//std::cout << "\nROTATE left";
	if (angle < 0)
		angle += M_PI;
	else if (angle >= M_PI)
		angle -= M_PI;
}
//4
void Cell::rotateRight() {
	angle += rotation_speed * max_rotation_speed;
	if (angle >= M_PI)
		angle -= M_PI;
	else if (angle < 0)
		angle += M_PI;
	//std::cout << "\nROTATE right";
}
//5
void Cell::vibrate() {
	this->accelerate(naturalVibration() * sf::Vector2f((rand()% 1001)/1000, (rand() % 1001) / 1000));
}
//6
void Cell::releaseEnergy() {

}
//7
void Cell::produceLight() {

}
//8
void Cell::contractMuscle() {

}

void Cell::releasePhermone(std::vector<pheromone*>& global_pher) {
	if (global_pher.size() < phermoneCount && naturalVibration() > 0.99) {
		global_pher.push_back(new pheromone);
		global_pher[global_pher.size() - 1]->position = position_current;
		global_pher[global_pher.size() - 1]->tag = tag;
	}
}

void Cell::checkFitness(float elapsed_time)
{
	sf::Vector2f zero(0.f, 0.f);
	float dist = sqrt((velocity.x * velocity.x) + (velocity.y * velocity.y));
	if (elapsed_time < 5.f) {
		//fitness += (position_current.y - CENTER.y) / RADIUS;
		if (position_current.y > CENTER.y)
			fitness += dist;
		else
			fitness -= 0;// 1;
	}
	else if (elapsed_time < 10.0f) {
		if (position_current.y > CENTER.y)
			fitness -= 0;// 1;
		else
			fitness += dist;
	}
	else if (elapsed_time < 15.0f) {
		if (position_current.x > CENTER.x)
			fitness += dist;
		else
			fitness -= 0;// 1;
	}
	else if (elapsed_time < 20.0f) {
		if (position_current.x > CENTER.x)
			fitness -= 0;// 1;
		else
			fitness += dist;
	}
	if (elapsed_time > 1.f) {
		if (velocity == zero)
			fitness -= 10.f;
	}


}

void Cell::setColour(std::vector<sf::CircleShape>& shapes)
{
	int red = 0;
	int green = 0;
	int blue = 0;
	std::vector<int> temp = {};

	//std::cout << "\nHey10";
	for (int i = 0; i < DNALENGTH; i++) {
		temp = std::vector<int>(DNA[i].begin() + 1, DNA[i].begin() + 1 + 21);
		red += bitsToInt(temp);
	}
	//std::cout << "\nHey11";
	red /= (DNALENGTH * DEFINITION);

	for (int i = 0; i < DNALENGTH; i++) {
		temp = std::vector<int>(DNA[i].begin() + 22, DNA[i].begin() + 22 + 21);
		green += bitsToInt(temp);
	}
	//std::cout << "\nHey12";
	green /= (DNALENGTH * DEFINITION);

	for (int i = 0; i < DNALENGTH; i++) {
		temp = std::vector<int>(DNA[i].begin() + 43, DNA[i].begin() + 43 + 21);
		blue += bitsToInt(temp);
	}
	blue /= (DNALENGTH * DEFINITION);

	shapes[index].setFillColor(sf::Color(red, blue, green));
}

void Cell::setColour(std::vector<sf::CircleShape>& shapes, sf::Color colour)
{
	shapes[index].setFillColor(colour);
}

std::string Cell::displayDNA()
{
	//std::cout << "YOOO";
	std::string info_vect = "\n";
	info_vect += "DNA::--------------------------";
	int count = 0;

	std::string gene1;
	std::string gene2;
	std::string gene3;
	std::string gene4;		
	std::vector<int> temp = {};	
	std::ostringstream ss;

	for (int i = 0; i < DNALENGTH; i++) {
		temp = std::vector<int>(DNA[i].begin(), DNA[i].begin() + 16);
		ss.str("");
		ss.clear();
		ss << std::hex << bitsToInt(temp);
		gene1 = ss.str();

		temp = std::vector<int>(DNA[i].begin() + 16, DNA[i].begin() + 32);
		ss.str("");
		ss.clear();
		ss << std::hex << bitsToInt(temp);
		gene2 = ss.str();

		temp = std::vector<int>(DNA[i].begin() + 32, DNA[i].begin() + 48);
		ss.str("");
		ss.clear();
		ss << std::hex << bitsToInt(temp);
		gene3 = ss.str();

		temp = std::vector<int>(DNA[i].begin() + 48, DNA[i].begin() + 64);
		ss.str("");
		ss.clear();
		ss << std::hex << bitsToInt(temp);
		gene4 = ss.str();

		info_vect += "\n" + gene1 + "=" + gene2 + "=" + gene3 + "=" + gene4;
	}
	return info_vect;
}

float Cell::friendlyPhermoneIntensity(std::vector<pheromone*>& global_pher) {
	float radius = 200.f;
	float sum = 0;

	if (tag < tagOffset) {
		for (int i = 0; i < global_pher.size(); i++) {
			pheromone* phe = global_pher[i];
			if (phe->tag < tagOffset && phe->tag != tag) {
				sf::Vector2f to_phe = position_current - phe->position;
				float dist = std::sqrtf(to_phe.x * to_phe.x + to_phe.y * to_phe.y);

				if (dist < radius) {
					sum += ((phe->intensity)* 100/(dist+0.01))/radius;
				}
			}
		}
	}
	else {
		for (int i = 0; i < global_pher.size(); i++) {
			pheromone* phe = global_pher[i];
			if (phe->tag >= tagOffset && phe->tag != tag) {
				sf::Vector2f to_phe = position_current - phe->position;
				float dist = std::sqrtf(to_phe.x * to_phe.x + to_phe.y * to_phe.y);

				if (dist < radius) {
					sum += ((phe->intensity) * 100 / (dist + 0.01)) / radius;
				}
			}
		}
	}
	//std::cout << "\nphers:" << global_pher.size();
	//std::cout << "\nintensity:" << sum;
	return sum;
}

float Cell::hostilePhermoneIntensity(std::vector<pheromone*>& global_pher) {
	float radius = 200.f;
	float sum = 0;

	if (tag < tagOffset) {
		for (int i = 0; i < global_pher.size(); i++) {
			pheromone* phe = global_pher[i];
			if (phe->tag >= tagOffset && phe->tag != tag) {
				sf::Vector2f to_phe = position_current - phe->position;
				float dist = std::sqrtf(to_phe.x*to_phe.x + to_phe.y * to_phe.y);

				if (dist < radius) {
					sum += ((phe->intensity) * 100 / (dist + 0.01)) / radius;
				}
			}
		}
	}
	else{
		for (int i = 0; i < global_pher.size(); i++) {
			pheromone* phe = global_pher[i];
			if (phe->tag < tagOffset && phe->tag != tag) {
				sf::Vector2f to_phe = position_current - phe->position;
				float dist = std::sqrtf(to_phe.x * to_phe.x + to_phe.y * to_phe.y);

				if (dist < radius) {
					sum += ((phe->intensity) * 100 / (dist + 0.01)) / radius;
				}
			}
		}
	}
	//std::cout << "\nintensity:" << sum;
	return sum;
}

void Cell::setTag(int input, std::vector<Cell*>& global_pre, std::vector<Cell*>& global_pred) {
	tag = input;
	if (tag >= tagOffset) {
		global_pred.push_back(this);
		cooldown = 3.f;
	}
	else {
		global_pre.push_back(this);
		cooldown = 5.f;
	}

}

void Cell::eat(std::vector<Cell*>& targets, float time) {
	float range = creature_radius + 5.f;
	for (int i = 0; i < targets.size(); i++) {
		sf::Vector2f to_target = position_current - targets[i]->position_current;
		float dist = std::sqrtf(to_target.x * to_target.x + to_target.y * to_target.y);
		if (dist < range && targets[i]->dead == false) {
			//std::cout << "\nHEYO6";
			initial_time = time;
			energy = 60.f;
			hunger += 1;
			targets[i]->dead = true;
			return;
		}

	}
}

void Cell::divide(std::vector<sf::CircleShape>& shapes, float time, std::vector<Cell*>& targets, std::vector<Cell*>& global_pre, std::vector<Cell*>& global_pred, std::vector<pheromone*>& global_pher) {
	
	if (tag >= tagOffset) {
		if (global_pred.size() < predatorCount && hunger >= 1) {
			//std::cout << "\nHEYO7";
			hunger = 0;
			sf::Vector2f offset(((rand() % 200) - 100) / 10, ((rand() % 200) - 100) / 20);
			targets.push_back(new Cell(shapes, creature_radius, position_current+ offset));
			targets[targets.size() - 1]->setDNA(getDNA(),mutation_chance);
			targets[targets.size() - 1]->setColour2(shapes);
			targets[targets.size() - 1]->decodeDNA();
			targets[targets.size() - 1]->setTag(tagOffset + global_pred.size() - 1, global_pre, global_pred);
			targets[targets.size() - 1]->energy_counter = time;

		}
	}
	else {
		releasePhermone(global_pher);
		if (global_pre.size() < populationCount && (time - initial_time > cooldown)) {
			//std::cout << "\nSize"<<global_pre.size();
			sf::Vector2f offset(((rand() % 200) - 100) / 10, ((rand() % 200) - 100) / 20);
			initial_time = time;
			targets.push_back(new Cell(shapes, creature_radius, position_current+offset));
			//std::cout << "\nHEYO9";
			//std::cout << "\nSIZE::" << DNA.size();
			//std::cout << "\nSIZET::" << targets.size();
			targets[targets.size() - 1]->setDNA(getDNA(), mutation_chance);
			//std::cout << "\nHEY10";
			targets[targets.size() - 1]->setColour2(shapes);
			//std::cout << "\nHEY11";
			targets[targets.size() - 1]->decodeDNA();
			//std::cout << "\nHEY12";
			targets[targets.size() - 1]->setTag(global_pre.size() - 1, global_pre, global_pred);
			targets[targets.size() - 1]->initial_time = time;
			//std::cout << "\nHEY13";
		}
	}
}

void Cell::update(float time, std::vector<Cell*>& targets, std::vector<sf::CircleShape>& shapes, std::vector<Cell*>& global_pre, std::vector<Cell*>& global_pred, std::vector<pheromone*>& global_pher) {

	if (tag >= tagOffset) {
		if (time - energy_counter > 1.f) {
			energy_counter = time;
			energy -= energy_decay;
			releasePhermone(global_pher);
		}
		if (time - initial_time > cooldown) {
			//std::cout << "\nHEYO3";
			eat(global_pre, time);
			//std::cout << "\nHEYO4";
		}
	}

	//std::cout << "\nHEYO5";
	divide(shapes, time, targets,global_pre,global_pred,global_pher);
	//std::cout << "\nHEYO6";
	//
	handleInputs(global_pher);
	//std::cout << "\nYOLO1";
	handleOutputs(global_pher);
	//std::cout << "\nYOLO2";
	//checkFitness(time);
	//if (tag == 0) {
	//	std::cout << "\nPhers:" << pheromones.size();
	//}
}

void Cell::setColour2(std::vector<sf::CircleShape>& shapes)
{
	int red = 0;
	std::vector<int> temp = {};

	//std::cout << "\nHey14";
	for (int i = 0; i < DNALENGTH; i++) {
		//std::cout << "\nHey19";
		temp = std::vector<int>(DNA[i].begin() + 1, DNA[i].begin() + 64);
		//std::cout << "\nHey20";
		red += bitsToInt(temp);
	}
	//std::cout << "\nHey15";
	red /= (DNALENGTH * 3 * DEFINITION);

	if(tag>=tagOffset)
		shapes[index].setFillColor(sf::Color(red, 128, 128));
	else
		shapes[index].setFillColor(sf::Color(128, red, 128));
	//std::cout << "\nHey18";
}

std::string Cell::displayStats()
{
	//std::cout << "YOOO";
	std::string info_vect = "\nSTATS::---------";
	info_vect += "\ntag::" + std::to_string(tag);	
	info_vect += "\nindex::" + std::to_string(index);
	info_vect += "\nage::" + std::to_string(_age);
	info_vect += "\nhunger::" + std::to_string(hunger);
	info_vect += "\nenergy::" + std::to_string(energy);
	return info_vect;
}