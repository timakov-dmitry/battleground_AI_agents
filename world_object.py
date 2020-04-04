from typing import List
import uuid


class WorldObject:
    def __init__(self, position: List[int]):
        self.position = position
        self.id = uuid.uuid1()
