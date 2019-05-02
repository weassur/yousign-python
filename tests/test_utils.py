import pytest
from unittest.mock import Mock, patch

from yousign.utils import (
    check_status,
    BadRequestError,
    UnauthorizedError,
    NotAllowedError,
    NotFoundError,
)


class TestUtils:
    def test_check_status(self):
        response = Mock()
        response.status_code = 200
        assert check_status(response)
        response.status_code = 201
        assert check_status(response)
        response.status_code = 204
        assert check_status(response)

        with pytest.raises(BadRequestError):
            response.status_code = 400
            check_status(response)

        with pytest.raises(UnauthorizedError):
            response.status_code = 401
            check_status(response)

        with pytest.raises(NotAllowedError):
            response.status_code = 405
            check_status(response)

        with pytest.raises(NotFoundError):
            response.status_code = 404
            check_status(response)
