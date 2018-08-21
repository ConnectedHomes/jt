import sys
import json
import click
import requests
from crayons import *
from .jsontree import *


CONTEXT_SETTINGS = dict(help_option_names=[])

@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument('filename', required=False)
@click.option('-u', help='Perform HTTP GET request on the specified endpoint and print JSON response as tree.')
@click.option('-s', is_flag=True, help='Read JSON from STDIN.')
@click.option('-h', is_flag=True, help='Show help.')
def run(filename, u, s, h):
    j = JSONTree()
    if (u and filename) or (not u and not filename and not s) or h:
        help_string = "\n\
    {}\n\
    {}, a command line utility for visualising JSON schemas as ASCII trees.\n\n\
    {}:\n\
        $ {}\n\n\
    {}:\n\
        {} : Show this message and exit.\n\
        {} : Read JSON from {}.\n\
        {} : Read JSON from {}.\n\n\
    {}:\n\
        Read JSON from {}:\n\
        $ {}\n\n\
        Read JSON from {}:\n\
        $ {}\n\n\
        Read JSON from {}:\n\
        $ {}\n\n\
        Show help:\n\
        $ {}\n\n\
    {}:\n\
        {} - describes {} data.\n\
        {} - describes {} data.\n\
        {} - describes {} data.\n\
        ".format(
            yellow("\
  ║\n\
      ╠") + white ("══╦══\n") +
yellow("    ══╝") + white("  ║\n\
         ║\n"),
            white('jt'),
            red('Usage'),
            white('jt ') + green('FILENAME ') + white('[-h] [-s] [-u ') + cyan('URL') + white(']'),
            red('Options'),
            white('-h'),
            white('-s'),
            yellow('STREAM'),
            white('-u'),
            cyan('HTTP GET request'),
            red('Examples'),
            cyan('HTTP GET request'),
            white('jt -u ') + cyan('URL'),
            green('FILE'),
            white('jt ') + green('FILENAME'),
            yellow('STREAM'),
            'echo ' + yellow('\'{"node_0": {"node_0_0": [{"node_0_0_0": "", "node_0_0_1": [""]}]}}\' ') 
                + '| ' + white('jt -s'),
            white('jt -h '),
            red('Legend'),
            green('\'') + str('node_0') + green('\''),
            green('string'),
            cyan('[') + str('node_0') + cyan(']'),
            cyan('array'),
            magenta('{') + str('node_0') + magenta('}'),
            magenta('dictionary'),
        )
        print(help_string)

        sys.exit(0)

    if u:
        j.tree(json.loads(requests.get(u).text))

    if s:
        input_buffer = json.loads(''.join([l for l in sys.stdin]))
        j.tree([input_buffer])

    if filename:
        d = ''.join([i for i in open(filename, 'r')])
        j.tree([(json.loads(d))])

