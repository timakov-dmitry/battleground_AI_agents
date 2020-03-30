import numpy as np


class Agent:
    def __init__(self, world_map, position):
        self.map = world_map
        self.position = position

    def set_new_state(self, world_map, position):
        self.map = world_map

    def get_available_directions(self) -> list:
        available_directions = []
        if self.position[0]-1 > 0 and self.map[self.position[0]-1, self.position[1]] == 0:
            available_directions.append('left')
        if self.position[0]+1 < self.map.shape[0] and self.map[self.position[0]+1, self.position[1]] == 0:
            available_directions.append('right')
        if self.position[1]+1 < self.map.shape[1] and self.map[self.position[0], self.position[1]+1] == 0:
            available_directions.append('down')
        if self.position[1]-1 > 0 and self.map[self.position[0], self.position[1]-1] == 0:
            available_directions.append('up')
        return available_directions

    def get_next_move(self):
        available_directions = self.get_available_directions()
        return 'stay' if len(available_directions) < 1 else np.random.choice(available_directions)
