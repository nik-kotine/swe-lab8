from rewards_ms.app.domain.RewardCalculator import RewardCalculator
import pytest

def test_CalculatePositiveAmountShouldReturnValue():
    calc = RewardCalculator()
    assert calc.calculate_reward(50) == 5

def test_CalculateZeroAmountShouldReturnZero():
    calc = RewardCalculator()
    assert calc.calculate_reward(0) == 0

def test_CalculateNegativeAmountShouldRaiseValueError():
    calc = RewardCalculator()
    with pytest.raises(ValueError):
        calc.calculate_reward(-50)

