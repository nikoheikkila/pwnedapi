import re
from tempfile import NamedTemporaryFile
from unittest import mock

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


@mock.patch('pwnedapi.__main__.Password')
def test_check_safe_password(m_password):
    m_pass_inst = mock.Mock()
    m_pass_inst.pwned_count = 0
    m_password.return_value = m_pass_inst

    runner = CliRunner()
    result = runner.invoke(main.check, input='Peter\nPeter')
    assert result.exit_code == 0
    pattern = \
        r'Password: \nRepeat for confirmation: \n' \
        r'Your password has been pwned \d+ times.\n' \
        r'Your password is safe.'
    assert re.match(pattern, result.output)


def test_scan(tempfile):
    runner = CliRunner()
    result = runner.invoke(main.scan, [tempfile])
    assert result.exit_code == 0
    pattern = r'Password,Leak Count\n{}\n\n'.format(
        r'\n'.join([r'{},\d+'.format(x) for x in PASSWORDS]))
    assert re.match(pattern, result.output)
