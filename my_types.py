from typing import TypedDict, List
import numpy as np


class State(TypedDict):
    world_map: np.ndarray
    position: List[int]
    score: int
