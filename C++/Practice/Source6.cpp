#include <iostream>
#include <string>

using namespace std;

int main() {
	string line;
	cout << "Write a sentence\n";
	getline(cin, line);
	cout << "You Wrote: " << line;
	cout << "\nSpelled:";
	for (int i = 0; i < line.length(); i++) {
		cout << line[i] << "-";
	}
}