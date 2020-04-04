from agent import Agent


class StayAgent(Agent):
    def __init__(self):
        super().__init__()

    def get_next_action(self):
        return 'stay'
