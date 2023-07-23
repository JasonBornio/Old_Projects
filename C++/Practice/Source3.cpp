#include <iostream>
#include <cstring>

using namespace std;

int main() {
	char a[100], b[100], type[100];
	int boolean = 1;
	cout << "enter some strings\n";
	cin >> a >> b;
	while (1) {
		cout << "select mode: 1 = compare, 2 = copy\n";
		cin >> type;
		boolean = strcmp(type, "1");
		if (!boolean) {
			int compare = strcmp(a, b);
			if (!compare) {
				cout << "the two strings are eqaul\n";
			}
			else {
				cout << "the two strings are different\n";
			}
			cout << "the output of strcmp is:" << compare;
			break;
		}
		boolean = strcmp(type, "2");
		if (!boolean) {
			strcpy(a, b);
			cout << "the two strings are:" << a << b;
			break;
		}

	}
	//return 0;
}