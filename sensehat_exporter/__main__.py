from __future__ import absolute_import, print_function
import time

from prometheus_client import start_http_server
from prometheus_client.core import REGISTRY
from sense_hat import SenseHat

from .collector import CustomCollector


REGISTRY.register(CustomCollector(SenseHat()))

host = "0.0.0.0"
port = 9542
print("Listening on %s:%d" % (host, port))
start_http_server(port, host)
while True:
    time.sleep(1)
