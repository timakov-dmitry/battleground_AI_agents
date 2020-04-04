import numpy as np
from constans import MAP_OBJECT_VALUES


class Agent:
    position: list = None
    world_map: np.array
    score: int = 0

    def __init__(self):
        self.log('Bot started', 'info')

    @staticmethod
    def log(message: str, message_type: str):
        print(f'{message_type.upper() } - {message}')

    def update_state(self, state: dict):
        self.position = state["position"]
        self.world_map = state["world_map"]
        self.score = state["score"]

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

    def get_next_action(self):
        return 'stay'
