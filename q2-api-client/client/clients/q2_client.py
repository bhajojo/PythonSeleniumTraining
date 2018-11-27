from client.clients.rest_client import RestClient
from client.endpoints.mobile_ws_endpoints import LoginEndPoint
from client.utils.url import URL

class Q2Client(RestClient):

    def __init__(self, **kwargs):
        super.__init__(**kwargs)
        self._connect_timeout = kwargs.get('connect_timeout', 60)
        self._read_timeout = kwargs.get('read_timeout',120)
        self._scheme= kwargs.get('scheme',"https")
        self._base_path= kwargs.get('base_path')
        self._headers['Accept'] = "application/json"
        self._headers['q2token'] = kwargs.get('q2token') if kwargs.get('q2token') is not None else self.get_Q2Token()

    def _get_q2_token(self):
        credentials ={'userId': self._username, 'password': self._password}
        endpoint = LoginEndPoint.LOGON.User.value
        response = self._post(url=self._build_url(endpoint), json= credentials)
        response.raise_for_status()
        return response.headers.get('q2token')

    def _build_url(self, endpoint ="/"):
        path = endpoint if self._base_path is None else "".join(self._base_path,endpoint)
        url = URL(scheme=self._scheme, host=self._host, port= self._port,path=path)
        return url.build


