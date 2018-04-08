import tablib

from pwnedapi.Password import Password
from time import sleep


class Scanner():
    """Class for scanning password lists for pwnage."""

    COLUMNS = ["Password", "Leak Count"]
    BINARY_FORMATS = ["csv", "dbf", "ods", "xls", "xlsx"]

    def __init__(self, extra_cols: list = []) -> None:
        self.data = tablib.Dataset()
        self.COLUMNS.extend(extra_cols)
        self.data.headers = self.COLUMNS

    def get_headers(self):
        return self.data.headers

    def export(self, format: str = "csv") -> tablib.Dataset:
        """Formats data to another."""

        return self.data.export(format)

    def export_as(self, output_file: str) -> None:
        """Exports data to a file."""

        format = output_file.split(".")[-1]
        data = self.export(format)
        mode = "wb" if format in self.BINARY_FORMATS else "w"

        with open(output_file, mode) as o:
            o.write(data)

    def scan(self, filename: str, sleep_time: float = 0.2):
        """Scans password data from file.
        WARNING: Depending on the size of the file
        this might take a *long* time depending on the
        HIBP API performance. Parameter sleep_time is provided for
        avoiding throttled API responses."""

        lines = [line.rstrip("\n") for line in open(filename)]

        for line in lines:
            password = Password(line)
            if password.is_pwned():
                self.data.append([password.get_value(), password.pwned_count])
            sleep(sleep_time)

        return self
