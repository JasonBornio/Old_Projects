#include "Fighter.h"
#include "Actions.h"
#include "Transformations.h"

int main() {
	Fighter fighter, fighter2;
	fighter.set_stats();
	fighter2.set_stats();
	dark(fighter);
	silver(fighter2);
	melee_attack(fighter, fighter2);
}