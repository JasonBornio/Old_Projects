#pragma once
#include <iostream>
#include <math.h>

using namespace std;

class Transmitter
{
public:
	Transmitter();
	void set_value();
	int get_value() const;
	int Byte[8];

private:
	int value;

};

Transmitter::Transmitter() {
	Byte[8] = { 0 };
	value = 0;
}

void Transmitter::set_value() {
	cout << "\nEnter a value:\n";
	cin >> value;
	cout << "\nvalue = " << value<<"\n";

	//start bit
	Byte[0] = 1;

	int a = value;
	int r;

	for (int i = 1; i < 6; i++) {

		r = a % 2;
		a = a / 2 - r / 2;

		if (r) {
			Byte[i] = 1;
		}
		else {
			Byte[i] = 0;
		}
	}

	Byte[7] = 1;
}

int Transmitter::get_value() const {
	return value;
}

