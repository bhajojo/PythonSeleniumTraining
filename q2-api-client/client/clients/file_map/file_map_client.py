from client.clients.q2_client import Q2Client
from client.endpoints.file_map_endpoints import FileMapEndPoint

class FileMapClient(Q2Client):

    def get_file_map_asset(self,asset,**query):
        endpoint = FileMapEndPoint.FILE_MAP_ASSET.value.format(asset=asset)
        query_parameters = self._copy_query_parameters()
        query_parameters.update(**query)
        return self._get(url=self._build_url(endpoint), query_parameters=query_parameters)

