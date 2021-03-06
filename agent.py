from typing import List, Dict
from my_types import State
import numpy as np
from constans import MAP_OBJECT_VALUES
import numpy as np


class Agent:
    position: List[int] = None
    world_map: np.array
    player = None
    score: int = 0

    def __init__(self):
        pass

    def connect_player(self, player):
        self.player = player

    def update_state(self, state):
        self.position = state["position"]
        self.world_map = state["world_map"]
        self.score = state["score"]

    # this can be override in agent inheritor
    def get_available_directions(self) -> list:
        available_directions = []
        available_cells = [MAP_OBJECT_VALUES['EMPTY'], MAP_OBJECT_VALUES['FOOD']]
        if self.position[0]-1 > 0 and self.world_map[self.position[0]-1, self.position[1]] in available_cells:
            available_directions.append('left')
        if self.position[0]+1 < self.world_map.shape[0] and self.world_map[self.position[0]+1, self.position[1]] in available_cells:
            available_directions.append('right')
        if self.position[1]+1 < self.world_map.shape[1] and self.world_map[self.position[0], self.position[1]+1] in available_cells:
            available_directions.append('down')
        if self.position[1]-1 > 0 and self.world_map[self.position[0], self.position[1]-1] in available_cells:
            available_directions.append('up')
        return available_directions

    # this mast be override in agent inheritor
    def get_next_action(self) -> str:
        return 'stay'
