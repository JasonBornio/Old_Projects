#include "Draw.h"

Draw::Draw(HDC hdc, int xDest, int yDest, int DestWidth, int DestHeight, int xSrc, int ySrc)
{
	int width = DestWidth;
	int height = DestHeight;
	LPVOID memory = VirtualAlloc(0,
		width * height * 4,
		MEM_RESERVE | MEM_COMMIT,
		PAGE_READWRITE
	);

	bitmap_info = typedef struct tagBITMAPINFO {
		BITMAPINFOHEADER bmiHeader;
		RGBQUAD          bmiColors[1];
	} BITMAPINFO, * LPBITMAPINFO, * PBITMAPINFO;


	StretchDIBits(hdc, xDest, yDest, width, height, xSrc, ySrc, width, height, memory, &bitmap_info, DIB_RGB_COLORS, SRCCOPY);
}

void Draw::DrawImage(std::vector<std::vector<int>> image)
{
}

