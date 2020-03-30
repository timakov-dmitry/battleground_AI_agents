from assets import ANIMALS_IMAGES
from agent import Agent
import numpy as np


class Player:
    SENSE_RANGE = 3

    def __init__(self, agent: Agent, position=[0, 0]):
        self.position = position
        self.name = np.random.choice(ANIMALS_IMAGES)
        self.image_url = f'assets/{self.name}.png'
        self.available_directions = []
        self.score = 0
        self.agent = agent

    def update_state(self, world_map, position):
        self.agent.set_new_state(world_map, position)

    def ask_next_direction(self) -> str:
        return self.agent.get_next_move()