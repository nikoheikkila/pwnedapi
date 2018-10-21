import re
from tempfile import NamedTemporaryFile

import pytest
from click.testing import CliRunner

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
    pattern = \
        r'Password: \nRepeat for confirmation: \n' \
        r'Your password has been pwned \d+ times.\n'
    assert re.match(pattern, result.output)


def test_scan(tempfile):
    runner = CliRunner()
    result = runner.invoke(main.scan, [tempfile])
    assert result.exit_code == 0
    pattern = r'Password,Leak Count\n{}\n\n'.format(
        r'\n'.join([r'{},\d+'.format(x) for x in PASSWORDS]))
    assert re.match(pattern, result.output)
