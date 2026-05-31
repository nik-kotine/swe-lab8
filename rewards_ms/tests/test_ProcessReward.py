from rewards_ms.app.application.ProcessReward import ProcessReward
from rewards_ms.app.domain.RewardCalculator import RewardCalculator
from rewards_ms.app.domain.TransactionReceived import TransactionReceived
from rewards_ms.app.ports.RewardRepository import RewardRepository

class MockRewardRepository(RewardRepository):

    def __init__(self):
        self.saved_reward = None

    def save_reward(self, reward):
        self.saved_reward = reward

    def _create_table(self):
        pass

def test_ProcessRewardShouldSaveReward():
    repository = MockRewardRepository()
    calculator = RewardCalculator()
    process_reward = ProcessReward(calculator, repository)

    event = TransactionReceived(amount = 100, user_id = "JOHNID")

    reward = process_reward.execute(event)

    assert reward.reward_points == 10
    assert reward.user_id == "JOHNID"
    assert repository.saved_reward == reward
