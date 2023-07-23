#pragma once
#include <iostream>
#include<vector>
using namespace std;

class Circuit
{
public:
	Circuit();
	void input();
	void build();
	void add_component(string name, int value, int connection);
	int num;

private:
	vector<string>circuit;
	vector<vector<int>>components;
	void build_vertical(int component);
	void build_horizontal(int component, int spaces);
};


Circuit::Circuit() {
	num = 0;
}


void Circuit::build() {
	int horizontal1, vertical, horizontal2;
	if(num%3 == 0){
		horizontal1 = num / 3;
		vertical = num / 3;
		horizontal2 = num / 3;
	}
	else if (num % 3 == 1) {
		horizontal1 = (num - 1) / 3;
		vertical = ((num - 1) / 3) + 1;
		horizontal2 = (num - 1) / 3;
	}
	else {
		horizontal1 = ((num - 2) / 3) + 1;
		vertical = (num - 2) / 3;
		horizontal2 = ((num - 2) / 3) + 1;
	}

	for (int i = 0; i < horizontal1; i++) {
		build_vertical(components[0][i]);
	}
	for (int i = 0; i < vertical; i++) {
		build_horizontal(components[0][i], horizontal1);
	}
	cout << "\n";
	for (int i = 0; i < horizontal2; i++) {
		build_vertical(components[0][i]);
	}

}


void Circuit::build_vertical(int component) {
	switch (component) {
	case 0: 
		cout << "---------";
	case 1: 
		cout << "--! R !--";
	case 2:
		cout << "---| |---";
	}
}


void Circuit::build_horizontal(int component, int spaces) {


	switch (component) {
	case 0:
		for (int i = 0; i < 3; i++) {
			cout << "\n";
			for (int j = 0; j < spaces; j++) {
				cout << "         ";
			}
			cout << "!";
		}
	case 1:
		for (int i = 0; i < 3; i++) {
			cout << "\n";
			for (int j = 0; j < spaces; j++) {
				cout << "        ";
			}
			if (i == 1) {
				cout << "!R!";
			}
			else {
				cout << " !";
			}
		}
	case 2:
		for (int i = 0; i < 3; i++) {
			cout << "\n";
			for (int j = 0; j < spaces; j++) {
				cout << "        ";
			}
			if (i == 1 ) {
				cout << "===";
			}
			else {
				cout << " !";
			}
		}
	}
}


void Circuit::add_component(string name, int value, int connection) {
	vector<int>x;
	int nam;

	if (name == "r" || name == "R") {
		nam = 1;
	}
	else if(name == "c" || name == "C") {
		nam = 2;
	}
	else {
		nam = 0;
	}

	x.push_back(nam);
	x.push_back(value);
	x.push_back(connection);
	components.push_back(x);
}


void Circuit::input() {

	//string input;
	//int input1;
	//string name;
	//int value, connection;

	/*while (input != "done" || input1 != 0) {

		cout << "input component name";
		cin >> input;
		if (input == "done") {
			break;
		}
		name = input;

		cout << "input component value";
		cin >> input1;
		if (input1 == 0) {
			break;
		}
		value = input1;

		cout << "input component connection type";
		cin >> input1;
		if (input1 == 0) {
			break;
		}
		connection = input1;

		add_component(r, 100, 1);

		num++;
	}*/
}