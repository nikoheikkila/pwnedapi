import pytest
import json
import os

from tempfile import NamedTemporaryFile
from pwnedapi.utils import Scanner


PASSWORDS = [
    "dog",
    "cat",
    "cuckoo"
]


@pytest.fixture()
def tempfile():
    tmpfile = NamedTemporaryFile(delete=False)
    tmpfile.write(str.encode("\n".join(PASSWORDS)))
    return tmpfile.name


@pytest.fixture()
def emptyfile():
    return NamedTemporaryFile().name


def test_export_as(tempfile):
    scanner = Scanner()
    results = scanner.scan(tempfile).data

    assert results.height == 3
    assert results.width == 2

    export_file = "test.json"

    scanner.export_as(export_file)
    data = json.load(open(export_file))

    for d in data:
        assert d[scanner.get_headers()[0]] in PASSWORDS
        assert d[scanner.get_headers()[1]] > 0

    os.remove(export_file)


def test_scan_empty_file(emptyfile):
    scanner = Scanner()

    with pytest.raises(OSError, message="File {} is empty.".format(emptyfile)):
        scanner.scan(emptyfile)


def test_scan_non_existent_file():
    data_file = "foo"
    scanner = Scanner()

    if os.path.isfile(data_file):
        os.remove(data_file)

    with pytest.raises(FileNotFoundError):
        scanner.scan(data_file)
