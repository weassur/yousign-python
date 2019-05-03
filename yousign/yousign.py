import requests
import phonenumbers

from yousign.utils import check_status, check_email

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

    ## content should be a base64 encoded string, without the header
    ## https://staging-dev.yousign.com/#/procedureCreate?id=add-files-to-my-procedure
    ## use
    ## import base64
    ## with open(filename, 'rb') as upload_file:
    ##     encoded_string = base64.b64encode(f.read())
    def add_file(
        self, name, content, procedure_id=None, description=None, *args, **kwargs
    ):
        url = self.api_url + "/files"
        params = {"name": name, "content": content}
        if procedure_id:
            params["procedure"] = procedure_id
        if description:
            params["description"] = description
        response = requests.post(url, headers=self._get_headers(), params=params)
        check_status(response)
        data = response.json()
        return data

    def add_member(self, procedure_id, first_name, last_name, email, phone_number):
        assert check_email(email)
        phone = phonenumbers.parse(phone_number)
        phone = phonenumbers.format_number(phone, phonenumbers.PhoneNumberFormat.E164)
        url = self.api_url + "/members"
        params = {
            "firstname": first_name,
            "lastname": last_name,
            "email": email,
            "phone": phone,
            "procedure": procedure_id,
        }
        response = requests.post(url, headers=self._get_headers(), params=params)
        check_status(response)
        data = response.json()
        return data

    def add_signature_image(
        self,
        file_id,
        member_id,
        mention="Read and approved",
        mention2="Signature",
        page=0,
        position=None,
    ):
        url = self.api_url + "/file_objects"
        params = {
            "file": file_id,
            "member": member_id,
            "mention": mention,
            "mention2": mention2,
            "page": page,
        }
        if position and page > 0:
            params["position"] = position
        response = requests.post(url, headers=self._get_headers(), params=params)
        check_status(response)
        data = response.json()
        return data
