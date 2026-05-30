from dataclasses import dataclass

@dataclass
class Reward:
    user_id: str
    reward_points: float

    def __init__(self, _name: str, _reward_points: float):
        self.name = _name
        self.reward_points = _reward_points
