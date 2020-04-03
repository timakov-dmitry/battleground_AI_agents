import pygame
from world import World
from constans import MAP_OBJECT_VALUES
from OpenGL.GL import *
from OpenGL.GLU import *


class Visualisation:
    CELL_SCALE = 65
    COLORS = {
        "OBSTACLE": [100, 150, 50]
    }

    def __init__(self, world: World):
        pygame.init()
        self.world = world
        self.vis_game = pygame
        self.screen = self.vis_game.display.set_mode([world.size[0]*self.CELL_SCALE, world.size[1]*self.CELL_SCALE])
        self.running = True

    def draw_objects(self):
        self.screen.fill([255, 255, 255])
        for next_x in range(self.world.size[0]):
            self.vis_game.draw.line(self.screen, (0, 0, 255), (next_x*self.CELL_SCALE, 0),
                             (next_x*self.CELL_SCALE, self.world.size[1]*self.CELL_SCALE))
        for next_y in range(self.world.size[1]):
            self.vis_game.draw.line(self.screen, (0, 0, 255), (0, next_y * self.CELL_SCALE),
                             (self.world.size[0] * self.CELL_SCALE, next_y * self.CELL_SCALE))
        for next_x in range(self.world.size[0]):
            for next_y in range(self.world.size[1]):
                if self.world.map[next_x, next_y] == MAP_OBJECT_VALUES['OBSTACLE']:
                    self.vis_game.draw.rect(self.screen,
                                     self.COLORS['OBSTACLE'],
                                     (next_x*self.CELL_SCALE+1,
                                      next_y*self.CELL_SCALE+1,
                                      self.CELL_SCALE-1,
                                      self.CELL_SCALE-1))


    def draw_players(self):
        for player in self.world.players:
            player_image = pygame.image.load(player.image_url).convert()
            self.screen.blit(player_image, (player.position[0] * self.CELL_SCALE + 1,
                                            player.position[1] * self.CELL_SCALE + 1))


    def append_food(self):
        for food in self.world.foods:
            food_image = pygame.image.load(food.image_url).convert()
            self.screen.blit(food_image, (food.position[0] * self.CELL_SCALE + 1,
                                          food.position[1] * self.CELL_SCALE + 1))

    def stop(self):
        self.running = False

    def __del__(self):
        self.vis_game.quit()
