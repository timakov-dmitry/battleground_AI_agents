import numpy as np
from world import World
from player import Player
from food import Food
from visualization import Visualisation
import time

WORLD_SIZE = (4, 4)
COUNT_PLAYERS = 1
COUNT_FOOD = 1
COUNT_OBSTACLES = 4
IS_VISUALISATION = False

world = World(WORLD_SIZE)
world.add_obstacles(COUNT_OBSTACLES)

for player_index in range(COUNT_PLAYERS):
    random_position = [np.random.randint(0, WORLD_SIZE[0]), np.random.randint(0, WORLD_SIZE[1])]
    bot = Player(random_position, player_index)
    bot.set_agent()
    world.player_register(bot)

for player in range(COUNT_FOOD):
    food = Food((np.random.randint(0, WORLD_SIZE[0]), np.random.randint(0, WORLD_SIZE[1])))
    world.food_append(food)
if IS_VISUALISATION:
    view = Visualisation(world)

running = True
counter = 1
while running and counter < 20:
    world.tick()
    if IS_VISUALISATION:
        view.draw_objects()
        view.draw_players()
        view.append_food()
        view.vis_game.display.flip()
        for event in view.vis_game.event.get():
            if event.type == view.vis_game.QUIT:
                running = False
    print(world)
    counter += 1
    time.sleep(2)

view.stop()
del view
