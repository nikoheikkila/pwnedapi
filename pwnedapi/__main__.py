from . import Password, Scanner

import click

@click.group()
def cli():
    pass


@cli.command()
@click.password_option(help="Password, which will be checked.")
def check(password):
    "Checks a single password if it has been pwned."
    password = Password(password)
    if password.is_pwned():
        print(f"Your password has been pwned {password.pwned_count} times.")


@cli.command()
@click.argument('INPUT_FILE', type=click.File('rb'))
@click.option('--output-format', help='Output data format.', default='csv')
def scan(input_file, output_format='csv'):
    "Scan a file for pwned passwords."
    scanner = Scanner()
    scanner.scan(input_file.name)
    print(scanner.export(output_format))
