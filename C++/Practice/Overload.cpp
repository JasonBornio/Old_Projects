#include "Overload.h"

int main() {
	Overload Number1, Number2;
	Number1.setValue(20);
	Number2.setValue(250);
	int sum = Number1 * Number2;
	cout << sum;
}
