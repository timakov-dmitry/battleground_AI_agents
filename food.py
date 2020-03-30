from assets import STAR_URL
import numpy as np


class Food:
    def __init__(self, position=(0, 0)):
        self.position = position
        self.image_url = STAR_URL
