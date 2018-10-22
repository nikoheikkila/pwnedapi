# -*- coding: utf-8 -*-

import random
import string
import pytest
import requests
import responses
from unittest.mock import patch

from pwnedapi.Password import Password
from pwnedapi.exceptions.PasswordException import PasswordException
from pwnedapi.exceptions.RequestException import RequestException


class TestPassword():

    BAD_URL = "https://api.pwnedpasswords.com/nope/"

    def generate_random_password(self, length: int) -> str:
        return ''.join(
            random.choice(
                string.ascii_lowercase + string.digits
            ) for _ in range(length)
        )

    @pytest.fixture(autouse=True)
    def setup(self):
        self.passwords = {
            "integers": 123456,
            "weak": "dog",
            "strong": self.generate_random_password(64)
        }

    def test_non_str_password(self):
        """Test against a non-string password."""

        with pytest.raises(
            PasswordException,
            message="Password must be a string."
        ):
            Password(self.passwords["integers"])

    @responses.activate
    def test_pwned_password(self):
        """Test against weak password
        which should be pwned at least once"""

        password = Password(self.passwords["weak"])
        url = Password.API_URL + password.hashed_password_prefix()
        # define a match in the API response
        responses.add(
            responses.GET,
            url,
            body="{}:1\r\n".format(password.hashed_password_suffix()),
            status=200,
        )
        assert password.is_pwned()
        assert password.pwned_count > 0

    @responses.activate
    def test_non_pwned_password(self):
        """Test random strong password."""

        password = Password(self.passwords["strong"])
        url = Password.API_URL + password.hashed_password_prefix()
        # no matches in API response
        responses.add(
            responses.GET,
            url,
            body="some_other_hash:0\r\n",
            status=200,
        )
        assert not password.is_pwned()
        assert password.pwned_count == 0

    @patch('requests.get')
    def test_request_timeout(self, mock_get):
        """Test that request can fail when timed out."""

        mock_get.side_effect = requests.exceptions.Timeout
        with pytest.raises(RequestException, message="API request timed out."):
            password = Password(self.passwords["weak"])
            password.is_pwned()

    @responses.activate
    def test_invalid_api_url(self):
        """Test that request can fail with invalid API URL."""

        responses.add(
            responses.GET,
            self.BAD_URL,
            status=404,
        )
        with pytest.raises(RequestException, message="API request failed."):
            password = Password(self.passwords["weak"])
            password.API_URL = self.BAD_URL
            password.is_pwned()

    @responses.activate
    def test_invalid_api_response(self):
        """HIBP API returns something unexpected."""

        password = Password(self.passwords["weak"])
        url = Password.API_URL + password.hashed_password_prefix()
        # an empty body with an OK status
        responses.add(
            responses.GET,
            url,
            body="",
            status=200,
        )
        # an unexpected status with a match in the body, just to test status
        responses.add(
            responses.GET,
            url,
            body="{}:1\r\n".format(password.hashed_password_suffix()),
            status=500,
        )
        with pytest.raises(RequestException, message="API request failed."):
            password.is_pwned()
        with pytest.raises(RequestException, message="API request failed."):
            password.is_pwned()
