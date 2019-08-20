"""
producer code for sending message to a rabbitmq topic
this is simple demo for publishing message to a specific topic only.
Once the message is published, the connection to rabbitmq is closed.

Enhancements: creation of a generic class independent of
RPC client, an abstract factory, which will return appropriate
RPC client class for the provided parameters in the abstract factory interface
"""
import pika
from .exceptions import MissingParameter


class Producer(object):

    def __init__(self):
        self.conn = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
        self.channel = self.conn.channel()
        self.exchange = None

    def connect(self, exchange=None, durable=True):
        if not exchange or not exchange:
            raise MissingParameter('missing parameter `exchange` during function call')

        self.channel.exchange_declare(exchange=exchange, exchange_type='topic', durable=durable)
        self.exchange = exchange

    def publish(self, topic=None, message=''):
        if not topic or not topic:
            raise MissingParameter('missing parameter `topic` during function call')
        self.channel.basic_publish(exchange=self.exchange, routing_key=topic, body=message)
        return 'Sent %r:%r" ' % (topic, message)

    def close(self):
        self.conn.close()

