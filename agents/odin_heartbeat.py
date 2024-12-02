import paho.mqtt.client as mqtt
import time
import os

# Configuration
BROKER = "100.72.222.91"  # Replace with your broker's address
DEVICE_ID = os.uname().nodename.lower()  # Use device hostname for unique ID
TOPIC = f"devices/{DEVICE_ID}/status"

# Define callbacks
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"[{DEVICE_ID}] Connected to MQTT broker at {BROKER}")
    else:
        print(f"[{DEVICE_ID}] Connection failed with code {rc}")

def on_publish(client, userdata, mid):
    print(f"[{DEVICE_ID}] Published message with mid: {mid}")

def on_message(client, userdata, msg):
    print(f"[{DEVICE_ID}] Received command: {msg.payload.decode()}")
    # Execute the command or simulate execution
    if msg.payload.decode() == "ping":
        print(f"[{DEVICE_ID}] Responding to ping")
        client.publish(f"devices/{DEVICE_ID}/response", "pong")

# Initialize MQTT client
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, client_id=DEVICE_ID)
client.on_connect = on_connect
client.on_publish = on_publish
client.on_message = on_message
client.subscribe(f"devices/{DEVICE_ID}/commands")

# Connect to the broker
client.connect(BROKER, 1883, 60)

# Start the network loop in a non-blocking thread
client.loop_start()

try:
    # Periodically send heartbeats
    while True:
        heartbeat_message = {
            "device_id": DEVICE_ID,
            "status": "online",
            "timestamp": time.time()
        }
        result = client.publish(TOPIC, str(heartbeat_message))
        print(f"[{DEVICE_ID}] Sent heartbeat: {heartbeat_message}")
        time.sleep(10)
except KeyboardInterrupt:
    print(f"[{DEVICE_ID}] Disconnecting...")
    client.disconnect()
    client.loop_stop()

