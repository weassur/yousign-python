users_response = [
    {
        "id": "/users/XXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
        "firstname": "John",
        "lastname": "Doe",
        "email": "john.doe@yousign.fr",
        "title": "Developer",
        "phone": "+33612345678",
        "status": "activated",
        "company": "/companies/XXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
        "permission": "ROLE_ADMIN",
        "group": {
            "id": "/user_groups/XXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
            "name": "Administrateur",
            "permissions": [
                "procedure_write",
                "procedure_template_write",
                "procedure_create_from_template",
                "contact",
                "sign",
                "company",
                "user",
                "api_key",
                "procedure_custom_field",
                "signature_ui",
                "certificate",
                "archive",
            ],
        },
        "createdAt": "2018-12-01T09:42:25+01:00",
        "updatedAt": "2018-12-01T09:42:25+01:00",
        "deleted": False,
        "deletedAt": None,
        "config": [],
        "inweboUserRequest": None,
        "samlNameId": None,
        "defaultSignImage": None,
        "notifications": {"procedure": True},
        "fastSign": False,
        "fullName": "John Doe",
    }
]

create_procedure_response = {
    "id": "/procedures/9d1ede2b-5687-4440-bdc8-dd0bc64f668c",
    "name": "string",
    "description": "string",
    "createdAt": "2019-05-02T14:36:11.993Z",
    "updatedAt": "2019-05-02T14:36:11.993Z",
    "expiresAt": "2019-05-02T14:36:11.993Z",
    "status": "draft",
    "creator": "/users/9d1ede2b-5687-4440-bdc8-dd0bc64f668c",
    "creatorFirstName": "string",
    "creatorLastName": "string",
    "company": "/companies/9d1ede2b-5687-4440-bdc8-dd0bc64f668c",
    "template": True,
    "ordered": True,
    "parent": "/procedures/9d1ede2b-5687-4440-bdc8-dd0bc64f668c",
    "metadata": {"key_1": "value_1", "key_2": "value_2"},
    "config": {
        "email": {
            "procedure.started": [
                {
                    "to": '["@members.auto","@creator","user@gmail.com","..."]',
                    "subject": "string",
                    "message": "string",
                    "fromName": "string",
                }
            ],
            "procedure.finished": [
                {
                    "to": '["@members.auto","@creator","user@gmail.com","..."]',
                    "subject": "string",
                    "message": "string",
                    "fromName": "string",
                }
            ],
            "procedure.refused": [
                {
                    "to": '["@members.auto","@creator","user@gmail.com","..."]',
                    "subject": "string",
                    "message": "string",
                    "fromName": "string",
                }
            ],
            "procedure.expired": [
                {
                    "to": '["@members.auto","@creator","user@gmail.com","..."]',
                    "subject": "string",
                    "message": "string",
                    "fromName": "string",
                }
            ],
            "procedure.deleted": [
                {
                    "to": '["@members.auto","@creator","user@gmail.com","..."]',
                    "subject": "string",
                    "message": "string",
                    "fromName": "string",
                }
            ],
            "member.started": [
                {
                    "to": '["@members.auto","@creator","user@gmail.com","..."]',
                    "subject": "string",
                    "message": "string",
                    "fromName": "string",
                }
            ],
            "member.finished": [
                {
                    "to": '["@members.auto","@creator","user@gmail.com","..."]',
                    "subject": "string",
                    "message": "string",
                    "fromName": "string",
                }
            ],
            "comment.created": [
                {
                    "to": '["@members.auto","@creator","user@gmail.com","..."]',
                    "subject": "string",
                    "message": "string",
                    "fromName": "string",
                }
            ],
        },
        "reminders": [
            {
                "interval": 0,
                "limit": 0,
                "config": {
                    "email": {
                        "reminder.executed": [
                            {
                                "to": '["@members.auto","@creator","user@gmail.com","..."]',
                                "subject": "string",
                                "message": "string",
                                "fromName": "string",
                            }
                        ]
                    }
                },
            }
        ],
        "webhook": {
            "procedure.started": [
                {
                    "url": "string",
                    "method": "GET",
                    "headers": {"X-Yousign-Custom-Header": "Test value"},
                }
            ],
            "procedure.finished": [
                {
                    "url": "string",
                    "method": "GET",
                    "headers": {"X-Yousign-Custom-Header": "Test value"},
                }
            ],
            "procedure.refused": [
                {
                    "url": "string",
                    "method": "GET",
                    "headers": {"X-Yousign-Custom-Header": "Test value"},
                }
            ],
            "procedure.expired": [
                {
                    "url": "string",
                    "method": "GET",
                    "headers": {"X-Yousign-Custom-Header": "Test value"},
                }
            ],
            "procedure.deleted": [
                {
                    "url": "string",
                    "method": "GET",
                    "headers": {"X-Yousign-Custom-Header": "Test value"},
                }
            ],
            "member.started": [
                {
                    "url": "string",
                    "method": "GET",
                    "headers": {"X-Yousign-Custom-Header": "Test value"},
                }
            ],
            "member.finished": [
                {
                    "url": "string",
                    "method": "GET",
                    "headers": {"X-Yousign-Custom-Header": "Test value"},
                }
            ],
            "comment.created": [
                {
                    "url": "string",
                    "method": "GET",
                    "headers": {"X-Yousign-Custom-Header": "Test value"},
                }
            ],
        },
    },
    "members": [
        {
            "id": "/members/9d1ede2b-5687-4440-bdc8-dd0bc64f668c",
            "user": "/users/9d1ede2b-5687-4440-bdc8-dd0bc64f668c",
            "type": "signer",
            "firstname": "string",
            "lastname": "string",
            "email": "string",
            "phone": "string",
            "position": 0,
            "createdAt": "2019-05-02T14:36:11.994Z",
            "updatedAt": "2019-05-02T14:36:11.994Z",
            "status": "pending",
            "fileObjects": [
                {
                    "id": "/file_objects/9d1ede2b-5687-4440-bdc8-dd0bc64f668c",
                    "file": {
                        "id": "/files/9d1ede2b-5687-4440-bdc8-dd0bc64f668c",
                        "name": "string",
                        "type": "signable",
                        "contentType": "application/pdf",
                        "description": "string",
                        "createdAt": "string",
                        "updatedAt": "string",
                        "metadata": {"key_1": "value_1", "key_2": "value_2"},
                        "company": "/companies/9d1ede2b-5687-4440-bdc8-dd0bc64f668c",
                        "creator": "/users/9d1ede2b-5687-4440-bdc8-dd0bc64f668c",
                        "sha256": "23203f9264161714cdb8d2f474b9b641e6a735f8cea4098c40a3cab8743bd749",
                    },
                    "page": 0,
                    "position": "400,700,500,800",
                    "fieldName": "string",
                    "mention": "Read and approuved",
                    "mention2 (internal)": "string",
                    "createdAt": "2019-05-02T14:36:11.994Z",
                    "updatedAt": "2019-05-02T14:36:11.994Z",
                    "executedAt": "2019-05-02T14:36:11.994Z",
                    "reason": "string",
                }
            ],
            "comment": "string",
            "procedure": "string",
            "operationLevel": "none",
            "operationCustomModes": ["sms"],
            "modeSmsConfiguration": {
                "content": "Hello, your code for signature is {{code}}."
            },
        }
    ],
    "files": [
        {
            "id": "/files/9d1ede2b-5687-4440-bdc8-dd0bc64f668c",
            "name": "string",
            "type": "signable",
            "contentType": "application/pdf",
            "description": "string",
            "createdAt": "string",
            "updatedAt": "string",
            "metadata": {"key_1": "value_1", "key_2": "value_2"},
            "company": "/companies/9d1ede2b-5687-4440-bdc8-dd0bc64f668c",
            "creator": "/users/9d1ede2b-5687-4440-bdc8-dd0bc64f668c",
            "sha256": "23203f9264161714cdb8d2f474b9b641e6a735f8cea4098c40a3cab8743bd749",
        }
    ],
    "relatedFilesEnable": True,
    "archive": False,
}

create_file_response = {
    "id": "/files/9d1ede2b-5687-4440-bdc8-dd0bc64f668c",
    "name": "string",
    "type": "signable",
    "contentType": "application/pdf",
    "description": "string",
    "createdAt": "string",
    "updatedAt": "string",
    "metadata": {
        "key_1": "value_1",
        "key_2": "value_2"
    },
    "company": "/companies/9d1ede2b-5687-4440-bdc8-dd0bc64f668c",
    "creator": "/users/9d1ede2b-5687-4440-bdc8-dd0bc64f668c",
    "sha256": "23203f9264161714cdb8d2f474b9b641e6a735f8cea4098c40a3cab8743bd749"
}
