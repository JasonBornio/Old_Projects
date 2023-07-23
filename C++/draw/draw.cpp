// draw.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "JUDrawTools.h"

class WhiteBoard : public Draw {
public:
    WhiteBoard() {

    }


public:
    bool Update(float fElapsedTime) override{
        cout << "hi";
        return true;
    }
private:


};

int main()
{
    WhiteBoard draw;
    draw.DrawLine(draw.DPoint(1000, 1000), draw.DPoint(100, 100));
    draw.DrawLine(draw.DPoint(500, 200), draw.DPoint(500, 1000));
    draw.ConstructConsole(draw);
    draw.clock();
}