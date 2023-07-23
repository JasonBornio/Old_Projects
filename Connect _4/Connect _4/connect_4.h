#pragma once
#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;

void drawGrid(char grid[8][8]);
char * place(int m, int n, char grid[8][8]);
int getInput();
int opponent();
void endCondition(int m, char n, char grid[8][8]);


void drawGrid(char grid[8][8]) {
	cout << " \n   1   2   3   4   5   6   7   8\n";
	for (int j = 0; j < 8; j++) {
		cout << " ---------------------------------\n";
		for (int i = 0; i < 8; i++) {
			cout << " | " << grid[i][j];
		}
		cout << " |\n";
	}
	cout << " ---------------------------------\n";
}


char * place(int m, int n, char grid[8][8]) {
	int a, d = 0;
	char r;
	a = n - 1;

	if (m) {
		r = 'O';
	}
	else {
		r = 'X';
	}

	while (!grid[a][d]) {

		if (!grid[a][7]) {
			grid[a][7] = r;
			break;
		}
		else {
			if ((grid[a][d + 1])) {
				grid[a][d] = r;
				break;
			}
			else {
				d++;
			}
		}
	}
	return *grid;
}


int getInput() {
	int n, a, d = 0;
	cout << "please pick a number from 1 to 8:\n\n";

	while (1) {
		cin >> n;
		if (n < 9 && n > 0) {
			break;
		}
		else {
			cout << "INVALID please pick a number FROM 1 to 8:\n\n";
		}
	}
	return n;
}


int opponent() {
	int n;
	n = (rand() % 8) + 1;
	cout << "\nNUM IS: " << n <<"\n";
	return n;
}


void endCondition(int m, char n, char grid[8][8]) {
	string r;

	if (m) {
		r = "Player ";
	}
	else {
		r = "CPU ";
	}
	for (int j = 0; j < 8; j++) {
		for (int i = 0; i < 5; i++) {
			if ((grid[i][j] == n) && (grid[i + 1][j] == n) && (grid[i + 2][j] == n) && (grid[i + 3][j] == n)) {
				cout << "\n" << r << " wins\n";
			}
		}
	}
	for (int j = 0; j < 5; j++) {
		for (int i = 0; i < 8; i++) {
			if ((grid[i][j] == n) && (grid[i][j + 1] == n) && (grid[i][j + 2] == n) && (grid[i][j + 3] == n)) {
				cout << "\n" << r << " wins\n";
			}
		}
	}
}