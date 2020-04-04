from agent import Agent


class LeftAgent(Agent):
    def __init__(self):
        super().__init__()

    def get_next_action(self):
        return 'left'
