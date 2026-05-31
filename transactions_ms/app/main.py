import pika
from datetime import datetime
from transactions_ms.app.domain.Transaction import Transaction
from transactions_ms.app.application.RegisterTransaction import RegisterTransaction
from transactions_ms.app.adapters.RabbitMQTransactionPublisher import RabbitMQTransactionPublisher
from common.config import (
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

publisher = RabbitMQTransactionPublisher(parameters, RABBITMQ_QUEUE)

use_case = RegisterTransaction(publisher)

transaction = Transaction(
    user_id = "JOHNID",
    amount = 50,
    user_card = "JOHN-CARD-6767-8989",
    restaurant_id = "R001",
    date = datetime.now()
)

use_case.execute(transaction)

print("[!] Transacción publicada")
