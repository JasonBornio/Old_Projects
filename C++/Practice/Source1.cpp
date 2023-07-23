#include <iostream>
#include <cstring>

using namespace std;

int main() {
	char ch[10] = "hello";
	strcat(ch, "bye");
	cout << ch;
} 