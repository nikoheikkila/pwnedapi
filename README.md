# `pwnedapi` (Have I Been Pwned)

[![Build Status](https://travis-ci.org/nikoheikkila/pwnedapi.svg?branch=master)](https://travis-ci.org/nikoheikkila/pwnedapi)

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

You can also scan a file of passwords, and export results in any format supported by the `tablib` library.

```python
>>> from pwnedapi import Scanner
>>> scanner = Scanner()
>>> scanner.scan("passwords.txt")
>>> scanner.export_as("leaked.json")
>>> open("leaked.json").read()
'[{"Password": "dog", "Leak Count": 28348}, {"Password": "cat", "Leak Count": 26354}, {"Password": "somepass", "Leak Count": 657}]'
```

## Support

This is my first official Python package so if something is off feel free to send a PR. :fist:

# TODO

- [ ] Add password change form validators to Django and Flask

[hibp]: https://haveibeenpwned.com/API/v2#SearchingPwnedPasswordsByRange
[pwned]: https://philnash.github.io/pwned/
[tablib]: http://docs.python-tablib.org/en/latest/