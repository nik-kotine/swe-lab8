import pika

from common.config import (
    RABBITMQ_HOST,
    RABBITMQ_PORT,
    RABBITMQ_USER,
    RABBITMQ_PASSWORD,
    RABBITMQ_VHOST,
    RABBITMQ_QUEUE
)

from rewards_ms.app.domain.RewardCalculator import RewardCalculator
from rewards_ms.app.application.ProcessReward import ProcessReward
from rewards_ms.app.adapters.RabbitMQConsumer import RabbitMQConsumer
from rewards_ms.app.adapters.SQLiteRewardRepository import SQLiteRewardRepository

def main():
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

    calculator = RewardCalculator()
    repository = SQLiteRewardRepository()
    process_reward = ProcessReward(calculator, repository)

    consumer = RabbitMQConsumer(
        parameters,
        RABBITMQ_QUEUE,
        process_reward
    )

    consumer.consume()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[*] Saliendo del consumidor...")



