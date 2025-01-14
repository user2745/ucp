class UCPHandler:
    def __init__(self, device_id):
        self.device_id = device_id

    def handle_command(self, command):
        try:
            data = json.loads(command)
            action = data.get("action")
            if action == "ping":
                return {"status": "success", "response": "pong"}
            elif action == "log_status":
                return {"status": "success", "details": f"Device {self.device_id} is operational"}
            elif action == "fetch_data":
                return {"status": "success", "data": "Here is some mock data"}
            else:
                return {"status": "error", "details": "Unknown command"}
        except json.JSONDecodeError:
            return {"status": "error", "details": "Invalid JSON format"}
