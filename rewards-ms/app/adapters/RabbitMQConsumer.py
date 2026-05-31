import pika
import sys
import os
import json

from ..domain.RewardCalculator import RewardCalculator
from ..domain.TransactionReceived import TransactionReceived
from ..application.ProcessReward import ProcessReward
from ..adapters.SQLiteRewardRepository import SQLiteRewardRepository
from ..config import (
    RABBITMQ_HOST,
    RABBITMQ_PORT,
    RABBITMQ_USER,
    RABBITMQ_PASSWORD,
    RABBITMQ_VHOST,
    RABBITMQ_QUEUE,
)

credentials = pika.PlainCredentials(
    RABBITMQ_USER,
    RABBITMQ_PASSWORD
)

parameters = pika.ConnectionParameters(
    RABBITMQ_HOST,
    RABBITMQ_PORT,
    RABBITMQ_VHOST,
    credentials
)

def main():
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    queue_name = RABBITMQ_QUEUE
    channel.queue_declare(queue = queue_name, durable = True)

    def callback(ch, method, properties, body):
        message = json.loads(body.decode())
        event = TransactionReceived(amount = message["amount"], user_id = message["user_id"])
        calculator = RewardCalculator()
        repository = SQLiteRewardRepository()
        process_reward = ProcessReward(calculator, repository)
        reward = process_reward.execute(event)
        print(f"[!] Recompensa generada: {reward.reward_points} puntos para {reward.user_id}")

    channel.basic_consume(queue = queue_name, on_message_callback = callback, auto_ack = True)
    print(f"[*] Esperando mensajes en la cola '{queue_name}'. Presiona CTRL+C para salir.")
    channel.start_consuming()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[*] Saliendo del consumidor...")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
