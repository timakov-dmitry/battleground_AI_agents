from agent import Agent
import numpy as np


class RandomAgent(Agent):
    def __init__(self):
        super().__init__()

    def get_next_action(self):
        available_directions = self.get_available_directions()
        return 'stay' if len(available_directions) < 1 else np.random.choice(available_directions)
