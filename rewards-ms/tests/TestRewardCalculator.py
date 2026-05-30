from ..app.domain.RewardCalculator import RewardCalculator
import pytest

def CalculatePositiveAmountShouldReturnValue():
    calc = RewardCalculator()
    assert calc.calculate_reward(50) == 5

def CalculateZeroAmountShouldReturnZero():
    calc = RewardCalculator()
    assert calc.calculate_reward(0) == 0

def CalculateNegativeAmountShouldRaiseValueError():
    calc = RewardCalculator()
    with pytest.raises(ValueError):
        calc.calculate_reward(-50)

