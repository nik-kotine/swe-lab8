import json
from unittest.mock import Mock, patch
from transactions_ms.app.adapters.RabbitMQTransactionPublisher import RabbitMQTransactionPublisher
from transactions_ms.app.domain.Transaction import Transaction
from datetime import datetime

def test_PublishShouldSendTransactionToQueue():
    publisher = RabbitMQTransactionPublisher(_parameters = Mock(), _queue_name = "transactions")
    transaction = Transaction(
        user_id = "JOHNID",
        amount = 50,
        user_card = "CARD001",
        restaurant_id = "R001",
        date = datetime(2025, 1, 1)
    )
    fake_channel = Mock()
    fake_connection = Mock()
    fake_connection.channel.return_value = fake_channel

    with patch(
        "transactions_ms.app.adapters.RabbitMQTransactionPublisher.pika.BlockingConnection",
        return_value = fake_connection
    ):
        publisher.publish(transaction)

    fake_channel.queue_declare.assert_called_once_with(
        queue = "transactions",
        durable = True
    )
    fake_channel.basic_publish.assert_called_once()
    fake_connection.close.assert_called_once()

def test_PublishShouldSerializeTransactionCorrectly():

    publisher = RabbitMQTransactionPublisher(
        _parameters = Mock(),
        _queue_name = "transactions"
    )

    transaction = Transaction(
        user_id = "JOHNID",
        amount = 50,
        user_card = "CARD001",
        restaurant_id = "R001",
        date = datetime(2026, 1, 1)
    )

    fake_channel = Mock()
    fake_connection = Mock()
    fake_connection.channel.return_value = fake_channel

    with patch(
        "transactions_ms.app.adapters.RabbitMQTransactionPublisher.pika.BlockingConnection",
        return_value = fake_connection
    ):

        publisher.publish(transaction)

    _, kwargs = fake_channel.basic_publish.call_args

    message = json.loads(kwargs["body"])

    assert message["user_id"] == "JOHNID"
    assert message["amount"] == 50
    assert message["user_card"] == "CARD001"
    assert message["restaurant_id"] == "R001"
    assert message["date"] == "2026-01-01T00:00:00"
