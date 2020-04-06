from typing import List, Tuple
from player import Player
from food import Food
from obstacle import Obstacle
import numpy as np
from constans import MAP_OBJECT_VALUES


class World:
    players: List[Player] = []
    foods: List[Food] = []
    obstacles: List[Obstacle] = []

    def __init__(self, size: Tuple[int, int] = (10, 10)):
        self.size = size
        self.map: np.ndarray = np.zeros(size).astype(int)
        print('World created')

    def __str__(self) -> str:
        print(self.map.T)
        return ''

    @staticmethod
    def log(message: str, message_type: str = 'info') -> None:
        print(f'{message_type.upper()} - {message}')

    def player_register(self, player: Player):
        self.players.append(player)

    def add_food(self, count: int = 10, food_position: List[int] = None):
        for food in range(count):
            if not food_position:
                position = [np.random.randint(0, self.size[0]), np.random.randint(0, self.size[1])]
                self.foods.append(Food(position))
            else:
                self.foods.append(Food(food_position))

    def food_remove(self, position: List[int]):
        for food_index, food_item in enumerate(self.foods):
            if food_item.position == position:
                del self.foods[food_index]

    def add_obstacles(self, count: int = 1, obstacle_position: List[int] = None):
        for obstacle in range(count):
            if not obstacle_position:
                position = [np.random.randint(0, self.size[0]), np.random.randint(0, self.size[1])]
                self.obstacles.append(Obstacle(position))
            else:
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
    def get_new_position(player: Player):
        x, y = player.position
        if player.next_action == 'left':
            x = player.position[0] - 1
        if player.next_action == 'right':
            x = player.position[0] + 1
        if player.next_action == 'up':
            y = player.position[1] - 1
        if player.next_action == 'down':
            y = player.position[1] + 1
        if player.next_action == 'stay':
            pass
        return [x, y]

    def check_players_turn_collisions(self):
        for index, player in enumerate(self.players):
            player.is_last_move_success = True
            for other_player in self.players[index+1:]:
                if player.new_position == other_player.new_position:
                    player.is_last_move_success = False

        for player in self.players:
            if player.new_position[0] not in range(self.size[0]):
                player.is_last_move_success = False
            if player.new_position[1] not in range(self.size[1]):
                player.is_last_move_success = False

    def check_players_action_collisions(self):
        for player in self.players:
            if player.next_action == 'build' and player.obstacle_count < 1:
                player.is_last_move_success = False

    def do_players_moves(self):
        for player in self.players:
            if player.is_last_move_success:
                if player.next_action == 'build':
                    self.add_obstacles(1, player.position)
                    player.build_obstacle()

                player.position = player.new_position
                if self.map[player.new_position[0], player.new_position[1]] == MAP_OBJECT_VALUES["FOOD"]:
                    player.eat_food()
                    self.food_remove(player.new_position)

    def tick(self):
        # shuffle players turns
        np.random.shuffle(self.players)
        # ask new players positions
        for player in self.players:
            player.update_state(self.map, player.position)
            player.next_action = player.get_next_action()
            player.new_position = self.get_new_position(player)
            player.is_last_move_success = True

        self.check_players_action_collisions()
        self.check_players_turn_collisions()
        self.do_players_moves()
        self.map_update()

    def finish(self):
        self.players = sorted(self.players, key=lambda p: p.score)
        for player in self.players:
            print(f'Player "{player.name}" has {player.score} points')
        print(f'{self.players[-1].name}  - WINNER!')


