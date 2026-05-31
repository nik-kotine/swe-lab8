import sqlite3
from app.adapters.SQLiteRewardRepository import SQLiteRewardRepository
from app.domain.Reward import Reward

def test_SaveRewardShouldSaveReward(tmp_path):
    db_file = tmp_path / "test.db"
    repository = SQLiteRewardRepository(db_path = db_file)
    reward = Reward(user_id = "JOHNID", reward_points = 10)
    repository.save_reward(reward)
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()
    cursor.execute("""SELECT user_id, reward_points FROM rewards WHERE user_id = ?""", ("JOHNID", ))
    row = cursor.fetchone()
    connection.close()

    assert row is not None
    assert row[0] == "JOHNID"
    assert row[1] == 10

