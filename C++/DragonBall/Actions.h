#pragma once
#include <iostream>
#include "Fighter.h"

using namespace std;

void attack(Fighter& x, Fighter& y, bool a);
int check(Fighter& x, int a);

void attack(Fighter& x, Fighter& y, bool a) {
	int b = ((x.get_melee_damage() / 2) + (((rand() % 100) * x.get_melee_damage()) / 100));
	int c = ((x.get_ki_damage() / 2) + (((rand() % 100) * x.get_ki_damage()) / 100));
	int damage = (b - y.get_melee_defense());
	int ki_damage = (c - y.get_ki_defense());
	if (a) {
		if (damage <= 0) {
			damage = 1;
		}
		y.alter_stats(0, 0, 0, 0, damage, 0, 0, 0, 1);
		cout << "\n\n" << x.get_name() << " attacks " << y.get_name() << " for " << b << " hitpoints";
	}
	else {
		if (ki_damage <= 0) {
			ki_damage = 1;
		}
		y.alter_stats(0, 0, 0, 0, ki_damage, 0, 0, 0, 1);
		cout << "\n\n" << x.get_name() << " attacks " << y.get_name() << " for " << b << " hitpoints";
	}
	cout << "\n" << y.get_name() << " is now at " << y.get_health() << " HP\n";
	x.get_power_level();
	y.get_power_level();
}

int check(Fighter& x, int a) {
	int i;
	if (x.get_health() < 0) {
		x.multipliers(1, 1, 1, 1, 0, 1, 1, 1);
		i = 0;
		cout << "\n" << x.get_name() << " has been beaten ";
	}
	else if(a != 0){
		i = 1;
	}
	return i;
}


