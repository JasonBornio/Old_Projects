#include "Engine.h"

Engine::Engine()
{
    pWindow = new Window(y_length);
    hdc = GetDC(pWindow->m_hwnd);
    RECT rect;
    GetClientRect(pWindow->m_hwnd, &rect);
    width = rect.right - rect.left;
    height = rect.bottom - rect.top;
}

Engine::~Engine()
{
}

void Engine::preUpdate()
{
}

void Engine::postUpdate()
{
}

void Engine::Update()
{        
    if (!pWindow->ProcessMessages()) {
        std::cout << "Closing World\n";
        running = false;
    }

    Draw drawer = Draw(hdc, 0, 0, width, height, 0, 0);

}

void Engine::Start()
{
    std::cout << "Creating World!\n";

    running = true;

    MainLoop();

    delete pWindow;
}

void Engine::MainLoop()
{

    running = true;
    while (running) {

        preUpdate();
        Update();
        postUpdate();

        //Render

        time();

    }
}

void Engine::time()
{
    Sleep(10);
}
