import numpy as np
from world import World
from player import Player
from food import Food
from visualization import Visualisation
from agents.random_agent import RandomAgent
import time

WORLD_SIZE = (10, 10)
COUNT_PLAYERS = 3
COUNT_FOOD = 2
COUNT_OBSTACLES = 20

world = World(WORLD_SIZE)
world.add_obstacles(COUNT_OBSTACLES)

for player in range(COUNT_PLAYERS):
    random_position = [np.random.randint(0, WORLD_SIZE[0]), np.random.randint(0, WORLD_SIZE[1])]
    random_agent = RandomAgent(world, random_position)
    bot = Player(random_agent, random_position)
    world.player_register(bot)

for player in range(COUNT_FOOD):
    food = Food((np.random.randint(0, WORLD_SIZE[0]), np.random.randint(0, WORLD_SIZE[1])))
    world.food_append(food)

view = Visualisation(world)
running = True
counter = 1
while running and counter < 20:
    world.tick()
    view.draw_objects()
    view.draw_players()
    view.append_food()
    view.vis_game.display.flip()
    print(world)
    counter += 1
    for event in view.vis_game.event.get():
        if event.type == view.vis_game.QUIT:
            running = False
    time.sleep(1)



view.stop()
del view

print(world)
