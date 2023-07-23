#pragma once
#include <Windows.h>
#include <vector>

class Draw
{
public:
	Draw(HDC hdc, int xDest, int yDest, int DestWidth, int DestHeight, int xSrc, int ySrc);

	void DrawImage(std::vector<std::vector<int>> image);

private:

};

