#include "Entity.h"
class PlantCell : public Entity
{
public:
	using Entity::Entity;
	bool checkSplit();
	void split();
	void update();
	float getInitialRadius();
private:
	float growth_rate = 0.001f;
	float split_chance = 0.15f;
	float initial_radius = radius;
};
