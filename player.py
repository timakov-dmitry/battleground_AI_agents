from typing import List
from my_types import State
from assets import ANIMALS_IMAGES
from agent import Agent
from world_object import WorldObject
from constans import AVAILABLE_ACTION
from agents.random_agent import RandomAgent
import numpy as np


class Player(WorldObject):
    score: int = 0
    agent: Agent = None
    is_last_move_success: bool = False
    world_map: np.ndarray = []
    new_position: List[int] = []

    def __init__(self, position: List[int], index: int):
        WorldObject.__init__(self, position)
        self.id = index + 5
        self.name = ANIMALS_IMAGES[index]
        self.image_url = f'assets/{self.name}.png'

    def set_agent(self, agent: Agent = None):
        # todo agent verify methods availability
        if not agent:
            random_agent = RandomAgent()
            self.agent = random_agent
        else:
            self.agent = agent

    def update_state(self, world_map: np.ndarray, position: List[int]):
        self.world_map = world_map
        self.position = position

    @property
    def state(self) -> State:
        return {
            "world_map": self.world_map,
            "position": self.position,
            "score": self.score
        }

    def get_next_action(self) -> str:
        self.agent.update_state(self.state)
        action = self.agent.get_next_action()
        if action not in AVAILABLE_ACTION:
            self.agent.log('Wrong action name', 'error')
            return 'stay'
        return action
