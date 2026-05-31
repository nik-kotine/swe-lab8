import pika
import json
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

try:
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    queue_name = RABBITMQ_QUEUE
    channel.queue_declare(queue = queue_name, durable = True)
    message = json.dumps({
        "amount" : 100.0,
        "user_id" : "JOHNCARD000111",
        "restaurant_id" : "R001"
    })
    channel.basic_publish(exchange = "", routing_key = queue_name, body = message)
    print(f"[x] Mensaje enviado exitosamente: '{message}'")

except Exception as e:
    print(f"[!] Error de conexión: {e}")

finally:
    if "conexion" in locals() and connection.is_open:
        connection.close()


