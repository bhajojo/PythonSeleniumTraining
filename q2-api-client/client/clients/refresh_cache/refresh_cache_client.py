from client.clients.q2_client import Q2Client
from client.clients.endpoints.refresh_cache_endpoints import RefreshCacheEndPoints


class RefreshCacheClient(Q2Client):

    def refresh_cache(self):
        endpoint = RefreshCacheClient.REFRESH_CACHE.value
        return self._post(url=self._build_url(endpoint))


