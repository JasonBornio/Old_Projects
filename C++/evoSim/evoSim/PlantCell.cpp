#include "PlantCell.h"
bool PlantCell::checkSplit()
{
	if (radius > (initial_radius * 3.1f)) {
		float random = 0.f;
		random = ((rand() % 100) / 100);
		if (random < split_chance)
			return true;
	}
	return false;
}

void PlantCell::split()
{
	int divisions = int(getArea() / M_PI * (initial_radius * initial_radius));
	if (divisions < 2)
		divisions = 2;

	for (int i = 0; i < divisions; i++){

	}
}

void PlantCell::update()
{
	radius += radius * growth_rate;
	shape.setRadius(radius);
}

float PlantCell::getInitialRadius() {
	return initial_radius;
}