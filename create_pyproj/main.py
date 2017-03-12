"""create_pyproj create python project template command line tool."""

from create_pyproj.options import Options
from create_pyproj.template import create_python_template

import argparse
import sys
from typing import List


def process_options(args: List[str]) -> Options:
    options = Options()
    # Make the help output a little less jarring.
    help_factory = (lambda prog: argparse.RawDescriptionHelpFormatter(
        prog=prog, max_help_position=28))

    parser = argparse.ArgumentParser(prog='create_pyproj',
                                     fromfile_prefix_chars='@',
                                     formatter_class=help_factory)
    parser.add_argument(
            "-p", "--path", metavar='create template file path',
            nargs=1, help="[optional] create template file path")
    # parser.add_argument('--text', action='store_true')

    parser.add_argument(
            "-a", "--auth", metavar='set auth name',
            nargs=1, help="[optional] auth name")
 
    args = parser.parse_args()

    if args.path:
        options.path = args.path[0]

    if args.auth:
        options.auth = args.auth[0]

    return options


def main() -> None:
    options = process_options(sys.argv[1:])
    
    create_python_template(options)

    sys.exit(0)
