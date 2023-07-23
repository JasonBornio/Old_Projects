#include <iostream>
#include <string>

using namespace std;

int main() {
	char line[100];;
	cout << "Write a sentence\n";
	cin.getline(line, 200);
	cout << "You Wrote: " << line;
}