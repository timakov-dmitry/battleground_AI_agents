from player import Player
from food import Food
from obstacle import Obstacle
import numpy as np
from constans import MAP_OBJECT_VALUES


class World:
    def __init__(self, size=(10, 10)):
        self.size = size
        self.map = np.zeros(size).astype(int)
        self.players = []
        self.foods = []
        self.obstacles = []
        print('World created')

    def __str__(self):
        print(self.map.T)
        return ''

    def player_register(self, player: Player):
        self.players.append(player)
        self.map_update()

    def food_append(self, food: Food):
        self.foods.append(food)
        self.map_update()

    def add_obstacles(self, count=10):
        for obstacle in range(count):
            obstacle_position = [np.random.randint(0, self.size[0]), np.random.randint(0, self.size[1])]
            self.obstacles.append(Obstacle(obstacle_position))

    def map_update(self):
        for player in self.players:
            self.map[player.position[0], player.position[1]] = MAP_OBJECT_VALUES['PLAYER']
        for food in self.foods:
            self.map[food.position[0], food.position[1]] = MAP_OBJECT_VALUES['FOOD']
        for obstacle in self.obstacles:
            self.map[obstacle.position[0], obstacle.position[1]] = MAP_OBJECT_VALUES['OBSTACLE']


    def tick(self):
        # ask new players positions
        for player in self.players:
            player.update_state(self.map, player)
            next_direction = player.ask_next_direction()
            if next_direction == 'left':
                player.position[0] = player.position[0] - 1
            if next_direction == 'right':
                player.position[0] = player.position[0] + 1
            if next_direction == 'up':
                player.position[1] = player.position[1] - 1
            if next_direction == 'down':
                player.position[1] = player.position[1] + 1
            if next_direction == 'stay':
                pass


