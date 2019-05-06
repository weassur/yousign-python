import pytest
from unittest.mock import Mock, patch
from yousign.yousign import (
    YouSign,
    STAGING_URL,
    PRODUCTION_URL,
    CONTENT_TYPE,
    DEFAULT_CONFIG,
)
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

        webhook_url = "https://webhook.com"
        instance = YouSign(
            api_key=api_key, production=False, webhook_url=webhook_url
        )
        default_config = DEFAULT_CONFIG
        default_config["webhook"] = (
            {
                "member.finished": [
                    {
                        "url": webhook_url,
                        "method": "GET",
                        "headers": {"X-Custom-Header": "Test value"},
                    }
                ]
            },
        )
        assert instance.default_config == default_config

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
        name = "Procedure Name"
        description = "procedure description"
        with patch("requests.post") as mock_post:
            mock_post.return_value = Mock(ok=True)
            mock_post.return_value.status_code = 201
            mock_post.return_value.json.return_value = create_procedure_response

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

        with patch("requests.post") as mock_post:
            mock_post.return_value = Mock(ok=True)
            mock_post.return_value.status_code = 201
            mock_post.return_value.json.return_value = create_procedure_response
            members = [
                {
                    "firstname": "John",
                    "lastname": "Doe",
                    "email": "john.doe@yousign.com",
                    "phone": "+336XXXXXXXX",
                    "fileObjects": [
                        {
                            "position": "0, 0, 100, 200",
                            "page": 2,
                            "file": "/files/XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
                        }
                    ],
                },
                {
                    "user": "/users/XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
                    "fileObjects": [
                        {
                            "page": 0,
                            "file": "/files/XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
                        }
                    ],
                },
            ]
            config = {
                "email": {
                    "member.started": [
                        {
                            "subject": "You have a new procedure !",
                            "message": 'Hello <tag data-tag-type="string" data-tag-name="recipient.firstname"></tag> <tag data-tag-type="string" data-tag-name="recipient.lastname"></tag> ! <br><br> You have ben added to a procedure, please access it here : <tag data-tag-type="button" data-tag-name="url" data-tag-title="Access to documents">Access to documents</tag>',
                            "to": ["@member"],
                        }
                    ],
                    "procedure.started": [
                        {
                            "subject": "John, created a procedure your API have.",
                            "message": "The content of this email is totally awesome.",
                            "to": [
                                "luke.skywalker@yousign.com",
                                "princess.leila@yousign.com",
                            ],
                        }
                    ],
                }
            }

            ret = instance.create_procedure(
                name=name,
                description=description,
                members=members,
                config=config,
                start=True,
            )
            mock_post.assert_called_once_with(
                STAGING_URL + "/procedures",
                headers={
                    "Content-Type": CONTENT_TYPE,
                    "Authorization": "Bearer {api_key}".format(api_key=api_key),
                },
                params={
                    "name": name,
                    "description": description,
                    "start": True,
                    "members": members,
                    "config": config,
                },
            )
            assert ret == create_procedure_response

    def test_start_procedure(self):
        api_key = "fake-api-key"
        instance = YouSign(api_key=api_key)
        procedure_id = "/procedures/procedure-id"
        with patch("requests.put") as mock_put:
            mock_put.return_value = Mock(ok=True)
            mock_put.return_value.status_code = 200
            mock_put.return_value.json.return_value = create_procedure_response
            ret = instance.start_procedure(procedure_id=procedure_id)
            mock_put.assert_called_once_with(
                STAGING_URL + procedure_id,
                headers={
                    "Content-Type": CONTENT_TYPE,
                    "Authorization": "Bearer {api_key}".format(api_key=api_key),
                },
                params={"start": True},
            )
            assert ret == create_procedure_response

    def test_add_file(self):
        api_key = "fake-api-key"
        instance = YouSign(api_key=api_key)
        name = "FileName.pdf"
        description = "File description"
        content = ""
        with patch("requests.post") as mock_post:
            mock_post.return_value = Mock(ok=True)
            mock_post.return_value.status_code = 201
            mock_post.return_value.json.return_value = create_file_response
            procedure_id = "/procedures/XXXX"

            ret = instance.add_file(
                name=name,
                content=content,
                procedure_id=procedure_id,
                description=description,
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

        with patch("requests.post") as mock_post:
            mock_post.return_value = Mock(ok=True)
            mock_post.return_value.status_code = 201
            mock_post.return_value.json.return_value = create_file_response

            ret = instance.add_file(name=name, content=content, description=description)
            mock_post.assert_called_once_with(
                STAGING_URL + "/files",
                headers={
                    "Content-Type": CONTENT_TYPE,
                    "Authorization": "Bearer {api_key}".format(api_key=api_key),
                },
                params={"name": name, "description": description, "content": content},
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
