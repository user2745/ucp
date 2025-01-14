from .ucp_client import UCPClient
from .ucp_handler import UCPHandler

class UCPServer:
    def __init__(self, broker_address="localhost", port=1883):
        self.client = UCPClient(device_id="NovaBackend", broker_address=broker_address, port=port)
        self.handler = UCPHandler(device_id="NovaBackend")

    def start(self):
        self.client.connect()
        self.client.subscribe("ucl/commands/#")
        self.client.set_message_handler(self._on_message)
        print("[Server] Running...")
        try:
            while True:
                pass  # Keep server running
        except KeyboardInterrupt:
            self.stop()

    def _on_message(self, topic, message):
        print(f"[Server] Command received on {topic}: {message}")
        response = self.handler.handle_command(message)
        response_topic = topic.replace("commands", "status")
        self.client.publish(response_topic, response)

    def broadcast(self, message):
        self.client.publish("ucl/broadcast", json.dumps(message))
        print(f"[Server] Broadcast message: {message}")

    def stop(self):
        self.client.disconnect()
        print("[Server] Stopped")

if __name__ == "__main__":
    server = UCPServer(broker_address="localhost", port=1883)
    server.start()
