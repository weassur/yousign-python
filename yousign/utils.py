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

