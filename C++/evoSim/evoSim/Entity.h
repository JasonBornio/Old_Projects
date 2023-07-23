#pragma once
#include <SFML/Graphics.hpp>
#include <vector>
#include <iostream>
#include "globalItems.h"
#define M_PI 3.14159265358979323846


class Entity
{
protected:
	//std::vector<sf::CircleShape>& shapesVector;
	float radius = 20.f;
	float force = .5f;
	std::vector<float> inputValues;
	std::vector<float> outputValues;
	std::vector<std::vector<int>> DNA = {};

public:
	Entity(std::vector<sf::CircleShape>& shapes, float radius, sf::Vector2f position);
	~Entity();
	sf::Vector2f position_current;
	sf::Vector2f position_old;
	sf::Vector2f velocity;
	sf::Vector2f acceleration;
	sf::CircleShape shape;
	int index = 0;

	void updatePosition(float dt);
	void accelerate(sf::Vector2f acc);
	float getRadius();
	void setRadius(float rad);
	float getForce();
	float getArea();
	void randomDNA(int numberOfgenes);
	std::vector<std::vector<int>> getDNA();
	void setDNA(std::vector<std::vector<int>> newDNA);
	void setDNA(std::vector<std::vector<int>> newDNA, float mut_chance);
	void mixDNA(float mut_chance, std::vector<std::vector<int>> newDNA, std::vector<std::vector<int>> newDNA2);
};

