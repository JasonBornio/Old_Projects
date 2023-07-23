#pragma once
#include <iostream>
#include "Fighter.h"

using namespace std;

void potaraFusion(Fighter& fuse, Fighter& x, Fighter& y);
void FusionDance(Fighter& fuse, Fighter& x, Fighter& y);

void potaraFusion(Fighter& fuse, Fighter& x, Fighter& y) {
	double melee_damage, ki_damage, melee_defense, ki_defense, health, ki, stamina, speed;
	melee_damage = (x.get_melee_damage() + y.get_melee_damage()) * 50;
	ki_damage = (x.get_ki_damage() + y.get_ki_damage()) * 50;
	melee_defense = (x.get_melee_defense() + y.get_melee_defense()) * 50;
	ki_defense = (x.get_ki_defense() + y.get_ki_defense()) * 50;
	health = (x.get_health() + y.get_health()) * 50;
	ki = (x.get_ki() + y.get_ki()) * 50;
	stamina = (x.get_stamina() + y.get_stamina()) * 50;
	speed = (x.get_speed() + y.get_speed()) * 50;
	fuse.stats(melee_damage, ki_damage, melee_defense, ki_defense, health, ki, stamina, speed, "Vegito");
	cout << "\n" << x.get_name() << " and " << y.get_name() << " have fused to become " << fuse.get_name();
}

void FusionDance(Fighter& fuse, Fighter& x, Fighter& y) {
	double melee_damage, ki_damage, melee_defense, ki_defense, health, ki, stamina, speed;
	melee_damage = (x.get_melee_damage() + y.get_melee_damage()) * 5;
	ki_damage = (x.get_ki_damage() + y.get_ki_damage()) * 5;
	melee_defense = (x.get_melee_defense() + y.get_melee_defense()) * 5;
	ki_defense = (x.get_ki_defense() + y.get_ki_defense()) * 5;
	health = (x.get_health() + y.get_health()) * 5;
	ki = (x.get_ki() + y.get_ki()) * 5;
	stamina = (x.get_stamina() + y.get_stamina()) * 5;
	speed = (x.get_speed() + y.get_speed()) * 5;
	fuse.stats(melee_damage, ki_damage, melee_defense, ki_defense, health, ki, stamina, speed, "Gogeta");
	cout << "\n" << x.get_name() << " and " << y.get_name() << " have fused to become " << fuse.get_name();
}