from __future__ import absolute_import, print_function
import argparse
import time

from prometheus_client import start_http_server
from prometheus_client.core import REGISTRY
from sense_hat import SenseHat

from .collector import CustomCollector


REGISTRY.register(CustomCollector(SenseHat()))

parser = argparse.ArgumentParser(
    description='Sense HAT exporter for Prometheus')
parser.add_argument('--host', default='0.0.0.0',
                    help='host (default: 0.0.0.0)')
parser.add_argument('--port', type=int, default=9542,
                    help='port number (default: 9542)')
args = parser.parse_args()


host = args.host
port = args.port
print("Listening on %s:%d" % (host, port))
start_http_server(port, host)
while True:
    time.sleep(1)
