from agent import Agent
import numpy as np


class RandomAgent(Agent):
    def __init__(self):
        super().__init__()

    def get_next_action(self):
        available_actions = self.get_available_directions()
        if self.player.obstacle_count > 0:
            available_actions = ['left', 'right', 'up', 'down', 'left', 'right', 'up', 'down', 'build']
        return 'stay' if len(available_actions) < 1 else np.random.choice(available_actions)
