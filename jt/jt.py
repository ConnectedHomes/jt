import click
import sys
import json
import requests
from .jsontree import *
from crayons import *


CONTEXT_SETTINGS = dict(help_option_names=[])

@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument('filename', required=False)
@click.option('-u', help='Perform GET request on the specified JSON endpoint and print JSON tree.')
@click.option('-h', is_flag=True, help='Show help.')
def run(filename, u, h):
    j = J()
    if (u and filename) or (not u and not filename) or h:
        help_string = "\n\
    {}, a command line utility for printing JSON tree structure.\n\n\
    Usage:\n\n\
        Read JSON from file:\n\
        $ {}\n\n\
        Read JSON from GET request:\n\
        $ {}\n\n\
        Show help:\n\
        $ {}\n\n\
    Output legend:\n\n\
    {} describes string data.\n\
    {} describes array data.\n\
    {} describes dict data.\n\n\
        ".format(
            white('jt'),
            white('jt ') + red('FILENAME'),
            white('jt -u ') + red('URL'),
            white('jt -h '),
            white('\'') + str('node_0') + white('\''),
            green('[') + str('node_0') + green(']'),
            yellow('{') + str('node_0') + yellow('}'),
        )
        print(help_string)

        sys.exit(0)

    if u:
        j.tree(json.loads(requests.get(u).text))

    if filename:
        d = ''.join([i for i in open(filename, 'r')])
        j.tree([(json.loads(d))])


if __name__ == '__main__':
    run()
