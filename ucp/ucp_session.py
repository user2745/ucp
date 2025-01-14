from datetime import datetime

class UCPSession:
    def __init__(self):
        self.sessions = {}

    def add_client(self, client_id):
        self.sessions[client_id] = {"last_active": datetime.now()}
        print(f"Client {client_id} added")

    def update_client_activity(self, client_id):
        if client_id in self.sessions:
            self.sessions[client_id]["last_active"] = datetime.now()
            print(f"Client {client_id} updated activity")
        else:
            self.add_client(client_id)

    def get_active_clients(self):
        return {k: v for k, v in self.sessions.items() if self.is_active(v)}

    def is_active(self, client_data, timeout=60):
        return (datetime.now() - client_data["last_active"]).seconds < timeout
