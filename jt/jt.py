import sys
import json
import click
import requests
from crayons import *
from .jsontree import *


CONTEXT_SETTINGS = dict(help_option_names=[])

@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument('filename', required=False)
@click.option('-u', help='Perform HTTP GET request on the specified endpoint and click.echo JSON response as tree.')
@click.option('-s', is_flag=True, help='Read JSON from stream.')
@click.option('-h', is_flag=True, help='Show help.')
def run(filename, u, s, h):
    j = JSONTree()
    if (u and filename) or (not u and not filename and not s) or h:
        help_string = "\n\
    {}\n\
    {}, a command line utility for visualising JSON schemas as text trees.\n\n\
    {}:\n\
        $ {}\n\n\
    {}:\n\
        {} : Show this message and exit.\n\
        {} : Read {} from {}.\n\
        {} : Read {} from {}.\n\n\
    {}:\n\
        Read {} from {}:\n\
        $ {}\n\n\
        Read {} from {}:\n\
        $ {}\n\n\
        Read {} from {}:\n\
        $ {}\n\n\
        Show help:\n\
        $ {}\n\n\
    {}:\n\
        {} - describes {} data.\n\
        {} - describes {} data.\n\
        {} - describes {} data.\n\n\
        ".format(
            yellow("\
  ║\n\
      ╠") + white ("══╦══\n") +
yellow("    ══╝") + white("  ║\n\
         ║\n"),
            white('jt'),
            yellow('Usage'),
            white('jt ') + green('FILENAME ') + white('[-h] [-s] [-u ') + blue('URL') + white(']'),
            yellow('Options'),
            white('-h'),
            white('-s'),
            yellow('JSON'),
            white('stream'),
            white('-u'),
            yellow('JSON'),
            blue('HTTP GET request'),
            yellow('Examples'),
            yellow('JSON'),
            blue('HTTP GET request'),
            white('jt -u ') + blue('https://api.github.com/users/para0rmal/repos'),
            yellow('JSON'),
            green('file'),
            white('jt ') + green('FILENAME'),
            yellow('JSON'),
            white('stream'),
            'echo ' + white('\'{"0": {"00": [{"000": "", "001": [""]}]}, "1": {"10": [""]}}\' ') 
                + '| ' + white('jt -s'),
            white('jt -h '),
            yellow('Legend'),
            white('\'') + str('node_0') + white('\''),
            white('string'),
            cyan('[') + str('node_0') + cyan(']'),
            cyan('array'),
            yellow('{') + str('node_0') + yellow('}'),
            yellow('dictionary'),
        )
        click.echo(help_string)

        sys.exit(0)

    if u:
        r = None

        try:
            r = requests.get(u)

        except:
            if not r:
                click.echo(red('Error: ') + 'Request to {} failed. '.format(cyan(u)))
                sys.exit()

            else:
                click.echo(red('Error: ') + 'Request to {} failed with status code {}.'.format(cyan(u), red(r.status_code)))
                sys.exit()


        try:
            click.echo(j.tree(json.loads(r.text)))

        except:
            click.echo(red('Error: ') + 'Expecting {} format.'.format(yellow('JSON')))
            sys.exit()

    if s:
        try:
            input_buffer = json.loads(''.join([l for l in sys.stdin]))
            click.echo(j.tree([input_buffer]))

        except:
            click.echo(red('Error: ') + 'Expecting {} format.'.format(yellow('JSON')))
            sys.exit()

    if filename:
        try:
            d = ''.join([i for i in open(filename, 'r')])

        except:
            click.echo(red('Error: ') + 'File {} not found.'.format(green(filename)))
            sys.exit()

        try:
            click.echo(j.tree([(json.loads(d))]))

        except:
            click.echo(red('Error: ') + 'Expecting {} format.'.format(yellow('JSON')))
            sys.exit()


