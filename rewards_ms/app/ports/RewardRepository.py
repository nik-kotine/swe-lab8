from abc import ABC, abstractmethod

class RewardRepository(ABC):

    @abstractmethod
    def save_reward(self, reward):
        pass

    @abstractmethod
    def _create_table(self):
        pass
