import pika

credentials = pika.PlainCredentials("students", "Ut3c2026")
parameters = pika.ConnectionParameters("213.199.42.57", 5672, "/", credentials)

try:
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    queue_name = "laboratorio_1"
    channel.queue_declare(queue = queue_name, durable = True)
    message = "¡Hola! Este es el primer mensaje del laboratorio"
    channel.basic_publish(exchange = "", routing_key = queue_name, body = message)
    print(f"[x] Mensaje enviado exitosamente: '{message}'")

except Exception as e:
    print(f"[!] Error de conexión: {e}")

finally:
    if "conexion" in locals() and connection.is_open:
        connection.close()


