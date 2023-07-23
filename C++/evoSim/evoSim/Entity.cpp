#include "Entity.h"

Entity::Entity(std::vector<sf::CircleShape>& shapes, float rad, sf::Vector2f position)
{
	radius = rad;
	sf::CircleShape circle(radius);
	shape = circle;
	position_current = sf::Vector2f(position);
	position_old = position_current;
	shape.setPosition(position_current);
	shape.setFillColor(sf::Color::Green);
	//index = shapes.size();
	shapes.push_back(shape);
	index = shapes.size() -1;
	//shapesVector = shapes;

}

Entity::~Entity()
{
}

void Entity::updatePosition(float dt)
{
	velocity = position_current - position_old;
	position_old = position_current;
	position_current = position_current + velocity + acceleration * dt * dt;
	acceleration = {};
}

void Entity::accelerate(sf::Vector2f acc)
{
	acceleration += acc;
}

float Entity::getRadius()
{
	return radius;
}

void Entity::setRadius(float rad)
{
	radius = rad;
}

float Entity::getForce()
{
	return force;
}

float Entity::getArea()
{
	return float(M_PI * (radius * radius));
}

void Entity::randomDNA(int numberOfgenes)
{
	for (int i = 0; i < numberOfgenes; i++){
		std::vector<int> gene = {};
		//std::cout << "\ngene " << i << ": ";
		for (int k = 0; k < 64; k++) {
			gene.push_back(rand() % 2);
			//std::cout << gene[k];
		}
		DNA.push_back(gene);
	}
}

std::vector<std::vector<int>> Entity::getDNA()
{
	return DNA;
}

void Entity::setDNA(std::vector<std::vector<int>> newDNA)
{
	DNA = newDNA;
}

void Entity::mixDNA(float mut_chance, std::vector<std::vector<int>> newDNA, std::vector<std::vector<int>> newDNA2)
{
	DNA = {};
	float random = 0;
	std::vector<int> new_gene;

	for (int i = 0; i < newDNA.size(); i++) {
		if (rand() % 2 == 1) {
			new_gene = newDNA[i];
		}
		else {
			new_gene = newDNA2[i];
		}

		random = (rand() % 1001) / 1000;

		if (random < mut_chance) {
			int random_index = rand() % new_gene.size();
			if (new_gene[random_index] == 1)
				new_gene[random_index] = 0;
			else
				new_gene[random_index] = 1;
		}

		DNA.push_back(new_gene);
	}
}

void Entity::setDNA(std::vector<std::vector<int>> newDNA, float mut_chance) {
	DNA = newDNA;
	//std::cout<<"\nHEEYYYYYYYYYYY0OOO\n";
	//std::cout << DNA.size();
	float random = 0;
	for (int i = 0; i < DNA.size(); i++) {
		random = (rand() % 1001) / 1000;
		if (random < mut_chance) {
			int random_index = rand() % DNA[i].size();
			if (DNA[i][random_index] == 1)
				DNA[i][random_index] = 0;
			else
				DNA[i][random_index] = 1;
		}
		//for (int k = 0; k < 64; k++)
			//std::cout << DNA[i][k];

	}
}
