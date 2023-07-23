#pragma once
#include <SFML/Graphics.hpp>
#include <vector>
#include <iostream>
using namespace sf;

#define M_PI 3.14159265358979323846
#define ARENA_RATIO Vector2f(1200, 700)
#define fighter_width 40
#define HITBOX  Vector2f(fighter_width, fighter_width * 1.5f)
#define CENTER Vector2f(610.f,500.f)
#define drag_coefficient 0.7f;