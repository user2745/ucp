# Universal Communication Protocol (UCP)

The **Universal Communication Protocol (UCP)** is a lightweight, scalable communication framework built on MQTT. It enables real-time, bidirectional communication between devices, making it ideal for IoT, distributed systems, and collaborative device networks.

## Architecture
1. **MQTT Broker (Fezzan)**:
   - Central hub for message routing using a publish/subscribe model.
2. **Device Agents**:
   - Each device runs a Python agent to:
     - Subscribe to commands (`ucl/commands/<device_id>`).
     - Publish status updates (`ucl/status/<device_id>`).
3. **Connected Devices**:
   - Example devices include:
     - **Odin**: MacBook Air for command processing.
     - **Neue-Sanssouci**: Orange Pi for edge computing.
     - **Hildegard**: Raspberry Pi for monitoring.

## Features
- **Lightweight**: Minimal resource usage with MQTT.
- **Real-Time**: Instant messaging and responses.
- **Scalable**: Easily add devices and expand functionality.
- **Modular**: Independent device operation through dynamic topics.

## Quick Start
### 1. Install the MQTT Broker
On Fezzan:
```bash
sudo apt install mosquitto mosquitto-clients
sudo systemctl enable mosquitto
sudo systemctl start mosquitto
```

### 2. Deploy the UCP Agents
Clone the repository and install dependencies:
```bash
git clone <repository_url>
cd ucp
pip install -r requirements.txt
```

Run the server or a client:
```bash
# Start the server
python main.py server

# Start a client
python main.py client <device_id>
```

### 3. Test Communication
Publish a test command:
```bash
mosquitto_pub -h <broker_ip> -t "ucl/commands/<device_id>" -m '{"action": "ping"}'
```

Subscribe to responses:
```bash
mosquitto_sub -h <broker_ip> -t "ucl/status/<device_id>"
```

## Topics
- **Commands**: `ucl/commands/<device_id>` — Devices receive instructions.
- **Status**: `ucl/status/<device_id>` — Devices send status and responses.
- **Broadcast**: `ucl/broadcast` — System-wide updates.
