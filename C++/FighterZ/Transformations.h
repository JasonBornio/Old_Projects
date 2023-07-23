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
void glow(Fighter& x);
void dark(Fighter& x);
void silver(Fighter& x);

void glow(Fighter& x) {
	x.multipliers(1, 1.1, 1, 1, 1, 1, 1, 1);
	x.calculate_power_level();
	cout << "\n" << x.get_name() << " uses Glow"
		<< "\ntheir power level is: " << x.get_power_level();
}

void dark(Fighter& x) {
	x.multipliers(1.5, 1, 1, 1, 1, 0.8, 1, 1);
	x.calculate_power_level();
	cout << "\n" << x.get_name() << " turns Dark"
		<< "\ntheir power level is: " << x.get_power_level();
}

void silver(Fighter& x) {
	x.multipliers(1.1, 1.1, 1, 1, 1, 1, 1, 1);
	x.calculate_power_level();
	cout << "\n" << x.get_name() << " turns Silver"
		<< "\ntheir power level is: " << x.get_power_level();
}