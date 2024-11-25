import paho.mqtt.client as mqtt
import json

class UCLClient:
    def __init__(self, device_id, broker_address="localhost", port=1883):
        self.device_id = device_id
        self.client = mqtt.Client(client_id=device_id)
        self.client.on_connect = self._on_connect
        self.client.on_message = self._on_message
        self.client.connect(broker_address, port, 60)

    def _on_connect(self, client, userdata, flags, rc):
        print(f"{self.device_id} connected with result code {rc}")

    def _on_message(self, client, userdata, msg):
        print(f"Message received on {msg.topic}: {msg.payload.decode()}")

    def subscribe(self, topic):
        self.client.subscribe(topic)
        print(f"{self.device_id} subscribed to {topic}")

    def publish(self, topic, message):
        if isinstance(message, dict):
            message = json.dumps(message)
        self.client.publish(topic, message)
        print(f"{self.device_id} published to {topic}: {message}")

    def loop_forever(self):
        self.client.loop_forever()
