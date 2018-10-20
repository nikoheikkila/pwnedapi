# `pwnedapi` (Have I Been Pwned)

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/5c1b1ede06564c7b8f857874aaeb4d13)](https://app.codacy.com/app/nikoheikkila/pwnedapi?utm_source=github.com&utm_medium=referral&utm_content=nikoheikkila/pwnedapi&utm_campaign=Badge_Grade_Settings)
[![Build Status](https://travis-ci.org/nikoheikkila/pwnedapi.svg?branch=master)](https://travis-ci.org/nikoheikkila/pwnedapi)
[![codecov](https://codecov.io/gh/nikoheikkila/pwnedapi/branch/master/graph/badge.svg)](https://codecov.io/gh/nikoheikkila/pwnedapi)

A small utility class to leverage Troy Hunt's [_Have I Been Pwned API v2_][hibp] and the _k-Anonymity_ model. Inspired by Phil Nash's Ruby gem [_pwned_][pwned].

## Installation

```bash
# From repository
pipenv install pwnedapi

# Locally after cloning
python setup.py install
```

## Usage

In its simplest form you'll only need to use two methods. Will probably add more if and when the API grows.

```python
>>> from pwnedapi import Password
>>> password = Password("mysupersecretpassword")
>>>
>>> if password.is_pwned():
...     print(f"Your password has been pwned {password.pwned_count} times.")
...
Your password has been pwned 2 times.
>>>
```

on cli:

```bash
$ pwned check
Password: ****
Repeat for confirmation: ****
Your password has been pwned 2 times.
```

You can also scan a file of passwords, and export results in any format supported by the [`tablib`][tablib] library.

```python
>>> from pwnedapi import Scanner
>>> scanner = Scanner()
>>> scanner.scan("passwords.txt")
>>> scanner.export_as("leaked.json")
>>> open("leaked.json").read()
'[{"Password": "dog", "Leak Count": 28348}, {"Password": "cat", "Leak Count": 26354}, {"Password": "somepass", "Leak Count": 657}]'
```

on cli:

```bash
$ pwned scan passwords.txt
Password,Leak Count
dog,30267
cat,27732
cuckoo,2717
```

## Contributing

Check the source code and issues from this repository, and should anything interesting pop out feel free to open a pull request. Before your changes will be merged make sure that Travis CI pipeline is green and code coverage is on acceptable level. GitHub takes care of these eventually but to save time always consider running the tests locally before pushing.

[hibp]: https://haveibeenpwned.com/API/v2#SearchingPwnedPasswordsByRange
[pwned]: https://philnash.github.io/pwned/
[tablib]: http://docs.python-tablib.org/en/latest/
