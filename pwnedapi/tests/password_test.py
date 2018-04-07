# -*- coding: utf-8 -*-

import random
import string
import pytest

from Password import Password
from exceptions.PasswordException import PasswordException
from exceptions.RequestException import RequestException


class TestPassword():

    BAD_URL = "https://api.pwnedpasswords.com/nope/"

    def generate_random_password(self, length: int) -> str:
        return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(length))

    @pytest.fixture(autouse=True)
    def setup(self):
        self.passwords = {
            "integers": 123456,
            "weak": "dog",
            "strong": self.generate_random_password(64)
        }

    def test_non_str_password(self):
        """Test against a non-string password."""

        with pytest.raises(PasswordException, message="Password must be a string."):
            password = Password(self.passwords["integers"])

    def test_pwned_password(self):
        """Test against weak password
        which should be pwned at least once"""

        password = Password(self.passwords["weak"])
        assert password.is_pwned()
        assert password.pwned_count > 0

    def test_non_pwned_password(self):
        """Test random strong password."""

        password = Password(self.passwords["strong"])
        assert not password.is_pwned()
        assert password.pwned_count == 0

    def test_request_timeout(self):
        """Test that request can fail with
        very little timeout value."""

        with pytest.raises(RequestException, message="API request timed out."):
            password = Password(self.passwords["weak"], read_timeout=0.01)
            password.is_pwned()

    def test_invalid_api_url(self):
        """Test that request can fail with invalid API URL."""

        with pytest.raises(RequestException, message="API request failed."):
            password = Password(self.passwords["weak"])
            password.API_URL = self.BAD_URL
            password.is_pwned()
