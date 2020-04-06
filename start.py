import numpy as np
from world import World
from player import Player
from food import Food
from visualization import Visualisation
from agents.left_agent import LeftAgent
from agents.stay_agent import StayAgent
from agents.random_agent import RandomAgent
import time

WORLD_SIZE = (12, 12)
COUNT_PLAYERS = 5
COUNT_FOOD = 20
COUNT_OBSTACLES = 15
COUNT_EPOCH = 200
APPEAR_NEW_FOOD_EPOCH = 1
IS_VISUALISATION = True

agents = [LeftAgent, StayAgent, RandomAgent]

world = World(WORLD_SIZE)
world.add_obstacles(COUNT_OBSTACLES)
world.add_food(COUNT_FOOD)

for player_index in range(COUNT_PLAYERS):
    random_position = [np.random.randint(0, WORLD_SIZE[0]), np.random.randint(0, WORLD_SIZE[1])]
    bot = Player(random_position, player_index)
    Agent = np.random.choice(agents)
    bot.set_agent(Agent())
    world.player_register(bot)

if IS_VISUALISATION:
    view = Visualisation(world)

running = True
counter = 1
while running and counter < COUNT_EPOCH:
    world.tick()
    if IS_VISUALISATION:
        view.draw_objects()
        view.draw_players()
        view.append_food()
        view.vis_game.display.flip()
        for event in view.vis_game.event.get():
            if event.type == view.vis_game.QUIT:
                running = False
    else:
        print(world)
    counter += 1
    if counter % APPEAR_NEW_FOOD_EPOCH == 0:
        world.add_food(1)
    time.sleep(0.1)

world.finish()
if IS_VISUALISATION:
    view.stop()
    del view
