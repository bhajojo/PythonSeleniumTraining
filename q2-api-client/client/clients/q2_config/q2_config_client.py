from client.clients.q2_client import Q2Client
from client.clients.q2_config_endpoints import Q2ConfigEndpoints

class Q2ConfigClient(Q2Client):

        def get_q2_config(self):
            endpoint= Q2ConfigEndpoints.Q2.CONFIG.value
            print (endpoint)
            return self._get(url=self._build_url(endpoint))