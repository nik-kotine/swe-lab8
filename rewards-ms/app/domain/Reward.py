from dataclasses import dataclass

@dataclass
class Reward:
    user_id: str
    reward_points: float
