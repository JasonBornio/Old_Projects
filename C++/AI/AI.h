#pragma once
#include <iostream>
#include <vector>

using namespace std;
class AI
{
public:
	AI();
	void user_input();

private:
	vector<vector<string>>knowledge;
	vector<vector<string>>memory;
	void respond();
	void sentance();
};

AI::AI() {

}

void AI::respond() {

}

void AI::sentance() {
	bool period = false;
	while (period == false) {
		cout << knowledge[0][0];
		period = true;
	}
}

void AI::user_input() {
	string word;
	vector<string>x;
	cout << "teach me a senetance starter";
	cin >> word;
	x.push_back(word);
	knowledge.push_back(x);
	sentance();
}

