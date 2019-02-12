from wsgiref.simple_server import make_server, WSGIRequestHandler

from prometheus_client import Gauge, make_wsgi_app
from prometheus_client.core import GaugeMetricFamily, REGISTRY
from sense_hat import SenseHat


class CustomCollector(object):
    def __init__(self, client):
        self.client = client

    def collect(self):
        humidity = self.client.get_humidity()
        if 0 <= humidity <= 100:
            g = GaugeMetricFamily("sensehat_humidity", "Relative humidity %", labels=["sensor"])
            g.add_metric(["HTS221"], humidity)
            yield g

        g = GaugeMetricFamily("sensehat_temperature", "Temperature in degrees Celsius", labels=["sensor"])
        temp = self.client.get_temperature_from_humidity()
        if -100 <= temp <= 100:
            g.add_metric(["HTS221"], temp)
        temp = self.client.get_temperature_from_pressure()
        if -100 <= temp <= 100:
            g.add_metric(["LPS25H"], temp)
        yield g

        pressure = self.client.get_pressure()
        if 500 <= pressure <= 1500:
            g = GaugeMetricFamily("sensehat_pressure", "Pressure in hPa", labels=["sensor"])
            g.add_metric(["LPS25H"], pressure)
            yield g


class NoLoggingWSGIRequestHandler(WSGIRequestHandler):
    def log_message(self, format, *args):
        pass


if __name__ == '__main__':
    REGISTRY.register(CustomCollector(SenseHat()))

    host = "0.0.0.0"
    port = 9542
    print("Listening on %s:%d" % (host, port))
    app = make_wsgi_app()
    httpd = make_server(host, port, app,  handler_class=NoLoggingWSGIRequestHandler)
    httpd.serve_forever()
