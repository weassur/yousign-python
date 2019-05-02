import pytest
from yousign.yousign import YouSign, STAGING_URL, PRODUCTION_URL


class TestYouSign:
    def test_constructor(self):
        api_key = "fake-api-key"
        instance = YouSign(api_key=api_key)
        assert instance.api_key == api_key
        assert instance.api_url == STAGING_URL

        instance = YouSign(api_key=api_key, production=True)
        assert instance.api_key == api_key
        assert instance.api_url == PRODUCTION_URL

        with pytest.raises(TypeError):
            # fmt: off
            instance = YouSign()  #pylint: disable=E1120
            # fmt: on

        with pytest.raises(TypeError):
            # fmt: off
            instance = YouSign(foo="bar")  #pylint: disable=E1120,E1123
            # fmt: on
