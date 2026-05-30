from abc import ABC, abstractmethod

class RewardRepository(ABC):

    @abstractmethod
    def save_reward(self, reward):
        pass
