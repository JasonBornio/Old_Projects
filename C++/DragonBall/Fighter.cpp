#include "Fighter.h"
#include "Actions.h"
#include "Saiyan.h"
#include "Fusion.h"
#include "Transformations.h"

int main() {
	Saiyan goku, vegeta, vegito, buu;
	goku.stats(150, 300, 5, 5, 2000, 1000, 1000, 1000, "Goku");
	vegeta.stats(275, 750, 7, 8, 4500, 2200, 2000, 2000, "Vegeta");
	buu.stats(15000, 30000, 500, 500, 200000, 100000, 100000, 100000, "Buu");
	string a;
	int x = 1;

	goku.get_power_level();
	vegeta.get_power_level();
	potaraFusion(vegito, goku, vegeta);
	buu.get_power_level();
	vegito.get_power_level();

	while (x) {
		cout << "\nPress any key to attack";
		cin >> a;
		//superSaiyanGod(goku);
		attack(vegito, buu, 1);
		x = check(buu, x);
		if (x == 0) {
			break;
		}
		attack(buu, vegito, 1);
		x = check(vegito, x);
		//goku.multipliers(1, 1, 1, 1, 1, 1, 1, 1);
	}
}
