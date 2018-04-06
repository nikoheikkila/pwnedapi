# -*- coding: utf-8 -*-

import random
import string
import pytest

from Password import Password

class TestPassword():

    def generate_random_password(self, length: int) -> str:
        return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(length))

    @pytest.fixture(autouse=True)
    def setup(self):
        self.passwords = {
            "weak": "dog",
            "strong": self.generate_random_password(64)
        }

    def test_pwned_password(self):
        """Test against weak password
        which should be pwned at least once"""
        password = Password(self.passwords["weak"])
        assert password.is_pwned()
        assert password.pwned_count > 0

    def test_non_pwned_password(self):
        password = Password(self.passwords["strong"])
        assert not password.is_pwned()
        assert password.pwned_count == 0
