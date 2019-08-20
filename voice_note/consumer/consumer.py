import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

if not sys.argv[1:]:
    sys.stderr.write("Usage: %s [exchange_name] [binding_key]...\n" % sys.argv[0])
    sys.exit(1)

try:
    channel.exchange_declare(exchange=sys.argv[1], exchange_type='topic', durable=True)
except Exception as e:
    print('Exception while connecting to exchange: ', e)
    sys.exit(1)

binding_keys = sys.argv[2:]
if not binding_keys:
    sys.stderr.write("Usage: %s [binding_key]...\n" % sys.argv[0])
    sys.exit(1)

queue_name = sys.argv[2].split('.')[0]
for binding_key in binding_keys:
    channel.queue_bind(
        exchange=sys.argv[1], queue=binding_key, routing_key=binding_key)

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))


channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()
