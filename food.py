from assets import STAR_URL
from world_object import WorldObject
import numpy as np


class Food(WorldObject):
    def __init__(self, position: list):
        WorldObject.__init__(self, position)
        self.image_url = STAR_URL
