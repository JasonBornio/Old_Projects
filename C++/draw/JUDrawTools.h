#pragma once
#include <iostream>
#include <Windows.h>
#include <cmath>
#include <thread>
#include<vector>
using namespace std;


class Draw {

public:
	Draw() {

	}



public:
	HWND myconsole;
	struct Point {
		int x, y;
	};

	Point DPoint(int x, int y) {
		Point point;
		point.x = x;
		point.y = y;
		return point;
	}
	void ConstructConsole(Draw& x);
	void DrawLine(Point p1, Point p2);
	void clock();
	virtual bool Update(float FElaspedTime) = 0;
	bool active = true;

private:


};


void Draw::clock() {
	while (active) {
		Update(0);
	}
}

void Draw::ConstructConsole(Draw& x){

}

void Draw::DrawLine(Point p1, Point p2) {
	myconsole = GetConsoleWindow();
	HDC mydc = GetDC(myconsole);
	COLORREF COLOR = RGB(0, 255, 0);
	int xlength, ylength, ratio, xstart, ystart;

	if (p2.x > p1.x) {
		xlength = p2.x - p1.x;
	}
	else {
		xlength = p1.x - p2.x;
	}

	if (p2.y > p1.y) {
		ylength = p2.y - p1.y;
	}
	else {
		ylength = p1.y - p2.y;
	}

	xlength += 1;
	ylength += 1;

	if (xlength == 1) {
		ratio = 0;
	}
	else if (ylength == 1) {
		ratio = xlength;
	}
	else {
		ratio = xlength / ylength;
	}

	if (p2.x > p1.x) {
		xstart = p1.x;
	}
	else {
		xstart = p2.x;
	}
	if (p2.y > p1.y) {
		ystart = p1.y;
	}
	else {
		ystart = p2.y;
	}

	for (int i = ystart; i < ystart + ylength; i += 1) {
		for (int j = xstart; j <= xstart + ratio; j += 1) {
			SetPixel(mydc, j, i, COLOR);
		}
		xstart += ratio;
	}

	ReleaseDC(myconsole, mydc);
	cin.ignore();
}