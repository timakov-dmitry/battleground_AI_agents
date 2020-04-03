import uuid


class WorldObject:
    def __init__(self, position: list):
        self.position = position
        self.id = uuid.uuid1()
