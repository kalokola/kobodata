import requests
import json

class KoboData:
    def __init__(self,account_domain, data_uuid, token):
        self.account_domain = account_domain
        self.data_uuid = data_uuid
        self.token     = token
    
    @property
    def kobo_data(self):
        url = 'https://{}/api/v2/assets/{}/data/?format=json'.format(self.account_domain, self.data_uuid)
        headers = {'Authorization': 'Token {}'.format(self.token)}
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            return json.loads(r.content)
        return {"error":"Incorrect Authy Details"}

    
    
    @property
    def counts(self):
        data = KoboData(self.account_domain, self.data_uuid, self.token).kobo_data
        return data['count']

    @property
    def get_data(self):
        data = KoboData(self.account_domain, self.data_uuid, self.token).kobo_data
        return data['results']

__doc__ = """

For Documentation check out https://github.com/kalokola/kobodata/blob/main/README.md
"""