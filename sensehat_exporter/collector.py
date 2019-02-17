from prometheus_client.core import GaugeMetricFamily


class CustomCollector(object):
    def __init__(self, client):
        self.client = client

    def collect(self):
        humidity = self.client.get_humidity()
        if 0 <= humidity <= 100:
            g = GaugeMetricFamily("sensehat_humidity",
                                  "Relative humidity %",
                                  labels=["sensor"])
            g.add_metric(["HTS221"], humidity)
            yield g

        g = GaugeMetricFamily("sensehat_temperature",
                              "Temperature in degrees Celsius",
                              labels=["sensor"])
        temp = self.client.get_temperature_from_humidity()
        if -100 <= temp <= 100:
            g.add_metric(["HTS221"], temp)
        temp = self.client.get_temperature_from_pressure()
        if -100 <= temp <= 100:
            g.add_metric(["LPS25H"], temp)
        yield g

        pressure = self.client.get_pressure()
        if 500 <= pressure <= 1500:
            g = GaugeMetricFamily("sensehat_pressure", "Pressure in hPa",
                                  labels=["sensor"])
            g.add_metric(["LPS25H"], pressure)
            yield g
