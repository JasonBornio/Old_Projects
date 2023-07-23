#include <iostream>
#include <cstring>

using namespace std;

int main() {
	char a[100], b[100], c[100], d[100];
	cout << "Inputs Please!!:";
	cin >> a >> b >> c >> d;
	strcat(c, d);
	strcat(b, c);
	strcat(a, b);
	cout << a;
}