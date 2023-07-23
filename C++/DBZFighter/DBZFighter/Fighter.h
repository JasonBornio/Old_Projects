#include "Utilities.h"

class Fighter
{
public:
	Fighter(std::vector<RectangleShape>& shapes,  Vector2f position);
	~Fighter();
	Vector2f position_current;
	Vector2f position_old;
	Vector2f velocity;
	Vector2f acceleration;
	RectangleShape hitbox;
	int index = 0;

	void updatePosition(float dt, int subteps);
	void accelerate(Vector2f acc);
	Vector2f getHitBox();
	bool isMain();
	void setMain();
	bool grounded = false;
	bool jumped;
	bool cancle_gravity = false;

private:
	bool main = false;
};

