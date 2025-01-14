# Broker Configuration
BROKER_ADDRESS = "100.72.222.91"  # Replace with your MQTT broker's address
BROKER_PORT = 1883               # Default port for MQTT
KEEPALIVE = 60                   # Keepalive interval (seconds)

# Quality of Service Levels (QoS)
# 0 = At most once (no delivery guarantee)
# 1 = At least once (delivery guaranteed, may duplicate)
# 2 = Exactly once (delivery guaranteed, no duplicates)
DEFAULT_QOS = 1

# Topic Structure
# You can use `{device_id}` placeholders to dynamically generate topics for devices
DEFAULT_TOPICS = {
    "command": "ucl/commands/{device_id}",    # Commands sent to a specific device
    "status": "ucl/status/{device_id}",      # Status updates from a specific device
    "response": "ucl/response/{device_id}",  # Device-specific responses
    "broadcast": "ucl/broadcast",           # Broadcast messages to all devices
    "keepalive": "ucl/keepalive/{device_id}" # Keepalive heartbeats
}

# Heartbeat Configuration
HEARTBEAT_INTERVAL = 10  # Interval in seconds to send keepalive messages

# Logging Configuration
ENABLE_LOGGING = True
LOG_FILE = "ucp.log"

# Debug Mode
DEBUG = True
