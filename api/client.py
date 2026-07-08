import requests

class XUIClient:
    def __init__(self, server):
        self.server = server
        self.session = requests.Session()

    @property
    def base_url(self):
        return self.server.api_url.rstrip("/")
    
    def login(self):
        response = self.session.post(f"{self.base_url}/login", data={"username":self.server.api_login, "password":self.server.api_password,}, timeout=15, verify=False,)
        if response.status_code != 200:
          return False
        try:
            data = response.json()
        except Exception:
            return False
        return data.get("success", False)

    def get_server_status(self):
        response = self.session.get(f"{self.base_url}/panel/api/server/status", timeout=15, verify=False,)
        return response.json()
        
        
    def  get_inbounds(self):
        response = self.session.get(f"{self.base_url}/panel/api/inbounds/get/", timeout=15, verify=False)        
        return response.json()
    
    def delete_inbounds(self, inbounds_id):
        response = self.session.post(f"{self.base_url}/panel/api/inbounds/del/{inbounds_id}", timeout=15, verify=False,)
        return response.json()
        
    def add_client(self, inbound_id, client_data):
        payload = {"id": inbound_id, "settings": client_data,}
        response = self.session.post(f"{self.base_url}/panel/api/inbound/addClient", json=payload, timeout=15, verify=False)
        return response.json()