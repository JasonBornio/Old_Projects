#include <iostream>
#include <cstdlib>
#include <string>
#include "connect_4.h"
using namespace std;

int main(){

	char grid[8][8];
	int n;

	for (int j = 0; j < 8; j++) {
		for (int i = 0; i < 8; i++) {
			grid[i][j] = 0;
		}
	}

	while (1) {
		drawGrid(grid);
		place(1, getInput(), grid);
		endCondition(1, 'O', grid);
		place(0, opponent(), grid);
		endCondition(0, 'X', grid);
	}
}