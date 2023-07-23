#pragma once
#include <iostream>

using namespace std;

class Fighter
{
public:
	Fighter();
	void stats(double a, double b, double c, double d, double e, int f, int g, int h, string n);
	void multipliers(double aa, double bb, double cc, double dd, double ee, double ff, double gg, double hh);
	double get_melee_damage() const;
	double get_ki_damage() const;
	double get_melee_defense() const;
	double get_ki_defense() const;
	double get_health() const;
	int get_ki() const;
	int get_stamina() const;
	int get_speed() const;
	string get_name() const;
	void alter_stats(double a, double b, double c, double d, double e, int f, int g, int h, bool x);
	int power_level;
	int get_power_level();

private:
	string name;
	double melee_damage, ki_damage;
	double melee_defense, ki_defense;
	double health;
	int ki, stamina, speed;
	double a, b, c, d, e, f, g, h;

};

Fighter::Fighter() {
	melee_damage = 0;
	ki_damage = 0;
	melee_defense = 0;
	ki_defense = 0;
	health = 0;
	ki = 0;
	stamina = 0;
	speed = 0;
	power_level = 0;
	name = "//";
	a = 1; b = 1; c = 1; d = 1; e = 1; f = 1; g = 1; h = 1;
}

void Fighter::stats(double a, double b, double c, double d, double e, int f, int g, int h, string n) {
	melee_damage = a;
	ki_damage = b;
	melee_defense = c;
	ki_defense = d;
	health = e;
	ki = f;
	stamina = g;
	speed = h;
	name = n;
}

void Fighter::multipliers(double aa, double bb, double cc, double dd, double ee, double ff, double gg, double hh) {
	a = aa;
	b = bb;
	c = cc;
	d = dd;
	e = ee;
	f = ff;
	g = gg;
	h = hh;
}

double Fighter::get_melee_damage() const {
	return melee_damage * a;
}

double Fighter::get_ki_damage() const {
	return ki_damage * b;
}

double Fighter::get_melee_defense() const {
	return melee_defense * c;
}

double Fighter::get_ki_defense() const {
	return ki_defense * d;
}

double Fighter::get_health() const {
	return health * e;
}

int Fighter::get_ki() const {
	return ki * f;
}

int Fighter::get_stamina() const {
	return stamina * g;
}

int Fighter::get_speed() const {
	return speed * h;
}

string Fighter::get_name() const {
	return name;
}

int Fighter::get_power_level() {
	int p = (((melee_damage * a) + (ki_damage * b))*10 + ((health * e) + (speed * h)) + ((melee_defense * c) + (ki_defense * d)) / 2 + ((ki * f) + (stamina * g)) / 3);
	power_level = p;
	cout << "\n" << name << "'s Power Level is: " << power_level;
	return power_level;
}

void Fighter::alter_stats(double a, double b, double c, double d, double e, int f, int g, int h, bool x) {
	if (x) {
		melee_damage -= a;
		ki_damage -= b;
		melee_defense -= c;
		ki_defense -= d;
		health -= e;
		ki -= f;
		stamina -= g;
		speed -= h;
	}
	else {
		melee_damage += a;
		ki_damage += b;
		melee_defense += c;
		ki_defense += d;
		health += e;
		ki += f;
		stamina += g;
		speed += h;
	}
}
