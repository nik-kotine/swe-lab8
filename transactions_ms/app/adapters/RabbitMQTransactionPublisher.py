import json
import pika

from transactions_ms.app.domain.Transaction import Transaction
from transactions_ms.app.ports.TransactionPublisher import TransactionPublisher

class RabbitMQTransactionPublisher(TransactionPublisher):

    def __init__(self, _parameters, _queue_name):
        self.parameters = _parameters
        self.queue_name = _queue_name

    def publish(self, transaction: Transaction):
        connection = pika.BlockingConnection(self.parameters)
        channel = connection.channel()
        channel.queue_declare(queue = self.queue_name, durable = True)
        message = json.dumps({
            "user_id" : transaction.user_id,
            "amount" : transaction.amount,
            "user_card" : transaction.user_card,
            "restaurant_id" : transaction.restaurant_id,
            "date" : transaction.date.isoformat(),
        })
        channel.basic_publish(exchange = "", routing_key = self.queue_name, body = message)
        connection.close()
