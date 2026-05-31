import pika
import json
from rewards_ms.app.domain.TransactionReceived import TransactionReceived

class RabbitMQConsumer:

    def __init__(self, _parameters, _queue_name, _process_reward):
        self.parameters = _parameters
        self.queue_name = _queue_name
        self.process_reward = _process_reward

    def callback(self, ch, method, properties, body):
        message = json.loads(body.decode())
        event = TransactionReceived(amount = message["amount"], user_id = message["user_id"])
        reward = self.process_reward.execute(event)
        print(f"[!] Recompensa generada: {reward.reward_points} puntos para {reward.user_id}")

    def consume(self):
        connection = pika.BlockingConnection(self.parameters)
        channel = connection.channel()
        channel.queue_declare(queue = self.queue_name, durable = True)
        channel.basic_consume(
            queue = self.queue_name,
            on_message_callback = self.callback,
            auto_ack = True
        )
        channel.start_consuming()
