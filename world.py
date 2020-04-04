from player import Player
from food import Food
from obstacle import Obstacle
from typing import List
import numpy as np
from constans import MAP_OBJECT_VALUES


class World:
    players: List[Player] = []
    foods: List[Food] = []
    obstacles: List[Obstacle] = []

    def __init__(self, size=(10, 10)):
        self.size = size
        self.map = np.zeros(size).astype(int)
        print('World created')

    def __str__(self):
        print(self.map.T)
        return ''

    @staticmethod
    def log(message: str, message_type: str = 'info'):
        print(f'{message_type.upper()} - {message}')

    def player_register(self, player: Player):
        self.players.append(player)

    def food_append(self, food: Food):
        self.foods.append(food)

    def food_remove(self, position):
        for food_index, food_item in enumerate(self.foods):
            if food_item.position == position:
                del self.foods[food_index]

    def add_obstacles(self, count=10):
        for obstacle in range(count):
            obstacle_position = [np.random.randint(0, self.size[0]), np.random.randint(0, self.size[1])]
            self.obstacles.append(Obstacle(obstacle_position))

    def map_update(self):
        self.map = np.zeros(self.size).astype(int)
        for player in self.players:
            self.map[player.position[0], player.position[1]] = player.id
        for food in self.foods:
            self.map[food.position[0], food.position[1]] = MAP_OBJECT_VALUES['FOOD']
        for obstacle in self.obstacles:
            self.map[obstacle.position[0], obstacle.position[1]] = MAP_OBJECT_VALUES['OBSTACLE']

    @staticmethod
    def get_new_position(player: Player, next_direction: list):
        x, y = player.position
        if next_direction == 'left':
            x = player.position[0] - 1
        if next_direction == 'right':
            x = player.position[0] + 1
        if next_direction == 'up':
            y = player.position[1] - 1
        if next_direction == 'down':
            y = player.position[1] + 1
        if next_direction == 'stay':
            pass
        return [x, y]

    def check_players_turn_collisions(self):
        for index, player in enumerate(self.players):
            player.is_last_move_success = True
            for other_player in self.players[index+1:]:
                if player.new_position == other_player.new_position:
                    player.is_last_move_success = False

    def do_players_moves(self):
        for player in self.players:
            if player.is_last_move_success:
                player.position = player.new_position
                if self.map[player.new_position[0], player.new_position[1]] == MAP_OBJECT_VALUES["FOOD"]:
                    player.score += 1
                    World.log(f'Player {player.id} ({player.name}) eat the food in {player.position}')
                    self.food_remove(player.new_position)




    def tick(self):
        # shuffle players turns
        np.random.shuffle(self.players)
        # ask new players positions
        for player in self.players:
            player.update_state(self.map, player.position)
            next_direction = player.get_next_action()
            player.new_position = self.get_new_position(player, next_direction)
        self.check_players_turn_collisions()
        self.do_players_moves()
        self.map_update()


