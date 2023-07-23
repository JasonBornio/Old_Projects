#pragma once
#include <iostream>

using namespace std;

class bitStream
{
public:
	bitStream();
	int Byte[8];
	void addByte();
	void shift();

private:
	int BitStream[8];

};

bitStream::bitStream() {
	Byte[8] = { 0 };
	BitStream[8] = { 0 };
}

void bitStream::addByte() {
	for (int i = 0; i <= 7; i++) {
		BitStream[i] = Byte[i];
	}
}

void bitStream::shift() {
	for (int i = 0; i <= 7; i++) {
		if (i == 7) {
			BitStream[i] = 0;
		}
		else {
			BitStream[i] = BitStream[i + 1];
		}
	}
	for (int i = 0; i < 8; i++) {
		cout << BitStream[i];
	}
	cout << "\n";
}