"""Password"""

import requests
import hashlib

from pwnedapi.__version__ import __version__
from pwnedapi.exceptions.PasswordException import PasswordException
from pwnedapi.exceptions.RequestException import RequestException
from requests.exceptions import Timeout


class Password:
    """This class represents a password.
    It does all the work of talking to the
    Pwned Passwords API to find out if the
    password has been pwned."""

    # Endpoint for the HIBP API v2
    API_URL = "https://api.pwnedpasswords.com/range/"

    # Currently the API desires first 5 characters
    HASH_PREFIX_LENGTH = 5

    # Hashed need to be encoded before sending
    HASH_ENCODING = "utf-8"

    USER_AGENT = "pwnedapi v{}".format(__version__)

    DEFAULT_REQUEST_HEADERS = {"User-Agent": USER_AGENT}

    def __init__(self, password: str, request_headers: dict = {}, read_timeout: int = 10) -> None:

        if not isinstance(password, str):
            raise PasswordException("Password must be a string.")

        self.password = password
        self.DEFAULT_REQUEST_HEADERS.update(request_headers)
        self.request_headers = self.DEFAULT_REQUEST_HEADERS
        self.read_timeout = read_timeout

        self.hashed_password = self.hash_password()
        self.pwned_count = 0

    def get_value(self) -> str:
        return self.password

    def hash_password(self) -> str:
        h = hashlib.sha1()
        h.update(self.password.encode(self.HASH_ENCODING))

        return h.hexdigest().upper()

    def is_pwned(self) -> bool:
        self.pwned_count = self.fetch_pwned_count()

        return self.pwned_count > 0

    def fetch_pwned_count(self) -> int:
        hash_list = self.make_request().text.split("\r\n")

        for hash in hash_list:
            if hash.startswith(self.hashed_password_suffix()):
                return int(hash.split(":")[1])

        return 0

    def make_request(self) -> requests.Response:
        url = self.API_URL + self.hashed_password_prefix()

        try:
            response = requests.get(
                url, headers=self.request_headers, timeout=self.read_timeout)
        except Timeout:
            raise RequestException("API request timed out.")

        if response.status_code != 200 or not response.content:
            raise RequestException("API request failed.")

        return response

    def hashed_password_prefix(self) -> str:
        return self.hashed_password[:self.HASH_PREFIX_LENGTH]

    def hashed_password_suffix(self) -> str:
        return self.hashed_password[self.HASH_PREFIX_LENGTH:]
