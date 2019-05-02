import requests

from yousign.utils import check_status

STAGING_URL = "https://staging-api.yousign.com"
PRODUCTION_URL = "https://api.yousign.com"

CONTENT_TYPE = "application/json"


class YouSign:
    def __init__(self, api_key, production=False):
        self.api_key = api_key
        self.api_url = PRODUCTION_URL if production else STAGING_URL

    def _get_headers(self):
        return {
            "Content-Type": CONTENT_TYPE,
            "Authorization": "Bearer {api_key}".format(api_key=self.api_key),
        }

    def users(self):
        url = self.api_url + "/users"
        response = requests.get(url, headers=self._get_headers())
        check_status(response)
        data = response.json()
        return data

    def create_procedure(self, name, description, *args, **kwargs):
        url = self.api_url + "/procedures"
        params = {"name": name, "description": description, "start": False}
        response = requests.post(url, headers=self._get_headers(), params=params)
        check_status(response)
        data = response.json()
        return data
