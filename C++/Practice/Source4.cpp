#include <iostream>
#include <string>

using namespace std;

int main() {
	string phrase;
	string adjective("super"), noun("Vegeta");
	string wish = "Bring them back!";

	phrase = "I am " + adjective + " " + noun + "!";
	cout << phrase << endl
		<< wish << endl;
	return 0;
}