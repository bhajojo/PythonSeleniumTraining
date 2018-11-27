from client.clients.central.central_client import CentralClient
from client.clients.file_map.file_map_client import FileMapClient
from client.clients.hq.hq_client import HQClient
from client.clients.q2_config.q2_config_client import Q2ConfigClient
from client.clients.refresh_cache.refresh_cache_client import RefreshCacheClient
from client.clients.sdk.sdk_client import SDKClient
from client.clients.v2.v2_client import V2Client

class Q2APIClient:

    def __init__(self, **kwargs):
        self._q2_config = Q2ConfigClient(**kwargs)
        kwargs['q2token'] = self._q2_config.get_header('q2token')
        self._central = CentralClient(**kwargs)
        self._file_map = FileMapClient(**kwargs)
        self._hq = HQClient(**kwargs)
        self._refresh_cache = RefreshCacheClient(**kwargs)
        self._v2 = V2Client(**kwargs)

        @property
        def q2_config(self):
            return self._q2_config

        @property
        def central(self):
            return self._central

        @property
        def file_map(self):
            return self._file_map

        @property
        def hq(self):
            return self._hq

        @property
        def refresh_cache(self):
            return self._refresh_cache

        @property
        def sdk(self):
            return self._sdk

        @property
        def v2(self):
            return self._v2



