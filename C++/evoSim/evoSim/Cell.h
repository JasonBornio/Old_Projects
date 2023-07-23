#pragma once
#include "Entity.h"
#include "NeuralNetwork.h"
#include "Utilities.h"
#include "globalItems.h"
#include <algorithm> // for find()
#include <sstream>

struct pheromone {
	sf::Vector2f position;
	float decay_rate = 0.05f;
	float intensity = 1.f;
	bool destroy = false;
	int tag;

	void update() {
		intensity -= (intensity * decay_rate);

		if (intensity < 0.001f)
			destroy = true;
	}
};

class Cell : public Entity
{
private:

	float natural_frequency = 5.f;
	float frequency_mult = 0.1f;
	float angle = M_PI / 2;
	sf::Vector2f movement_vector = {cos(angle), sin(angle)};
	sf::Vector2f movement_vector2 = { cos(angle + M_PI/4), sin(angle + M_PI / 4) };
	float max_move_speed = 2500.f;
	float max_rotation_speed = 5.f;
	float move_speed = .2f;
	float rotation_speed = .1f;
	//sensors
	float age();
	float naturalVibration();
	float friendlyPhermoneIntensity(std::vector<pheromone*>& global_pher);
	float hostilePhermoneIntensity(std::vector<pheromone*>& global_pher);

	float activation_threshold = 0.90f;
	bool move_forward = false;
	bool move_backward = false;
	bool rotate_left = false;
	bool rotate_right = false;
	bool release_energy = false;
	bool release_pheromone = false;
	bool produce_light = false;
	bool contract_muscles = false;
	bool _vibrate = false;
	bool move_left = false;
	bool move_right = false;

	void resetActions();
	//actions
	void moveLeft();
	void moveRight();
	void moveForward();
	void rotateLeft();
	void rotateRight();
	void moveBackward();
	void releaseEnergy();
	void produceLight();
	void contractMuscle();
	void vibrate();
	void releasePhermone(std::vector<pheromone*>& global_pher);

	float energy_counter = 0.f;

public:
	NeuralNetwork brain;
	using Entity::Entity;
	std::vector<float> inputValues;
	std::vector<float> outputValues;
	void decodeDNA();
	void handleInputs(std::vector<pheromone*>& global_pher);
	void handleOutputs(std::vector<pheromone*>& global_pher);
	void checkFitness(float elapsed_time);
	void setColour(std::vector<sf::CircleShape>& shapes);
	void setColour2(std::vector<sf::CircleShape>& shapes);
	void setColour(std::vector<sf::CircleShape>& shapes, sf::Color colour);
	std::string displayDNA();
	void setTag(int input, std::vector<Cell*>& global_pre, std::vector<Cell*>& global_pred);
	void eat(std::vector<Cell*>& targets, float time);
	void update(float time, std::vector<Cell*>& targets, std::vector<sf::CircleShape>& shapes, std::vector<Cell*>& global_pre, std::vector<Cell*>& global_pred, std::vector<pheromone*>& global_pher);
	void divide(std::vector<sf::CircleShape>& shapes, float time, std::vector<Cell*>& targets, std::vector<Cell*>& global_pre, std::vector<Cell*>& global_pred, std::vector<pheromone*>& global_pher);
	std::string displayStats();
	float fitness = 0;
	bool dead = false;
	float energy = 60.f;
	float energy_decay = 2.f;
	int cooldown = 3.f;
	float hunger = 0.f;
	float _age = 0;
	int tag = 0;
	float initial_time = 0.f;


};