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
    tmpfile = NamedTemporaryFile()
    tmpfile.write(str.encode(""))
    return tmpfile.name


def test_export_as(tempfile):
    scanner = Scanner()
    results = scanner.scan(tempfile)

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
    with pytest.raises(IOError, message=f"File {emptyfile} is empty."):
        Scanner().scan(emptyfile)
