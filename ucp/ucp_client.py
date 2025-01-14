import paho.mqtt.client as mqtt
import json
import threading
import time

class UCPClient:
    def __init__(self, device_id, broker_address="localhost", port=1883, keepalive=60):
        self.device_id = device_id
        self.client = mqtt.Client(client_id=device_id)
        self.broker_address = broker_address
        self.port = port
        self.keepalive = keepalive

        # MQTT Callbacks
        self.client.on_connect = self._on_connect
        self.client.on_message = self._on_message

    def _on_connect(self, client, userdata, flags, rc):
        print(f"[{self.device_id}] Connected with result code {rc}")

    def _on_message(self, client, userdata, msg):
        print(f"[{self.device_id}] Received on {msg.topic}: {msg.payload.decode()}")

    def connect(self):
        self.client.connect(self.broker_address, self.port, self.keepalive)
        self.client.loop_start()

    def subscribe(self, topic):
        self.client.subscribe(topic)
        print(f"[{self.device_id}] Subscribed to {topic}")

    def publish(self, topic, message, qos=1):
        if isinstance(message, dict):
            message = json.dumps(message)
        self.client.publish(topic, message, qos)
        print(f"[{self.device_id}] Published to {topic}: {message}")

    def start_heartbeat(self, interval=10):
        def heartbeat():
            while True:
                self.publish(f"ucl/keepalive/{self.device_id}", {"status": "online"})
                time.sleep(interval)
        threading.Thread(target=heartbeat, daemon=True).start()

    def set_message_handler(self, handler):
        self.client.on_message = lambda client, userdata, msg: handler(msg.topic, msg.payload.decode())

    def disconnect(self):
        self.client.loop_stop()
        self.client.disconnect()
        print(f"[{self.device_id}] Disconnected")

if __name__ == "__main__":
    client = UCPClient(device_id="client1", broker_address="localhost", port=1883)
    client.connect()
    client.subscribe("ucl/commands/client1")
    client.publish("ucl/commands/client1", {"action": "ping"})
    client.start_heartbeat()
    try:
        while True:
            pass  # Keep client running
    except KeyboardInterrupt:
        client.disconnect()
