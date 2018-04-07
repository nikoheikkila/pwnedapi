# `pwnedapi` (Have I Been Pwned)

A small utility class to leverage Troy Hunt's [_Have I Been Pwned API v2_](https://haveibeenpwned.com/API/v2#SearchingPwnedPasswordsByRange) and the _k-Anonymity_ model. Inspired by Phil Nash's Ruby gem [_pwned_](https://philnash.github.io/pwned/).

## Installation

```bash
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

## Support

This is my first official Python package so if something is off feel free to send a PR. :fist:

# TODO

- [ ] Add password change form validators to Django and Flask