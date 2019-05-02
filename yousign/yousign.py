STAGING_URL = "https://staging-api.yousign.com"
PRODUCTION_URL = "https://api.yousign.com"


class YouSign:
    def __init__(self, api_key, production=False):
        self.api_key = api_key
        self.api_url = PRODUCTION_URL if production else STAGING_URL
