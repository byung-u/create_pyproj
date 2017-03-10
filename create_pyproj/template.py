"""create_pyproj create python project template command line tool."""

from create_pyproj.options import Options

import argparse
import os
import sys
from typing import List, Tuple


def get_path_and_proj(options: Options) -> Tuple[str, str]:
    if options.path is None and options.proj is None:
        path = './new_project'
        proj = 'new_project'
    elif options.path is None and options.proj is not None:
        path = './new_project'
        proj = options.proj
    elif options.path is None and options.proj is None:
        path = options.path
        proj = 'new_project'
    else:
        path = options.path
        proj = options.proj

    return path, proj

def create_python_template(options: Options) -> bool:

    path, proj = get_path_and_proj(options)
    #1. create directory
    if not os.path.exists(path):
        os.makedirs(path)

    print(path, proj)
