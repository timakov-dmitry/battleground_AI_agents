from typing import NamedTuple, List
import numpy as np


class State(NamedTuple):
    world_map: np.ndarray
    position: List[int]
    score: int
