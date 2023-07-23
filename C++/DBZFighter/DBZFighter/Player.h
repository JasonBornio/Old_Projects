#include "Utilities.h"
#include "PhysicsSolver.h"

struct Player {

	#pragma region triggers
	struct Trigger {
		bool pressed = false;
		bool held = false;
		bool released = false;
		std::string name = "";
		int timer = 0;
		bool double_tapped = false;
	};

	Trigger left;
	Trigger right;
	Trigger up;
	Trigger down;
	Trigger jump;
	#pragma endregion
	#pragma region controls
	bool is_moving_left = false;
	bool is_moving_right = false;
	#pragma endregion
	#pragma region vars
	Fighter* fighter;

	bool is_dashing = false;
	bool air_dashing = false;
	#pragma endregion

	void start() {

	}

	void setPlayer(Fighter* input) {
		fighter = input;
	}

	void preUpdate() {

	}
	void update() {
		preUpdate();
		//---------
		processTriggers();
		handleMovement();


		//---------
		postUpdate();
	}

	void postUpdate() {

	}

	void resetEffects() {
	}

	void handleMovement() {
		float move_speed = 2.5f * fighter_width / 40;
		float dash_speed = move_speed * 4.f;
		float jump_force = 1.5f * fighter_width / 40;
		int state = 0;


		if (fighter->grounded) {
			if (left.double_tapped || right.double_tapped)
				is_dashing = true;
			if (left.released && right.released)
				is_dashing = false;

			if (is_dashing) {
				if (right.held)
					fighter->position_current.x += dash_speed;
				else if (left.held)
					fighter->position_current.x -= dash_speed;

			}
			else {
				if (right.held)
					fighter->position_current.x += move_speed;
				else if (left.held)
					fighter->position_current.x -= move_speed;
			}

			if (jump.pressed) {
				fighter->velocity.y = 0;
				fighter->velocity.y -= jump_force;
				fighter->jumped = true;
			}
		}
		else {
			if (left.double_tapped && !air_dashing) {
				fighter->cancle_gravity = true;
				fighter->position_current.x -= dash_speed;
			}
			else if (air_dashing && fighter->grounded) {
				resetGrav();
			}
			
			
		}
	
		
		/*
		switch (state) {
		case 0 :
			return;
		default:
			return;
		}*/
	}

	void resetGrav() {
		fighter->velocity.y = 0;
		fighter->cancle_gravity = false;
	}

	void processTriggers() {
		left.name = "left";
		checkTrigger(left, Keyboard::isKeyPressed(Keyboard::A));
		right.name = "right";
		checkTrigger(right, Keyboard::isKeyPressed(Keyboard::D));
		checkTrigger(up, Keyboard::isKeyPressed(Keyboard::W));
		checkTrigger(down, Keyboard::isKeyPressed(Keyboard::S));
		checkTrigger(jump, Keyboard::isKeyPressed(Keyboard::Space));
	}

	void checkTrigger(Trigger& trigger, bool input) {

		if (input && trigger.double_tapped == false && trigger.released == true && trigger.timer < 10) {
			trigger.double_tapped = true;
			trigger.released = false;
			//std::cout << "\n" << trigger.name << " DOUBLE PRESSED";
		}
		else if (input && trigger.pressed == false && trigger.held == false) {
			trigger.pressed = true;
			trigger.released = false;
			trigger.timer = 0;
			//std::cout << "\n" << trigger.name << " pressed";
		}
		else if (input) {
			trigger.double_tapped = false;
			trigger.pressed = false;
			trigger.held = true;
			//std::cout << "\n" << trigger.name << " held";
		}
		else if (!input && trigger.released == false && trigger.held || trigger.pressed) {
			trigger.double_tapped = false;
			trigger.pressed = false;
			trigger.held = false;
			trigger.released = true;
			//std::cout << "\n" << trigger.name << " released";
		}
		
		if(trigger.timer < 20){
			trigger.timer += 1;
		}
	}
};