from unittest.mock import patch

def test_MainShouldStartConsumer():
    with (
        patch("rewards_ms.app.main.SQLiteRewardRepository"),
        patch("rewards_ms.app.main.RewardCalculator"),
        patch("rewards_ms.app.main.ProcessReward"),
        patch("rewards_ms.app.main.RabbitMQConsumer") as consumer_cls,
    ):
        from rewards_ms.app.main import main
        main()
        consumer_cls.return_value.consume.assert_called_once()
