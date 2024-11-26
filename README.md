# Universal Communication Layer (UCL)

The Universal Communication Layer (UCL) is a lightweight, scalable communication system that enables seamless interaction between multiple devices using MQTT. It powers the connected infrastructure of L'Atelier, facilitating real-time messaging and device collaboration.

## Architecture
The UCL consists of:
1. **Mosquitto MQTT Broker (Fezzan)**:
   - Acts as the central hub for all communication.
   - Handles the publish/subscribe model for connected devices.

2. **Device Agents**:
   - Each device has a custom Python agent that:
     - Subscribes to its specific `ucl/commands/<device_id>` topic for incoming commands.
     - Publishes status updates to `ucl/status/<device_id>`.

3. **Connected Devices**:
   - **Odin**: MacBook Air running the agent to process commands and respond.
   - **Neue-Sanssouci**: Orange Pi for edge computing tasks.
   - **Hildegard**: Raspberry Pi 3 for lightweight computation and monitoring.

## Features
- **Lightweight Communication**: Built on MQTT, ensuring minimal resource usage.
- **Modularity**: Each device operates independently while communicating through the UCL.
- **Scalability**: Easily add new devices and topics to expand functionality.
- **Real-Time Messaging**: Supports instant message delivery and response.

## Setup
### 1. Install Mosquitto (Broker)
On Fezzan:
```
sudo apt install mosquitto mosquitto-clients
sudo systemctl enable mosquitto
sudo systemctl start mosquitto
```

Ensure the broker listens on port `1883` with the following configuration:
```
listener 1883
allow_anonymous true
```

### 2. Deploy Device Agents
Clone this repository on each device and install the dependencies:
```
git clone <repository_url>
cd ucl
pip install -r requirements.txt
```

Run the agent:
```
python3 agents/<device_name>_agent.py
```

### 3. Test the System
Publish a test message to the broker:
```
mosquitto_pub -h <broker_ip> -t "ucl/commands/<device_name>" -m '{"action": "test_command"}'
```

Subscribe to the status topic to verify the response:
```
mosquitto_sub -h <broker_ip> -t "ucl/status/<device_name>"
```

## Topics
- **Commands**: `ucl/commands/<device_id>` — Devices subscribe here to receive instructions.
- **Status**: `ucl/status/<device_id>` — Devices publish their status and results here.

## Future Plans
- Add authentication for secure communication.
- Implement logging and monitoring dashboard.
- Expand to new devices and advanced functionalities.
