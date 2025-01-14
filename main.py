from ucp.ucp_server import UCPServer
from ucp.ucp_client import UCPClient
import sys
import threading

def run_server():
    server = UCPServer(broker_address="localhost", port=1883)
    server.start()

def run_client(device_id):
    client = UCPClient(device_id=device_id, broker_address="localhost", port=1883)
    client.connect()
    client.subscribe(f"ucl/commands/{device_id}")
    client.start_heartbeat()

    # Custom message handler
    def handle_message(topic, message):
        print(f"[{device_id}] Received message: {message}")
        if message == '{"action": "ping"}':
            client.publish(f"ucl/status/{device_id}", {"status": "success", "response": "pong"})

    client.set_message_handler(handle_message)
    try:
        while True:
            pass  # Keep client running
    except KeyboardInterrupt:
        client.disconnect()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py [server|client] [device_id]")
        sys.exit(1)

    mode = sys.argv[1]
    if mode == "server":
        run_server()
    elif mode == "client":
        if len(sys.argv) < 3:
            print("Usage: python main.py client [device_id]")
            sys.exit(1)
        device_id = sys.argv[2]
        run_client(device_id)
    else:
        print("Unknown mode. Use 'server' or 'client'.")
