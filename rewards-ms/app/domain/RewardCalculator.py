from dataclasses import dataclass

@dataclass
class RewardCalculator:
    user_id: str
    amount: float

    def __init__(self, _user_id: str, _amount: float) -> None:
        self.user_id = _user_id
        self.amount = _amount

    def calculate_reward(self) -> float:
        return 0.1 * self.amount
