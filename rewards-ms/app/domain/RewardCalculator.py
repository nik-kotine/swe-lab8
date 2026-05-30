class RewardCalculator:
    
    @staticmethod
    def calculate_reward(amount: float) -> float:
        if amount < 0:
            raise ValueError("reward amount cannot be negative")
        return 0.1 * amount
