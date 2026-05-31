from app.domain.RewardCalculator import RewardCalculator
from app.domain.Reward import Reward
from app.domain.TransactionReceived import TransactionReceived
from app.ports.RewardRepository import RewardRepository

class ProcessReward:
    calculator: RewardCalculator
    repository: RewardRepository

    def __init__(self, _calculator: RewardCalculator, _repository: RewardRepository):
        self.calculator = _calculator
        self.repository = _repository

    def execute(self, event: TransactionReceived) -> Reward:
        points = self.calculator.calculate_reward(event.amount)
        reward = Reward(user_id = event.user_id, reward_points = points)
        self.repository.save_reward(reward)
        return reward
