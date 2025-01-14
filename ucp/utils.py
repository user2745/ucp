BROKER_ADDRESS = "localhost"
BROKER_PORT = 1883

# Default Topics
TOPICS = {
    "command": "nova/{client_id}/command",
    "response": "nova/{client_id}/response",
    "broadcast": "nova/broadcast",
    "keepalive": "nova/{client_id}/keepalive",
}
