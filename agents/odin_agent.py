import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ucl_core import UCLClient
import json

def handle_command(command):
    print(f"Executing command on Odin: {command}")
    try:
        data = json.loads(command)
        action = data.get("action")
        if action == "log_status":
            # Simulate logging system status
            status_info = {
                "device": "Odin",
                "status": "All systems operational"
            }
            return {"status": "success", "details": status_info}
        elif action == "fetch_logs":
            # Simulate fetching logs
            return {"status": "success", "details": "Log data not implemented yet"}
        else:
            return {"status": "error", "details": "Unknown command"}
    except json.JSONDecodeError:
        return {"status": "error", "details": "Invalid JSON format"}

if __name__ == "__main__":
    odin = UCLClient(device_id="odin", broker_address="100.72.222.91")

    def on_message(client, userdata, message):
        print(f"Message received on {message.topic}: {message.payload.decode()}")
        response = handle_command(message.payload.decode())
        odin.publish("ucl/status/odin", response)

    odin.subscribe("ucl/commands/odin")
    odin.client.on_message = on_message
    odin.loop_forever()
