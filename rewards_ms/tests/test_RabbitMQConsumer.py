from unittest.mock import Mock, patch
from rewards_ms.app.adapters.RabbitMQConsumer import RabbitMQConsumer

def test_CallbackShouldProcessTransactionMessage():
    process_reward = Mock()
    consumer = RabbitMQConsumer(
        _parameters = Mock(),
        _queue_name = "transactions",
        _process_reward = process_reward
    )
    body = b'{"user_id":"JOHNID","amount":50}'
    consumer.callback(
        ch = None,
        method = None,
        properties = None,
        body = body
    )
    process_reward.execute.assert_called_once()
    event = process_reward.execute.call_args[0][0]

    assert event.user_id == "JOHNID"
    assert event.amount == 50

def test_ConsumeShouldRegisterConsumer():
    process_reward = Mock()
    consumer = RabbitMQConsumer(
        _parameters = Mock(),
        _queue_name = "transactions",
        _process_reward = process_reward
    )
    fake_channel = Mock()
    fake_connection = Mock()
    fake_connection.channel.return_value = fake_channel
    with patch(
        "rewards_ms.app.adapters.RabbitMQConsumer.pika.BlockingConnection",
        return_value = fake_connection
    ):
        consumer.consume()
    fake_channel.queue_declare.assert_called_once_with(
        queue = "transactions",
        durable = True
    )
    fake_channel.basic_consume.assert_called_once()
