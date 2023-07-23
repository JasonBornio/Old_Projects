#pragma once

#include <Windows.h>

LRESULT CALLBACK WindowProc(HWND hWnd, UINT uMsg, WPARAM wParam, LPARAM lParam);

class Window
{
public:
	Window(int height);
	Window(const Window&) = delete;
	Window& operator =(const Window&) = delete;
	~Window();
	HWND m_hwnd = {};
	bool ProcessMessages();
private:
	HINSTANCE m_hInstance;
	HWND m_hwnd;
};

