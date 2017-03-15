"""create_pyproj create python project template command line tool."""

from create_pyproj.options import Options

import os
import shutil
import sys
from typing import List, Tuple


def get_path_and_proj(options: Options) -> Tuple[str, str]:
    if options.path is None and options.proj is None:
        options.path = './new_project'
        options.proj = 'new_project'
    elif options.path is None and options.proj is not None:
        options.path = './new_project'
    elif options.path is not None and options.proj is None:
        options.proj = 'new_project'

    return options

def create_python_template(options: Options) -> bool:

    options = get_path_and_proj(options)
    #1. create directory
    if os.path.exists(options.path):
        # remove last template
        print('remove dir:', options.path)
        shutil.rmtree(options.path)

    os.makedirs(options.path)
    os.chdir(options.path)
     
    create_file('LICENSE', options)
    create_file('README.md', options)
    create_file('TODO.md', options)

    if not os.path.exists('docs'):
        os.makedirs('docs')
    create_file('./docs/conf.py', options)
    create_file('./docs/generated', options)
    create_file('./docs/index.rst', options)
    create_file('./docs/installation.rst', options)
    create_file('./docs/modlues.rst', options)
    create_file('./docs/quickstart.rst', options)
    project_rst = '%s.rst' % options.proj
    create_file('./docs/project.rst', options)

    if not os.path.exists(options.proj):
        os.makedirs(options.proj)
        test_path = './%s/test' % options.proj
        if not os.path.exists(test_path):
            os.makedirs(test_path)
        test_file = '%s/__init__.py' % test_path
        create_file(test_file, options)
        test_file = '%s/test_main.py' % test_path
        create_file(test_file, options)
    proj_file = '%s/__init__.py' % options.proj
    create_file(proj_file, options)
    proj_file = '%s/exception.py' % options.proj
    create_file(proj_file, options)
    proj_file = '%s/main.py' % options.proj
    create_file(proj_file, options)
    proj_file = '%s/model.py' % options.proj
    create_file(proj_file, options)

    create_file('./requirements.txt', options)

    if not os.path.exists('scripts/'):
        os.makedirs('scripts/')
    proj_file = './scripts/%s' % options.proj
    create_file(proj_file, options)

    create_file('./setup.py', options)

def create_file(file_name, options):
    fw = open(file_name, 'w')
    if (file_name == 'LICENSE'):
        fw.write('''MIT License

Copyright (c) %d %s

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.''' % (options.year, options.auth))
    elif (file_name == 'README.md'):
        fw.write('''%s
--------------------
%s''' % (options.proj, options.proj))
    elif (file_name == 'TODO.md'):
        fw.write('-')

    fw.close()
