#include <SFML/Graphics.hpp>
#include <vector>
#include "PhysicsSolver.h"
#include <iostream>
#include "globalItems.h"
#include "PlantCell.h"
#include "Cell.h"
#include <Windows.h>

std::vector<sf::CircleShape> shapes;
std::vector<pheromone*> global_pheromones = {};
std::vector<Cell*> global_prey = {};
std::vector<Cell*> global_predators = {};
solver physics;
Cell* topG;
bool ready = false;
bool toggleDNA = false;
bool toggleNET = false;
bool switchDNA = false;
int indexa = 0;


void spawnEntity(float radius, sf::Vector2f position) {
    sf::CircleShape shape(radius);
    //sf::Vector2f position(0, 0);
    shape.setPosition(position);
    shape.setFillColor(sf::Color::Green);
    shapes.push_back(shape);
}

void removeDead() {
    //std::cout << "\nHey1";
    int shift = 0;
    for (int i = 0; i < global_prey.size(); i++) {
        if (global_prey[i]->dead) {
            global_prey[i]->~Cell();
            global_prey.erase(global_prey.begin() + i);
            shift += 1;
        }
        else {
            global_prey[i]->tag -= shift;
        }
    }
    int shift2 = 0;
   // std::cout << "\nHey2";
    for (int i = 0; i < global_predators.size(); i++) {
        //std::cout << "\nHey6";
        if (global_predators[i]->dead) {
            //std::cout << "\nHey7";
            global_predators[i]->~Cell();
            //std::cout << "\nHey8";
            global_predators.erase(global_predators.begin() + i);
            //std::cout << "\nHey9";
            //std::cout << "\nHey10";
            shift2 += 1;
        }
        else {
            global_predators[i]->tag -= shift2;
        }

    }
    //std::cout << "\nHey11";
    physics.entity_list = {};
    shapes = {};
    for (int i = 0; i < global_prey.size(); i++) {
        physics.entity_list.push_back(global_prey[i]);
        sf::CircleShape circle(global_prey[i]->getRadius());
        circle.setPosition(global_prey[i]->position_current);
        global_prey[i]->index = shapes.size();
        shapes.push_back(circle);
        global_prey[i]->setColour2(shapes);

    }
    //std::cout << "\nHey5";
    for (int i = 0; i < global_predators.size(); i++) {
        physics.entity_list.push_back(global_predators[i]);
        sf::CircleShape circle(global_predators[i]->getRadius());
        circle.setPosition(global_predators[i]->position_current);
        global_predators[i]->index = shapes.size();
        shapes.push_back(circle);
        global_predators[i]->setColour2(shapes);
    }
    //std::cout << "\npredators:" << global_predators.size();
    //std::cout << "\nprey:" << global_prey.size();
    //std::cout << "\nentities:" << physics.entity_list.size();
    //std::cout << "\nshapes:" << shapes.size();
}

void update(float time){
    int i = 0;
    while(i < physics.entity_list.size()) {
        //std::cout << "\nSized2:" << physics.entity_list[i]->getDNA().size();
        physics.entity_list[i]->update(time, physics.entity_list, shapes, global_prey,global_predators,global_pheromones);
        if(physics.entity_list[i]->_age > topG->_age)
            topG = physics.entity_list[i];
        if (physics.entity_list[i]->energy <= 0) {
            //std::cout << "\nHEYO1";
            physics.entity_list[i]->dead = true;
            //physics.entity_list[i]->~Cell();
            //std::cout << "\nDIE";
            //physics.entity_list.erase(physics.entity_list.begin() + i);
            //predators.erase(predators.begin() + (physics.entity_list[i]->tag - tagOffset));
        }
        //std::cout << "\nHEY30";
        i += 1;
    }
    removeDead();
    if(global_predators.size() > 0)
        topG = global_predators[0];
    else
        topG = physics.entity_list[0];
}

void update2(float time) {
    for (int i = 0; i < physics.entity_list.size(); i++) {
        physics.entity_list[i]->checkFitness(time);
        physics.entity_list[i]->handleInputs(global_pheromones);
        physics.entity_list[i]->handleOutputs(global_pheromones);

    }
}

void intialiseCells(int number, int genelength) {
    //std::cout << "\nHey3";
    for (int i = 0; i < number; i++) {
        //std::cout << "\nHey4";
        sf::Vector2f offset((rand() % 601) - 300, (rand() % 601) - 300);
        //std::cout << "\nHey5";
        physics.entity_list.push_back(new Cell(shapes, creature_radius, CENTER +offset));
        //std::cout << "\nHey6";
        physics.entity_list[i]->randomDNA(genelength);
        //std::cout << "\nHey7";
        physics.entity_list[i]->setColour(shapes);
        //std::cout << "\nHey8";
        physics.entity_list[i]->decodeDNA();
        //std::cout << "\nHey9";
    }
    topG = physics.entity_list[0];
}

void instialisePCells() {

    //std::cout << "\nHey3";
    for (int i = 0; i < populationCount/2; i++) {
        //std::cout << "\nHey4";
        sf::Vector2f offset((rand() % 601) - 300, (rand() % 601) - 300);
        //std::cout << "\nHey5";
        physics.entity_list.push_back(new Cell(shapes, creature_radius, CENTER + offset));
        //std::cout << "\nHey6";
        physics.entity_list[i]->randomDNA(DNALENGTH);
       // std::cout<<"\nSized:" << physics.entity_list[i]->getDNA().size();
        //std::cout << "\nHey7";
        physics.entity_list[i]->setColour2(shapes);
        //std::cout << "\nHey8";
        physics.entity_list[i]->decodeDNA();
        //std::cout << "\nHey9";
        physics.entity_list[i]->setTag(i,global_prey,global_predators);

    }
    int size = physics.entity_list.size();
    for (int i = 0; i < predatorCount/2; i++) {
        //std::cout << "\nHey4";
        sf::Vector2f offset((rand() % 601) - 300, (rand() % 601) - 300);
        //std::cout << "\nHey5";
        physics.entity_list.push_back(new Cell(shapes, creature_radius, CENTER + offset));
        //std::cout << "\nHey6";
        physics.entity_list[size+i]->randomDNA(DNALENGTH);
        //std::cout << "\nHey7";
        physics.entity_list[size+i]->setColour2(shapes);
        //std::cout << "\nHey8";
        physics.entity_list[size+i]->decodeDNA();
        //std::cout << "\nHey9";
        physics.entity_list[size+i]->setTag(i + tagOffset, global_prey, global_predators);

    }

    topG = global_predators[0];

}

std::vector<std::vector<int>> getFittestDNA() {
    std::vector<std::vector<int>> DNA = {};
    Cell* bestCell = physics.entity_list[0];
    int index = 0;

    for (int i = 0; i < physics.entity_list.size(); i++) {
        Cell* current = physics.entity_list[i];
        if (current->fitness > bestCell->fitness) {
            bestCell = current;
            index = i;
        }
    }

    DNA = physics.entity_list[index]->getDNA();
    physics.entity_list[index]->~Cell();
    physics.entity_list.erase(physics.entity_list.begin() + index);
    return DNA;
}

float getBestFitness() {
    Cell* bestCell = physics.entity_list[0];
    float fit = -1000000;

    for (int i = 0; i < physics.entity_list.size(); i++) {
        Cell* current = physics.entity_list[i];
        if (current->fitness > fit) {
            fit = current->fitness;
        }
    }

    return fit;
}

float nextGeneration() {
    float bestFit = getBestFitness();
    //std::cout << "\nNEXT1";
    shapes = {};
    std::vector<Cell*> survivor_list;
    int cutoff = int(populationCount * cutoff_percenetage);

    for (int i = 0; i < cutoff; i++) {
        sf::Vector2f offset((rand() % 601) - 300, (rand() % 601) - 300);
        survivor_list.push_back(new Cell(shapes, creature_radius, CENTER + offset));
        //std::cout << "\nNEXT2";
        survivor_list[i]->setDNA(getFittestDNA());
        //std::cout << "\nNEXT3";
    }
    //std::cout << "\nNEXT4";
    int initSize = survivor_list.size();
    int count = 0;

    while (survivor_list.size() < populationCount) {
        sf::Vector2f offset((rand() % 601) - 300, (rand() % 601) - 300);
        survivor_list.push_back(new Cell(shapes, creature_radius, CENTER + offset));
        int parent_index_1 = rand() % initSize;
        int parent_index_2 = rand() % initSize;
        survivor_list[survivor_list.size()-1]->mixDNA(mutation_chance, survivor_list[parent_index_1]->getDNA(), survivor_list[parent_index_2]->getDNA());
        count += 1;
        //std::cout << "\nNEXT5";
    }
    //std::cout << "\nNEXT6";

    for (int i = 0; i < physics.entity_list.size(); i++) {
        physics.entity_list[i]->~Cell();
        physics.entity_list.erase(physics.entity_list.begin() + i);
    }

    physics.entity_list = survivor_list;

    for (int i = 0; i < physics.entity_list.size(); i++) {
        physics.entity_list[i]->setColour(shapes);
        physics.entity_list[i]->decodeDNA();
    }
    topG = physics.entity_list[0];
    return bestFit;
}

void checkKeys(sf::RenderWindow& win){

    if (sf::Keyboard::isKeyPressed(sf::Keyboard::Escape))
        win.close();

    if (sf::Keyboard::isKeyPressed(sf::Keyboard::N)) {
        if (toggleNET == true)
            toggleNET = false;
        else
            toggleNET = true;
    }

    if (sf::Keyboard::isKeyPressed(sf::Keyboard::D)) {
        if (toggleDNA == true)
            toggleDNA = false;
        else
            toggleDNA = true;
    }
}

int main()
{
    sf::RenderWindow window(sf::VideoMode(1500, 1000), "SFML works!");
    window.setFramerateLimit(60);
    window.setPosition(sf::Vector2i(430, 0));
    sf::Clock clock;
    float oldElapsed = 0;
    int limit = 0;
    int count = 0;
    float time = 0;
    int generation = 0;
    float genTime = 0.f;
    float elapsed = 0;
    float fit = 0;
    std::string info;

    sf::CircleShape shape(RADIUS);
    shape.setPosition(CENTER.x - RADIUS, CENTER.y - RADIUS);
    intialiseCells(populationCount, DNALENGTH);

    sf::Text text;
    sf::Font font;
    font.loadFromFile("C:/Windows/Fonts/arial.ttf");
    text.setFont(font);
    text.setString(std::to_string(generation));
    text.setFillColor(sf::Color::White);
    text.setPosition({ 960,10 });
    text.setCharacterSize(13);

    while (window.isOpen())
    {
        sf::Event event;
        while (window.pollEvent(event))
        {
            if (event.type == sf::Event::Closed)
                window.close();

        }

       // if (sf::Keyboard::isKeyPressed(sf::Keyboard::Escape))
         //   window.close();

        if (sf::Keyboard::isKeyPressed(sf::Keyboard::N)) {
            if (toggleNET == true)
                toggleNET = false;
            else
                toggleNET = true;
        }

        if (sf::Keyboard::isKeyPressed(sf::Keyboard::D)) {
            if (toggleDNA == true)
                toggleDNA = false;
            else
                toggleDNA = true;
        }

        if (sf::Keyboard::isKeyPressed(sf::Keyboard::S)) {
            if (switchDNA == true)
                switchDNA = false;
            else
                switchDNA = true;
        }

        if (sf::Keyboard::isKeyPressed(sf::Keyboard::Up)) {
            if (indexa != physics.entity_list.size() - 1)
                indexa += 1;
        }
        if (sf::Keyboard::isKeyPressed(sf::Keyboard::Down)) {
            if (indexa != 0)
                indexa -= 1;
        }

        info = "";
        elapsed = clock.getElapsedTime().asSeconds();
        window.clear();

        if (elapsed - time > 20.f) {
            ready = true;
            fit = nextGeneration();
            generation += 1;
            //Sleep(1000);
            time = elapsed;
        }


        update2(elapsed - time);
        physics.update(elapsed - oldElapsed);
        //std::cout << "\nHEY31";
        oldElapsed = elapsed;

        if (switchDNA)
            physics.entity_list[indexa]->setColour(shapes, sf::Color(50, 50, 50));
        else
            topG->setColour(shapes, sf::Color(50, 50, 50));
        //std::cout << "\nHEY32";

        if (toggleDNA && toggleNET) {
            if (switchDNA) {
                info += physics.entity_list[indexa]->brain.displayNet(physics.entity_list[indexa]->fitness);
                info += physics.entity_list[indexa]->displayStats();
                physics.entity_list[indexa]->brain.drawNet(window);
                info += physics.entity_list[indexa]->displayDNA();
            }
            else {
                info += topG->brain.displayNet(topG->fitness);
                info += topG->displayStats();
                topG->brain.drawNet(window);
                info += topG->displayDNA();
            }
        }
        else if (toggleNET) {
            if (switchDNA) {
                info += physics.entity_list[indexa]->brain.displayNet(physics.entity_list[indexa]->fitness);
                info += physics.entity_list[indexa]->displayStats();
                physics.entity_list[indexa]->brain.drawNet(window);
            }
            else {
                info += topG->brain.displayNet(topG->fitness);
                info += topG->displayStats();
                topG->brain.drawNet(window);
            }
        }
        else if (toggleDNA) {
            if (switchDNA)
                info = physics.entity_list[indexa]->displayDNA();
            else
                info = topG->displayDNA();

        }

        text.setString(std::to_string(elapsed - time) + "\nGEN:: " + std::to_string(generation) + "\nBestFitness:: " + std::to_string(fit) + info);
        window.draw(shape);
        //Draw
        window.draw(text);
        for (int i = 0; i < shapes.size(); i++)
        {
            //std::cout << "\nHEY33";
            float radius = physics.entity_list[i]->getRadius();
            //std::cout << "\nHEY34";
            sf::Vector2f offset(radius, radius);
            //std::cout << "\nHEY35";
            shapes[i].setPosition(physics.entity_list[i]->position_current - offset);
            //std::cout << "\nHEY36";
            //std::cout << "\nSHAPES::" << shapes.size();
            //std::cout << "\nCells::" << physics.entity_list.size();
            //std::cout << "\ni: " << i;
            window.draw(shapes[i]);
        }
        //std::cout << "\nHEY37";
        //Draw

        window.display();
    }
    return 0;
}


//
/*
int main()
{
    sf::RenderWindow window(sf::VideoMode(1500, 1000), "SFML works!");
    window.setFramerateLimit(60);
    window.setPosition(sf::Vector2i(430, 0));
    sf::Clock clock;
    float oldElapsed = 0;
    int limit = 0;
    int count = 0;
    float time = 0;
    int generation = 0;
    float genTime = 0.f;
    float elapsed;
    std::string info;

    sf::CircleShape shape(RADIUS);
    shape.setPosition(CENTER.x - RADIUS, CENTER.y - RADIUS);
    //intialiseCells(populationCount, DNALENGTH);
    instialisePCells();

    sf::Text text, text2;
    sf::Font font;
    font.loadFromFile("C:/Windows/Fonts/arial.ttf");
    text.setFont(font);
    text.setString(std::to_string(generation));
    text.setFillColor(sf::Color::White);
    text.setPosition({ 960,10 });
    text.setCharacterSize(13);

    while (window.isOpen())
    {
        sf::Event event;
        while (window.pollEvent(event))
        {
            if (event.type == sf::Event::Closed)
                window.close();

        }

        if (sf::Keyboard::isKeyPressed(sf::Keyboard::Escape))
            window.close();

        if (sf::Keyboard::isKeyPressed(sf::Keyboard::N)) {
            if (toggleNET == true)
                toggleNET = false;
            else
                toggleNET = true;
        }

        if (sf::Keyboard::isKeyPressed(sf::Keyboard::D)) {
            if (toggleDNA == true)
                toggleDNA = false;
            else
                toggleDNA = true;
        }

        if (sf::Keyboard::isKeyPressed(sf::Keyboard::S)) {
            if (switchDNA == true)
                switchDNA = false;
            else
                switchDNA = true;
        }

        if (sf::Keyboard::isKeyPressed(sf::Keyboard::Up)) {
            if (indexa != physics.entity_list.size() - 1)
                indexa += 1;
        }
        if (sf::Keyboard::isKeyPressed(sf::Keyboard::Down)) {
            if (indexa != 0)
                indexa -= 1;
        }
        elapsed = clock.getElapsedTime().asSeconds();

        info = "";
        info += "\npredatorCount:" + std::to_string(global_predators.size());
        info += "\npreyCount:" + std::to_string(global_prey.size());
        info += "\nCreature_index:" + std::to_string(indexa);

        window.clear();

        update(elapsed);
        physics.update(elapsed - oldElapsed, global_prey);
        //std::cout << "\nHEY31";
        oldElapsed = elapsed;
        if (switchDNA)
            physics.entity_list[indexa]->setColour(shapes, sf::Color(50, 50, 50));
        else
            topG->setColour(shapes, sf::Color(50, 50, 50));
        //std::cout << "\nHEY32";

        if (toggleDNA && toggleNET) {
            if (switchDNA) {
                info += physics.entity_list[indexa]->brain.displayNet(physics.entity_list[indexa]->fitness);
                info += physics.entity_list[indexa]->displayStats();
                physics.entity_list[indexa]->brain.drawNet(window);
                info += physics.entity_list[indexa]->displayDNA();
            }
            else {
                info += topG->brain.displayNet(topG->fitness);
                info += topG->displayStats();
                topG->brain.drawNet(window);
                info += topG->displayDNA();
            }
        }
        else if (toggleNET) {
            if (switchDNA) {
                info += physics.entity_list[indexa]->brain.displayNet(physics.entity_list[indexa]->fitness);
                info += physics.entity_list[indexa]->displayStats();
                physics.entity_list[indexa]->brain.drawNet(window);
            }
            else {
                info += topG->brain.displayNet(topG->fitness);
                info += topG->displayStats();
                topG->brain.drawNet(window);
            }
        }
        else if (toggleDNA) {
            if (switchDNA) 
                info = physics.entity_list[indexa]->displayDNA();
            else 
                info = topG->displayDNA();
            
        }

        text.setString(std::to_string(elapsed - time) + "\nGEN:: " + std::to_string(generation) + info);
        window.draw(shape);

        for (int i = 0; i < global_pheromones.size(); i++) {
            global_pheromones[i]->update();
            if (global_pheromones[i]->destroy == true) {
                //std::cout << "\nDESTROY";
                global_pheromones.erase(global_pheromones.begin() + i);
            }
            else {
                sf::CircleShape pher(5.f);
                pher.setPosition(global_pheromones[i]->position);
                if (global_pheromones[i]->tag > tagOffset)
                    pher.setFillColor(sf::Color(255, 0, 0,global_pheromones[i]->intensity * 255));
                else
                    pher.setFillColor(sf::Color(0, 255,0,global_pheromones[i]->intensity *255));
                //pher.setRadius(5.f * global_pheromones[i]->intensity);
                window.draw(pher);
            }
        }

        //Draw
        window.draw(text);
        for (int i = 0; i < shapes.size(); i++)
        {
            //std::cout << "\nHEY33";
            float radius = physics.entity_list[i]->getRadius();
            //std::cout << "\nHEY34";
            sf::Vector2f offset(radius, radius);
            //std::cout << "\nHEY35";
            shapes[i].setPosition(physics.entity_list[i]->position_current - offset);
            //std::cout << "\nHEY36";
            //std::cout << "\nSHAPES::" << shapes.size();
            //std::cout << "\nCells::" << physics.entity_list.size();
            //std::cout << "\ni: " << i;
            window.draw(shapes[i]);
        }
        //std::cout << "\nHEY37";
        //Draw

        window.display();
    }
    return 0;
}
*/
/*
if (elapsed - time > 1.5f && count < 5) {
    time = elapsed;
    sf::Vector2f position(RADIUS - 20.f, 0.f);
    float random_radius = ((rand() % 200) / 10) + 5.0f;     // v2 in the range 1 to 100
    spawnCell(random_radius, position);
    count += 1;
}
*/

/*
unsigned char str[16 + 1] = { 0 };
const char* hex_digits = "0123456789ABCDEF";
int i;

for (i = 0; i < 16; i++) {
    str[i] = hex_digits[(rand() % 16)];
}

printf("%s\n", str);
*/

/*
void spawnCell(float radius, sf::Vector2f position) {
    sf::Vector2f offset(0.f, 0.f);
    Entity cell(shapes, radius, position + offset + CENTER);
    cell.accelerate({-10000.f, 1000.f});
    physics.entity_list.push_back(cell);
}

void splitCells(PlantCell& cell) {
    int divisions = int(cell.getRadius()/cell.getInitialRadius());
    std::cout << "\nCHECK1";
    if (divisions < 2) {
        divisions = 2;
        std::cout << "\nCHECK2";
    }
    cell.setRadius(cell.getRadius() / divisions);
    std::cout << "\nCHECK3";
    for (int i = 0; i < divisions-1; i++) {
        sf::Vector2f offset(cell.getRadius() * (i + 1), cell.getRadius() *( i+1));
        PlantCell new_cell(shapes, (cell.getRadius() / divisions), cell.position_current + offset);
        physics.entity_list.push_back(new_cell);
        std::cout << "\nCHECK4";
        std::cout << "\nDIV: "<<divisions;
    }
    std::cout << "\nCHECK5";
}

void update() {
    for (int i = 0; i < physics.entity_list.size(); i++) {
        //PlantCell& cell; = physics.entity_list[i];
        //cell.update();
        //shapes[cell.index].setRadius(cell.getRadius());
        //if(cell.checkSplit())
        //    splitCells(cell);
    }
}
*/

/*
*         if (elapsed - time > 10.f) {
            time = elapsed;
            ready = true;
            nextGeneration();
            generation += 1;
        }
        if (ready && (toggleDNA || toggleNET)) {
            if (toggleDNA && toggleNET) {
                info = topG->brain.displayNet(topG->fitness);
                topG->brain.drawNet(window);
                info += topG->displayDNA();
            }
            else if (toggleNET) {
                info = topG->brain.displayNet(topG->fitness);
                topG->brain.drawNet(window);
            }
            else if (toggleDNA)
                info = topG->displayDNA();

            topG->setColour(shapes, sf::Color(50,50,50));
        }*/