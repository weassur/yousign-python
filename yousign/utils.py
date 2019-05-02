import re

email_regex = re.compile(
    r"(^[-!#$%&'*+/=?^_`{}|~0-9A-Z]+(\.[-!#$%&'*+/=?^_`{}|~0-9A-Z]+)*"  # dot-atom
    r'|^"([\001-\010\013\014\016-\037!#-\[\]-\177]|\\[\001-011\013\014\016-\177])*"'  # quoted-string
    r")@(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?$",
    re.IGNORECASE,
)  # domain


def check_email(email):
    return email_regex.search(email) is not None


class BadRequestError(Exception):
    pass


class UnauthorizedError(Exception):
    pass


class NotFoundError(Exception):
    pass


class NotAllowedError(Exception):
    pass


VALID_STATUS_CODE = set([200, 201, 204])
ERROR_STATUS_CODE = {
    400: BadRequestError,
    401: UnauthorizedError,
    404: NotFoundError,
    405: NotAllowedError,
}


def check_status(response):
    if response.status_code in VALID_STATUS_CODE:
        return True

    exception = ERROR_STATUS_CODE.get(
        response.status_code, Exception("unknown exception")
    )
    raise exception

