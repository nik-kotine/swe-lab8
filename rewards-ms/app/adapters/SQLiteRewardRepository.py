import sqlite3
from app.ports.RewardRepository import RewardRepository
from pathlib import Path
from app.config import REWARDS_DB

QUERIES_DIR = Path(__file__).resolve().parent / "queries"

def load_sql(file_name: str):
    file_name = str(QUERIES_DIR) + "/" + file_name
    with open(file_name, "r") as f:
        return f.read()

class SQLiteRewardRepository(RewardRepository):

    def __init__(self, db_path = REWARDS_DB):
        self.db_path = db_path
        self._create_table()

    def _create_table(self):
        connection = sqlite3.connect(self.db_path)
        query = load_sql("CreateRewardsTable.sql")
        connection.execute(query)
        connection.commit()
        connection.close()

    def save_reward(self, reward):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        query = load_sql("SelectPointsFromUser.sql")
        cursor.execute(query, (reward.user_id,))
        row = cursor.fetchone()

        if row is None:
            query = load_sql("InsertIntoRewards.sql")
            cursor.execute(query, (reward.user_id, reward.reward_points))
        else:
            new_total = row[0] + reward.reward_points
            query = load_sql("UpdateRewards.sql")
            cursor.execute(query, (new_total, reward.user_id))

        connection.commit()
        connection.close()


