#pragma once
#include <SFML/Graphics.hpp>
#include <vector>
#include "Entity.h"
#include "Cell.h"
#include<iostream>
#include "globalItems.h"

struct solver {

	sf::Vector2f gravity = { 0.f, 1000.f };
	std::vector<Cell*> entity_list;

	void update(float dt) {
		int substeps = 8;
		for (int i = 0; i < substeps; i++) {
			//applyGravity();
			//solveAttractionForces(global_prey);
			applyDrag();
			applyConstraint();
			//solveCollisions();
			updatePositions(dt/substeps);
		}
	}

	void updatePositions(float dt) {
		for (int i = 0; i < entity_list.size(); i++) {
			entity_list[i]->updatePosition(dt);
		}
	}

	void applyGravity() {
		for (int i = 0; i < entity_list.size(); i++) {
			entity_list[i]->accelerate(gravity);
		}
	}

	void applyDrag() {
		for (int i = 0; i < entity_list.size(); i++) {
			Cell* obj = entity_list[i];
			const float dist = length(obj->velocity);
			const sf::Vector2f n = obj->velocity;
			const sf::Vector2f drag = square(n)* drag_coefficient * obj->getArea();
			obj->accelerate(-drag);
		}
	}

	void solveAttractionForces(std::vector<Cell*>& global_prey) {
		const int object_count = global_prey.size();

		for (int i = 0; i < object_count; i++) {
			Cell* object = global_prey[i];
			for (int j = 0; j < object_count; j++) {
				if (j != i) {
					Cell* object2 = entity_list[j];
					const sf::Vector2f collision_axis = object2->position_current - object->position_current;
					const float dist2 = length(collision_axis);
					const float min_dist = object->getRadius() + object2->getRadius();
					if (dist2 > min_dist) {

						const float dist = dist2;// cc

						const sf::Vector2f n = collision_axis / dist;
						const sf::Vector2f attraction = n * object->getForce() * (-1.0f/(dist * dist)) * object->getArea();

						object2->accelerate(-attraction);
					}
				}
			}
		}
	}

	void solveCollisions() {
		const int object_count = entity_list.size();
		const float coeff = 0.1f;
		for (int i = 0; i < object_count; i++) {
			Cell* object = entity_list[i];
			for (int j = 0; j < object_count; j++) {
				if (j != i) {
					Cell* object2 = entity_list[j];
					const sf::Vector2f collision_axis = object->position_current - object2->position_current;
					const float dist2 = length(collision_axis);
					const float min_dist = object->getRadius() + object2->getRadius();
					if (dist2 < min_dist) {

						const float dist = dist2;// cc

						const sf::Vector2f n = collision_axis / dist;
						const float mass_ratio_1 = object->getRadius() / (object->getRadius() + object2->getRadius());
						const float mass_ratio_2 = object2->getRadius() / (object->getRadius() + object2->getRadius());
						const float delta = 0.5f * coeff * (dist - min_dist);

						object->position_current -= n * (mass_ratio_2 * delta);
						object2->position_current += n * (mass_ratio_1 * delta);

					}
				}
			}
		}
	}

	void applyConstraint() {
		const sf::Vector2f position(CENTER);
		const float radius = RADIUS;
		for (int i = 0; i < entity_list.size(); i++) {
			const sf::Vector2f to_obj = entity_list[i]->position_current - position;
			const float dist = length(to_obj);

			if (dist > radius - entity_list[i]->getRadius()) {
				entity_list[i]->fitness -= 10.f;
				const sf::Vector2f n = to_obj / dist;
				entity_list[i]->position_current = position + n * (radius - entity_list[i]->getRadius());
			}
		}
	}


	inline sf::Vector2f square(const sf::Vector2f& lv)
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

	inline float dot(const sf::Vector2f& lv, const sf::Vector2f& rv)
	{
		return lv.x * rv.x + lv.y * rv.y;
	}

	inline float length(const sf::Vector2f& source)
	{
		return std::sqrt(source.x *source.x + source.y * source.y);
	}

};