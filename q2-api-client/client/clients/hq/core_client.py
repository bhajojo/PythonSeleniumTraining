from client.clients.q2_client import Q2Client
from client.clients.hq_endpoints import CoreEndpoints

class CoreClient(Q2Client):

    def get_bai_codes(self):
        endpoint = CoreEndpoints.BAI.CODES.value
        return self._get(url=self._build_url(endpoint))

    def get_bai_code(self):
        endpoint = CoreEndpoints.BAI.CODES.value
        return self._get(url=self._build_url(endpoint))

    def get_countries(self):
        endpoint = CoreEndpoints.COUNTRY.value
        return self._get(url=self._build_url(endpoint))

    def get_dispute_forms(self, language_short_name):
        endpoint = CoreEndpoints.DISPUTE_FORM_SHORT_NAME.value.format(languageShortName=language_short_name)
        return self._get(url=self._build_url(endpoint))

    def get_goals_category_mapping(self, mapping_id):
        endpoint = CoreEndpoints.GOALS_CATEGORY_MAPPING.value.format(id=mapping_id)
        return self._get(url=self._build_url(endpoint))

    

