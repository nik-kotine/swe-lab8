import pika
import sys
import os

credentials = pika.PlainCredentials("students", "Ut3c2026")
parameters = pika.ConnectionParameters("213.199.42.57", 5672, "/", credentials)

def main():
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    queue_name = "laboratorio_1"
    channel.queue_declare(queue = queue_name, durable = True)

    def callback(ch, method, properties, body):
        print(f"[x] Mensaje recibido: {body.decode()}")

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
