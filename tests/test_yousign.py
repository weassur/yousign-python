import pytest
from unittest.mock import Mock, patch
from yousign.yousign import YouSign, STAGING_URL, PRODUCTION_URL, CONTENT_TYPE
from tests.mocks import (
    users_response,
    create_procedure_response,
    create_file_response,
    create_member_response,
)


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

    def test_get_headers(self):
        api_key = "fake-api-key"
        instance = YouSign(api_key=api_key)
        headers = instance._get_headers()
        assert headers["Content-Type"] == CONTENT_TYPE
        assert headers["Authorization"] == "Bearer fake-api-key"

    def test_get_users(self):
        api_key = "fake-api-key"
        instance = YouSign(api_key=api_key)
        with patch("requests.get") as mock_get:
            mock_get.return_value = Mock(ok=True)
            mock_get.return_value.status_code = 200
            mock_get.return_value.json.return_value = users_response

            ret = instance.users()
            mock_get.assert_called_once_with(
                STAGING_URL + "/users",
                headers={
                    "Content-Type": CONTENT_TYPE,
                    "Authorization": "Bearer {api_key}".format(api_key=api_key),
                },
            )
        assert ret == users_response

    def test_create_procedure(self):
        api_key = "fake-api-key"
        instance = YouSign(api_key=api_key)
        with patch("requests.post") as mock_post:
            mock_post.return_value = Mock(ok=True)
            mock_post.return_value.status_code = 201
            mock_post.return_value.json.return_value = create_procedure_response
            name = "Procedure Name"
            description = "procedure description"

            ret = instance.create_procedure(name=name, description=description)
            mock_post.assert_called_once_with(
                STAGING_URL + "/procedures",
                headers={
                    "Content-Type": CONTENT_TYPE,
                    "Authorization": "Bearer {api_key}".format(api_key=api_key),
                },
                params={"name": name, "description": description, "start": False},
            )
            assert ret == create_procedure_response

    def test_add_file(self):
        api_key = "fake-api-key"
        instance = YouSign(api_key=api_key)
        with patch("requests.post") as mock_post:
            mock_post.return_value = Mock(ok=True)
            mock_post.return_value.status_code = 201
            mock_post.return_value.json.return_value = create_file_response
            name = "FileName.pdf"
            description = "File description"
            content = ""
            procedure_id = "/procedures/XXXX"

            ret = instance.add_file(
                procedure_id=procedure_id,
                name=name,
                description=description,
                content=content,
            )
            mock_post.assert_called_once_with(
                STAGING_URL + "/files",
                headers={
                    "Content-Type": CONTENT_TYPE,
                    "Authorization": "Bearer {api_key}".format(api_key=api_key),
                },
                params={
                    "name": name,
                    "description": description,
                    "content": content,
                    "procedure": procedure_id,
                },
            )
            assert ret == create_file_response

    def test_add_member(self):
        api_key = "fake-api-key"
        instance = YouSign(api_key=api_key)
        first_name = "First Name"
        last_name = "Last Name"
        email = "email@domain.com"
        phone_number = "+334226633"
        procedure_id = "/procedures/XXXX"
        with patch("requests.post") as mock_post:
            mock_post.return_value = Mock(ok=True)
            mock_post.return_value.status_code = 200
            mock_post.return_value.json.return_value = create_file_response

            ret = instance.add_member(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone_number=phone_number,
                procedure_id=procedure_id,
            )
            mock_post.assert_called_once_with(
                STAGING_URL + "/members",
                headers={
                    "Content-Type": CONTENT_TYPE,
                    "Authorization": "Bearer {api_key}".format(api_key=api_key),
                },
                params={
                    "firstname": first_name,
                    "lastname": last_name,
                    "email": email,
                    "phone": phone_number,
                    "procedure": procedure_id,
                },
            )
            assert ret == create_file_response

        with patch("requests.post") as mock_post:
            mock_post.return_value = Mock(ok=True)
            phone_number = "0344223322"
            with pytest.raises(Exception):
                ret = instance.add_member(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    phone_number=phone_number,
                    procedure_id=procedure_id,
                )
            email = "fakeemail"
            with pytest.raises(Exception):
                ret = instance.add_member(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    phone_number=phone_number,
                    procedure_id=procedure_id,
                )
            assert not mock_post.called
