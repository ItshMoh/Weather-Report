import paho.mqtt.client as mqtt

import json

mqttBroker = "test.mosquitto.org"

class WeatherAlertsServiceClient:

  def __init__(self):
              self.client = mqtt.Client()
              self.client.connect(mqttBroker)

  def sendRainAlert(self, id, location, extra):
            topic = "weather/rain"
            message = {
              "alertId": id,
              "location": location,
              "intensity": extra,
            }
            result = self.client.publish(topic, json.dumps(message))
            rc, mid = result
            if rc == mqtt.MQTT_ERR_SUCCESS:
                print(f"RainAlert Message with id {mid} published successfully.")
            else:
                print(f"Failed to publish message with id {mid}. Error code: {rc}")
          
  def sendSnowAlert(self, id, location, extra):
            topic = "weather/snow"
            message = {
              "alertId": id,
              "location": location,
              "intensity": extra,
            }
            result = self.client.publish(topic, json.dumps(message))
            rc, mid = result
            if rc == mqtt.MQTT_ERR_SUCCESS:
                print(f"SnowAlert Message with id {mid} published successfully.")
            else:
                print(f"Failed to publish message with id {mid}. Error code: {rc}")
          
  def sendHeatwaveAlert(self, id, location, extra):
            topic = "weather/heatwave"
            message = {
              "alertId": id,
              "location": location,
              "temperature": extra,
            }
            result = self.client.publish(topic, json.dumps(message))
            rc, mid = result
            if rc == mqtt.MQTT_ERR_SUCCESS:
                print(f"HeatwaveAlert Message with id {mid} published successfully.")
            else:
                print(f"Failed to publish message with id {mid}. Error code: {rc}")
          
  def sendNormalAlert(self, id, location, extra):
            topic = "weather/normal"
            message = {
              "alertId": id,
              "location": location,
              "temperature": extra,
            }
            result = self.client.publish(topic, json.dumps(message))
            rc, mid = result
            if rc == mqtt.MQTT_ERR_SUCCESS:
                print(f"NormalAlert Message with id {mid} published successfully.")
            else:
                print(f"Failed to publish message with id {mid}. Error code: {rc}")
          

