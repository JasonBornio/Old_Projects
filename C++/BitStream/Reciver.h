#pragma once
#include <iostream>

using namespace std;

class Reciever
{
public:
	Reciever();
	void set_value();
	int get_value() const;
	int readValue;

private:
	int value;

};

Reciever::Reciever() {
	value = 0;
}

void Reciever::set_value() {
	value = readValue;
}

int Reciever::get_value() const {
	return value;
}

