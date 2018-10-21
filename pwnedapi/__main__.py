import click
from typing import Any

from . import Password, Scanner

@click.group()
def cli() -> None:
    pass


@cli.command()
@click.password_option(help="Password, which will be checked.")
def check(password: Any) -> None:
    "Checks a single password if it has been pwned."
    password = Password(password)
    if password.is_pwned():
        print("Your password has been pwned {} times.".format(password.pwned_count))


@cli.command()
@click.argument('INPUT_FILE', type=click.File('rb'))
@click.option('--output-format', help='Output data format.', default='csv')
def scan(input_file: Any, output_format: str='csv') -> None:
    "Scan a file for pwned passwords."
    scanner = Scanner()
    scanner.scan(input_file.name)
    print(scanner.export(output_format))
