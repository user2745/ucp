import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ucl_core import UCLClient
import time

def handle_command(command):
    print(f"Executing command: {command}")
    # Simulate executing a command
    time.sleep(1)
    print("Command executed successfully.")
    return {"status": "success", "details": f"Executed: {command}"}

if __name__ == "__main__":
    fezzan = UCLClient(device_id="fezzan")

    # Subscribe to its command topic
    fezzan.subscribe("ucl/commands/fezzan")

    def on_message(client, userdata, message):
        payload = message.payload.decode()
        print(f"Command received: {payload}")
        response = handle_command(payload)
        fezzan.publish("ucl/status/fezzan", response)

    fezzan.client.on_message = on_message

    # Start listening
    fezzan.loop_forever()
