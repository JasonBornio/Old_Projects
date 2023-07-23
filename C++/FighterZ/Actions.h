#pragma once
#include "Fighter.h"
/*
0. strength;
1. ki_strength;
2. defense;
3. ki_defense;
4. speed;
5. health;
6. ki;
7. stamina;
*/
void melee_attack(Fighter& x, Fighter& y);


void melee_attack(Fighter& x, Fighter& y) {
	int attack = (x.get_stat(0)/2 + ((rand() % 20) * x.get_stat(0))/40) - y.get_stat(2);
	if (attack <= 0) {
		attack = 1;
	}
	y.decrease_stat(5, attack);
	cout << "\n" << x.get_name() << " attacks " << y.get_name() << " for " << attack << " hit points "
		<< "\n" << y.get_name() << " is now at " << y.get_stat(5) << " HP ";
}
