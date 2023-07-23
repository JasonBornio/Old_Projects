#pragma once
#include <iostream>
#include <cmath>
#include <cstdlib>
using namespace std;

class Overload
{
public:
	Overload();
	int Value() const;
	void setValue(int newValue);
private:
	int classValue;
};

Overload::Overload() {
	classValue = 0;
}

int Overload::Value() const{
	return classValue;
}

void Overload::setValue(int newValue) {
	classValue = newValue;
}

const int operator *(const Overload& Value1, const Overload& Value2) {
	int result;
	Overload Value3;
	Value3.setValue(Value1.Value() * Value2.Value());
	result = Value3.Value();
	return result;
}
  