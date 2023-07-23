#pragma once

#include <iostream>
#include "Window.h"
#include "Draw.h"

class Engine
{
public:
	Engine();
	~Engine();	
	void Start();
	virtual void preUpdate();
	virtual void postUpdate();
private:
	int height = 0;
	int width = 0;
	int y_length = 250;
	int x_length = x_length * 2;
	HDC hdc = {};
	Window* pWindow = {};
	bool running;
	void Update();
	void MainLoop();
	void time();
};

