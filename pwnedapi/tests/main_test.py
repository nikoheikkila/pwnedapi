from tempfile import NamedTemporaryFile
import re

from click.testing import CliRunner
import pytest

from pwnedapi import __main__ as main

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


def test_check():
    runner = CliRunner()
    result = runner.invoke(main.check, input='Peter\nPeter')
    assert result.exit_code == 0
    patt = \
        r'Password: \nRepeat for confirmation: \n' \
        r'Your password has been pwned \d+ times.\n'
    assert re.match(patt, result.output)


def test_scan(tempfile):
    runner = CliRunner()
    result = runner.invoke(main.scan, [tempfile])
    assert result.exit_code == 0
    #  assert result.output == 'Hello Peter!\n'
    patt = r'Password,Leak Count\ndog,\d+\ncat,\d+\ncuckoo,\d+\n\n'
    assert re.match(patt, result.output)
