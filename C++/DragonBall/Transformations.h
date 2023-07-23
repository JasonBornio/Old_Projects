#pragma once
#include <iostream>
#include "Fighter.h"

using namespace std;


void kaioken(Fighter& x);
void kaiokenX3(Fighter& x);
void kaiokenX10(Fighter& x);
void kaiokenX20(Fighter& x);
void superSaiyan(Fighter& x);
void ascendedSaiyan(Fighter& x);
void ultraSuperSaiyan(Fighter& x);
void masteredsuperSaiyanGod(Fighter& x);
void superSaiyan2(Fighter& x);
void majin(Fighter& x);
void superSaiyan3(Fighter& x);
void superSaiyanGod(Fighter& x);
void superSaiyanGodSuperSaiyan(Fighter& x);
void masteredSuperSaiyanGodSuperSaiyan(Fighter& x);
void SSBSSKKX10(Fighter& x);
void SSBSSKKX20(Fighter& x);
void royalBlue(Fighter& x);
void ultraInstinct(Fighter& x);
void masteredUltraInstinct(Fighter& x);


void kaioken(Fighter& x) {
	x.multipliers(2.5, 2.75, 3.0, 1.75, 3.0, 1.5, 2.0, 2.5);
	cout << "\n" << x.get_name() << " used Kaioken";
	x.get_power_level();
}

void kaiokenX3(Fighter& x) {
	x.multipliers(2.5, 2.75, 3.0, 1.75, 3.0, 1.5, 2.0, 2.5);
	cout << "\n" << x.get_name() << " used Kaioken level 3";
	x.get_power_level();
}

void kaiokenX10(Fighter& x) {
	x.multipliers(2.5, 2.75, 3.0, 1.75, 3.0, 1.5, 2.0, 2.5);
	cout << "\n" << x.get_name() << " used Kaioken level 10";
	x.get_power_level();
}

void kaiokenX20(Fighter& x) {
	x.multipliers(2.5, 2.75, 3.0, 1.75, 3.0, 1.5, 2.0, 2.5);
	cout << "\n" << x.get_name() << " used Kaioken level 20";
	x.get_power_level();
}

void superSaiyan(Fighter& x) {
	x.multipliers(2.5, 2.75, 3.0, 1.75, 3.0, 1.5, 2.0, 2.5);
	cout << "\n" << x.get_name() << " has transformed into a Super Saiyajin";
	x.get_power_level();
}

void ascendedSaiyan(Fighter& x) {
	x.multipliers(2.5, 2.75, 3.0, 1.75, 3.0, 1.5, 2.0, 2.5);
	cout << "\n" << x.get_name() << " has ascended the Super Saiyajin legend";
	x.get_power_level();
}

void ultraSuperSaiyan(Fighter& x) {
	x.multipliers(2.5, 2.75, 3.0, 1.75, 3.0, 1.5, 2.0, 2.5);
	cout << "\n" << x.get_name() << " has pushed past Super Saiyajin limit";
	x.get_power_level();
}

void masteredsuperSaiyanGod(Fighter& x) {
	x.multipliers(2.5, 2.75, 3.0, 1.75, 3.0, 1.5, 2.0, 2.5);
	cout << "\n" << x.get_name() << " has transformed into a Super Saiyajin";
	x.get_power_level();
}

void superSaiyan2(Fighter& x) {
	x.multipliers(2.5, 2.75, 3.0, 1.75, 3.0, 1.5, 2.0, 2.5);
	cout << "\n" << x.get_name() << " has transformed into a Super Saiyajin 2";
	x.get_power_level();
}

void majin(Fighter& x) {
	x.multipliers(2.5, 2.75, 3.0, 1.75, 3.0, 1.5, 2.0, 2.5);
	cout << "\n" << x.get_name() << " has given into to their evil";
	x.get_power_level();
}

void superSaiyan3(Fighter& x) {
	x.multipliers(2.5, 2.75, 3.0, 1.75, 3.0, 1.5, 2.0, 2.5);
	cout << "\n" << x.get_name() << " has transformed into a Super Saiyajin 3";
	x.get_power_level();
}

void superSaiyanGod(Fighter& x) {
	x.multipliers(2.5, 2.75, 3.0, 1.75, 3.0, 1.5, 2.0, 2.5);
	cout << "\n" << x.get_name() << " has transformed into ";
	x.get_power_level();
}

void superSaiyanGodSuperSaiyan(Fighter& x) {
	x.multipliers(2.5, 2.75, 3.0, 1.75, 3.0, 1.5, 2.0, 2.5);
	cout << "\n" << x.get_name() << " has transformed into a Super Saiyajin";
	x.get_power_level();
}

void masteredSuperSaiyanGodSuperSaiyan(Fighter& x) {
	x.multipliers(2.5, 2.75, 3.0, 1.75, 3.0, 1.5, 2.0, 2.5);
	cout << "\n" << x.get_name() << " has transformed into a Super Saiyajin";
	x.get_power_level();
}

void SSBSSKKX10(Fighter& x) {
	x.multipliers(2.5, 2.75, 3.0, 1.75, 3.0, 1.5, 2.0, 2.5);
	cout << "\n" << x.get_name() << " has transformed into a Super Saiyajin";
	x.get_power_level();
}

void SSBSSKKX20(Fighter& x) {
	x.multipliers(2.5, 2.75, 3.0, 1.75, 3.0, 1.5, 2.0, 2.5);
	cout << "\n" << x.get_name() << " has transformed into a Super Saiyajin";
	x.get_power_level();
}

void royalBlue(Fighter& x) {
	x.multipliers(2.5, 2.75, 3.0, 1.75, 3.0, 1.5, 2.0, 2.5);
	cout << "\n" << x.get_name() << " has transformed into a Super Saiyajin";
	x.get_power_level();
}

void ultraInstinct(Fighter& x) {
	x.multipliers(2.5, 2.75, 3.0, 1.75, 3.0, 1.5, 2.0, 2.5);
	cout << "\n" << x.get_name() << " has transformed into a Super Saiyajin";
	x.get_power_level();
}

void masteredUltraInstinct(Fighter& x) {
	x.multipliers(2.5, 2.75, 3.0, 1.75, 3.0, 1.5, 2.0, 2.5);
	cout << "\n" << x.get_name() << " has transformed into a Super Saiyajin";
	x.get_power_level();
}