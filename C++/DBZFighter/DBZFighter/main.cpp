#include "Player.h"

solver physics;
std::vector<RectangleShape> shapes;
RectangleShape arena(ARENA_RATIO);
Text text;

void renderObjects(RenderWindow& window) {
    window.clear();
    window.draw(arena);
    window.draw(text);
    for (int i = 0; i < shapes.size(); i++)
    {
        Vector2f hitbox = physics.fighter_list[i]->getHitBox();
        Vector2f offset(hitbox.x / 2, hitbox.y / 2);
        shapes[i].setPosition(physics.fighter_list[i]->position_current - offset);
        window.draw(shapes[i]);
    }
    window.display();
}

int main()
{
    RenderWindow window(VideoMode(1500, 1000), "SFML works!");
    window.setFramerateLimit(60);
    window.setPosition(Vector2i(430, 0));

    Clock clock;
    float oldElapsed = 0;
    float elapsed;

    arena.setPosition(CENTER.x - arena.getSize().x/2, CENTER.y - arena.getSize().y/2);

    Font font;
    font.loadFromFile("C:/Windows/Fonts/arial.ttf");
    text.setFont(font);

    physics.fighter_list.push_back(new Fighter(shapes, CENTER));
    Player player;
    player.setPlayer(physics.fighter_list[0]);

    while (window.isOpen())
    {
        Event event;
        elapsed = clock.getElapsedTime().asSeconds();
        while (window.pollEvent(event))
        {
            if (event.type == sf::Event::Closed)
                window.close();
        }

        if (Keyboard::isKeyPressed(Keyboard::Escape))
            window.close();

        //handle physics
        player.update();
        physics.update(elapsed - oldElapsed);
        oldElapsed = elapsed;

        //draw objects
        renderObjects(window);

    }
    return 0;
}