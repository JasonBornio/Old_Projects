#pragma once
#include <iostream>
using namespace std;

struct stats {
	double strength;
	double ki_strength;
	double defense;
	double ki_defense;
	double speed;
	double health;
	double ki;
	double stamina;
	int potential;
};


class Fighter
{
public:
	void set_stats();
	double get_stat(int a);
	int get_power_level();
	void increase_stat(int a, double b);
	void decrease_stat(int a, double b);
	string get_name();
	void multipliers(double a, double b, double c, double d, double e, double f, double g, double h);
	void calculate_power_level();
private:
	string name;
	stats f_stats;
	int power_level;
};


void Fighter::set_stats() {
	cout << "\ninput name:\n";
	cin >> name;
	cout << "input strength:\n";
	cin >> f_stats.strength;
	cout << "input ki_strength:\n";
	cin >> f_stats.ki_strength;
	cout << "input defense:\n";
	cin >> f_stats.defense;
	cout << "input ki_defense:\n";
	cin >> f_stats.ki_defense;
	cout << "input speed:\n";
	cin >> f_stats.speed;
	cout << "input health:\n";
	cin >> f_stats.health;
	cout << "input ki:\n";
	cin >> f_stats.ki;
	cout << "input stamina:\n";
	cin >> f_stats.stamina;
	cout << "input potential:\n";
	cin >> f_stats.potential;
	calculate_power_level();
}

double Fighter::get_stat(int a) {
	switch (a) {
	case 0:
		return f_stats.strength;
	case 1:
		return f_stats.ki_strength;
	case 2:
		return f_stats.defense;
	case 3:
		return f_stats.ki_defense;
	case 4:
		return f_stats.speed;
	case 5:
		return f_stats.health;
	case 6:
		return f_stats.ki;
	case 7:
		return f_stats.stamina;
	}
}

int Fighter::get_power_level() {
	return power_level;
}

void Fighter::increase_stat(int a, double b) {
	switch (a) {
	case 0:
		f_stats.strength += b;
	case 1:
		f_stats.ki_strength += b;
	case 2:
		f_stats.defense += b;
	case 3:
		f_stats.ki_defense += b;
	case 4:
		f_stats.speed += b;
	case 5:
		f_stats.health += b;
	case 6:
		f_stats.ki += b;
	case 7:
	    f_stats.stamina += b;
	}
}

void Fighter::decrease_stat(int a, double b) {
	switch (a) {
	case 0:
		f_stats.strength -= b;
	case 1:
		f_stats.ki_strength -= b;
	case 2:
		f_stats.defense -= b;
	case 3:
		f_stats.ki_defense -= b;
	case 4:
		f_stats.speed -= b;
	case 5:
		f_stats.health -= b;
	case 6:
		f_stats.ki -= b;
	case 7:
		f_stats.stamina -= b;
	}
}

string Fighter::get_name() {
	return name;
}

void Fighter::multipliers(double a, double b, double c, double d, double e, double f, double g, double h) {
	f_stats.strength *= a;
	f_stats.ki_strength *= b;
	f_stats.defense *= c;
	f_stats.ki_defense *= d;
	f_stats.speed *= e;
	f_stats.health *= f;
	f_stats.ki *= g;
	f_stats.stamina *= h;
}

void Fighter::calculate_power_level() {
	power_level = f_stats.strength + f_stats.ki_strength + f_stats.health + (f_stats.defense +
		f_stats.ki_defense + f_stats.speed + f_stats.ki +
		f_stats.stamina) / 4;
	cout << "\n" << name << "'s power level is " << power_level;
}