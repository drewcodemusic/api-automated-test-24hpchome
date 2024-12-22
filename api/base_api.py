from config.config import TestConfig

class BaseAPI:
    def __init__(self, api_client, base_url):
        self.api_client = api_client
        self.base_url = base_url
    
    def _get(self, endpoint):
        response = self.api_client.get(
            f"{self.base_url}{endpoint}",
            timeout=TestConfig.TIMEOUT
        )
        response.raise_for_status()
        return response.json()