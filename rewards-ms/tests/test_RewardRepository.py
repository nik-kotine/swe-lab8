from app.adapters.SQLiteRewardRepository import SQLiteRewardRepository
from app.domain.Reward import Reward

def test_SaveRewardShouldSaveReward(tmp_path):
    db_file = tmp_path / "test.db"
    repository = SQLiteRewardRepository(db_path = db_file)
    reward = Reward(user_id = "JOHNID", reward_points = 10)
    repository.save_reward(reward)
