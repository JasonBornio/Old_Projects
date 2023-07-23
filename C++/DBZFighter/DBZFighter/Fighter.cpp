#include "Fighter.h"

Fighter::Fighter(std::vector<RectangleShape>& shapes, Vector2f position)
{
	RectangleShape player(HITBOX);
	hitbox = player;
	position_current = Vector2f(position);
	position_old = position_current;
	hitbox.setPosition(position_current);
	hitbox.setFillColor(Color::Green);
	shapes.push_back(hitbox);
	index = shapes.size() - 1;

}

Fighter::~Fighter()
{
}

void Fighter::updatePosition(float dt, int substeps)
{
	if (jumped)
		jumped = false;
	else
		velocity.y = position_current.y - position_old.y;

	if (!grounded && !cancle_gravity)
		position_current.x += float(velocity.x / substeps);
	else {
		velocity.x = position_current.x - position_old.x;

	}
	position_old = position_current;
	position_current.y = position_current.y + velocity.y + acceleration.y * dt * dt;
	acceleration = {};



}

void Fighter::accelerate(sf::Vector2f acc)
{
	acceleration += acc;
}

Vector2f Fighter::getHitBox()
{
	return hitbox.getSize();
}

bool Fighter::isMain() {
	return main;
}

void Fighter::setMain() {
	main = true;
}