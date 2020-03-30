from player import Player
from food import Food
import numpy as np


class World:
    def __init__(self, size=(10, 10)):
        self.size = size
        self.map = np.zeros(size).astype(int)
        self.players = []
        self.foods = []
        print('World created')

    def __str__(self):
        print(self.map.T)
        return ''

    def player_register(self, player: Player):
        self.players.append(player)
        self.map[player.position[0], player.position[1]] = 1
        self.map_update()

    def food_append(self, food: Food):
        self.foods.append(food)
        self.map[food.position[0], food.position[1]] = 9
        self.map_update()

    def add_obstacles(self, count=10):
        for obstacle in range(count):
            pos_x = np.random.randint(0, self.size[0])
            pos_y = np.random.randint(0, self.size[1])
            self.map[pos_x, pos_y] = 8

    def map_update(self):
        for player in self.players:
            self.map[player.position] = 1

    def tick(self):
        # ask new players positions
        for player in self.players:
            player.update_state(self.map, player)
            next_direction = player.ask_next_direction()
            if next_direction == 'left':
                self.map[player.position[0], player.position[1]] = 0
                self.map[player.position[0]-1, player.position[1]] = 1
                player.position[0] = player.position[0] - 1
            if next_direction == 'right':
                self.map[player.position[0], player.position[1]] = 0
                self.map[player.position[0]+1, player.position[1]] = 1
                player.position[0] = player.position[0] + 1
            if next_direction == 'up':
                self.map[player.position[0], player.position[1]] = 0
                self.map[player.position[0], player.position[1]-1] = 1
                player.position[1] = player.position[1] - 1
            if next_direction == 'down':
                self.map[player.position[0], player.position[1]] = 0
                self.map[player.position[0], player.position[1]+1] = 1
                player.position[1] = player.position[1] + 1
            if next_direction == 'stay':
                pass


