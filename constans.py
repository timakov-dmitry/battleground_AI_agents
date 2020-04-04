from typing import List, Dict

MAP_OBJECT_VALUES: Dict = {
    "PLAYER": -1,
    "OBSTACLE": 1,
    "FOOD":  2,
    "EMPTY": 0
}
AVAILABLE_ACTION: List[str] = ['left', 'right', 'up', 'down', 'stay']
