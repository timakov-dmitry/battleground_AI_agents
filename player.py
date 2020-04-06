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
    obstacle_count: int = 0
    agent: Agent = None
    is_last_move_success: bool = False
    world_map: np.ndarray = []
    new_position: List[int] = []
    next_action: str = 'stay'

    def __init__(self, position: List[int], index: int):
        WorldObject.__init__(self, position)
        self.id = index + 5
        self.name = ANIMALS_IMAGES[index]
        self.image_url = f'assets/{self.name}.png'

    def log(self, message: str, message_type: str = 'info') -> None:
        print(f'{message_type.upper() } ({self.name}) - {message}')

    def set_agent(self, agent: Agent = None):
        # todo agent verify methods availability
        if not agent:
            random_agent = RandomAgent()
            self.agent = random_agent
        else:
            self.agent = agent
            self.agent.connect_player(self)
        print(f'Player {self.id} using {agent.__class__.__name__}')

    def update_state(self, world_map: np.ndarray, position: List[int]):
        self.world_map = world_map
        self.position = position

    def eat_food(self):
        self.score += 1
        self.obstacle_count += 1
        self.log(f'Player {self.id} ({self.name}) eat the food in {self.position}. Player score {self.score} points', 'info')

    def build_obstacle(self):
        self.obstacle_count -= 1
        self.log(f'Player {self.id} ({self.name}) build obstacle in {self.position}', 'info')

    def destroy_obstacle(self):
        self.obstacle_count -= 1
        self.log(f'Player {self.id} ({self.name}) destroyed obstacle in {self.position}', 'info')

    @property
    def state(self):
        return {
            "world_map": self.world_map,
            "position": self.position,
            "score": self.score
        }

    def is_next_action_available(self, action) -> bool:

        return True

    def get_next_action(self) -> str:
        self.agent.update_state(self.state)
        action = self.agent.get_next_action()
        if action not in AVAILABLE_ACTION:
            self.agent.log('Wrong action name', 'error')
            return 'stay'

        return action
