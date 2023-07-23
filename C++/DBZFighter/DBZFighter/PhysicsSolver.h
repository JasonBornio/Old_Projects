#include "Utilities.h"
#include "Fighter.h"

struct solver {

	Vector2f gravity = { 0.f, 2000.f };
	std::vector<Fighter*> fighter_list;

	const float ground = CENTER.y + ARENA_RATIO.y / 2;
	const float left_wall = CENTER.x - ARENA_RATIO.x / 2;
	const float right_wall = CENTER.x + ARENA_RATIO.x / 2;
	const float ceiling = CENTER.y - ARENA_RATIO.y / 2;

	void update(float dt) {
		int substeps = 8;
		for (int i = 0; i < substeps; i++) {
			checkGrounded();
			applyGravity();
			updatePositions(dt/substeps, substeps);
			applyConstraints();
		}
	}

	void updatePositions(float dt, int substeps) {
		for (int i = 0; i < fighter_list.size(); i++) {
			fighter_list[i]->updatePosition(dt, substeps);
		}
	}

	void checkGrounded() {
		for (int i = 0; i < fighter_list.size(); i++) {
			if (fighter_list[i]->position_current.y + fighter_list[i]->getHitBox().y / 2 + 1.f > CENTER.y + ARENA_RATIO.y / 2) {
				fighter_list[i]->grounded = true;
				//std::cout << "\ngrounded";
			}
			else {
				fighter_list[i]->grounded = false;
				//std::cout << "\nNOTgrounded";
			}
		}
	}

	void applyGravity() {
		for (int i = 0; i < fighter_list.size(); i++) {
			if(fighter_list[i]->grounded == false && fighter_list[i]->cancle_gravity == false)
				fighter_list[i]->accelerate(gravity);
		}
	}

/*
	void applyDrag() {
		for (int i = 0; i < fighter_list.size(); i++) {
			Fighter* obj = fighter_list[i];
			const float dist = length(obj->velocity);
			const Vector2f n = obj->velocity;
			const Vector2f drag = square(n) * drag_coefficient * obj->getArea();
			obj->accelerate(-drag);
		}
	}
	*/
	/*void solveCollisions() {
		const int object_count = fighter_list.size();
		const float coeff = 0.1f;
		for (int i = 0; i < object_count; i++) {
			Fighter* object = fighter_list[i];
			for (int j = 0; j < object_count; j++) {
				if (j != i) {
					Fighter* object2 = fighter_list[j];
					const Vector2f collision_axis = object->position_current - object2->position_current;
					const float dist2 = length(collision_axis);
					const float min_dist = object->getRadius() + object2->getRadius();
					if (dist2 < min_dist) {

						const float dist = dist2;// cc

						const Vector2f n = collision_axis / dist;
						const float mass_ratio_1 = object->getRadius() / (object->getRadius() + object2->getRadius());
						const float mass_ratio_2 = object2->getRadius() / (object->getRadius() + object2->getRadius());
						const float delta = 0.5f * coeff * (dist - min_dist);

						object->position_current -= n * (mass_ratio_2 * delta);
						object2->position_current += n * (mass_ratio_1 * delta);

					}
				}
			}
		}
	}*/

	void applyConstraints() {

		for (int i = 0; i < fighter_list.size(); i++) {
			const float object = fighter_list[i]->position_current.y + fighter_list[i]->getHitBox().y/2;

			if (object > ground) {
				fighter_list[i]->position_current = Vector2f(fighter_list[i]->position_current.x, ground - fighter_list[i]->getHitBox().y/2);
			}
		}
		for (int i = 0; i < fighter_list.size(); i++) {
			const float object = fighter_list[i]->position_current.y - fighter_list[i]->getHitBox().y / 2;

			if (object < ceiling) {
				fighter_list[i]->position_current = Vector2f(fighter_list[i]->position_current.x, ceiling + fighter_list[i]->getHitBox().y / 2);
			}
		}
		for (int i = 0; i < fighter_list.size(); i++) {
			const float object = fighter_list[i]->position_current.x - fighter_list[i]->getHitBox().x / 2;

			if (object < left_wall) {
				fighter_list[i]->position_current = Vector2f(left_wall + fighter_list[i]->getHitBox().x / 2, fighter_list[i]->position_current.y);
			}
		}
		for (int i = 0; i < fighter_list.size(); i++) {
			const float object = fighter_list[i]->position_current.x + fighter_list[i]->getHitBox().x / 2;

			if (object > right_wall) {
				fighter_list[i]->position_current = Vector2f(right_wall - fighter_list[i]->getHitBox().x / 2, fighter_list[i]->position_current.y);
			}
		}

	}

	inline Vector2f square(const Vector2f& lv)
	{
		if (lv.y < 0 && lv.x < 0) {
			return { -(lv.x * lv.x), -(lv.y * lv.y) };
		}
		else if (lv.x < 0) {
			return { -(lv.x * lv.x), (lv.y * lv.y) };
		}
		else if (lv.y < 0) {
			return { (lv.x * lv.x), -(lv.y * lv.y) };
		}
		else {
			return { (lv.x * lv.x), (lv.y * lv.y) }; 
		}
	}

	inline float dot(const Vector2f& lv, const Vector2f& rv)
	{
		return lv.x * rv.x + lv.y * rv.y;
	}

	inline float length(const Vector2f& source)
	{
		return std::sqrt(source.x *source.x + source.y * source.y);
	}

};