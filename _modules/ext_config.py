# -*- coding: utf-8 -*-
#
# vim: set ts=4 sw=4 sts=4 et :
'''
:maintainer:    Jason Mehring <nrgaway@gmail.com>
:maturity:      new
:depends:       none
:platform:      all

Configuration module to calculate formula root directories per
salt environment.
'''

# Import python libs
import os
import logging

# Import salt libs
import salt.utils.dictupdate

from salt.utils.odict import OrderedDict
from salt.utils.templates import SLS_ENCODING

# Import third party libs
import salt.ext.six as six

# Enable logging
log = logging.getLogger(__name__)

# Define the module's virtual name
__virtualname__ = 'config'


def __virtual__():
    '''
    '''
    return __virtualname__


def readdirs(dirpath, abspath=False):
    '''
    Returns a list of directories.

    Excludes files and any directories starting with
    '.', '..', and '_'.
    '''
    dirs = []

    if not dirpath or not os.path.exists(os.path.realpath(dirpath)):
        return []

    if not os.path.isdir(dirpath):
        dirpath = os.path.dirname(dirpath)

    for relpath in __salt__['file.readdir'](dirpath):
        # Ignore hidden '.*', private '_*' '.' and '..'
        if relpath and relpath[0] in ['.', '_']:
            continue

        # Only allow directories
        if not os.path.isdir(os.path.join(dirpath, relpath)):
            continue

        if isinstance(relpath, six.text_type):
            relpath = relpath.encode(SLS_ENCODING)

        if abspath:
            dirs.append(os.path.join(dirpath, relpath))
        else:
            dirs.append(relpath)

    return dirs


def file_roots(roots=None, formula_dirs=None, envs=True):
    '''
    formula_dirs: Root formula directory path
    envs: formula_dirs contains saltenv sub-directories

    Returns all formula based file roots.
    '''
    if roots:
        roots = OrderedDict(roots)
    else:
        roots = OrderedDict()

    formula_dirs = formula_dirs or __opts__.get(u'formula_dirs', ['/srv/formulas'])

    for formula_dir in formula_dirs:
        if envs:
            saltenvs = readdirs(formula_dir)
            if 'base' in saltenvs and saltenvs[0] != 'base':
                saltenvs.insert(0, saltenvs.pop(saltenvs.index('base')))
        else:
            saltenvs = [None]

        for env in saltenvs:
            if env is None:
                dirpath = formula_dir
                env = 'base'
            else:
                dirpath = os.path.join(formula_dir, env)

            for relpath in readdirs(dirpath):
                abspath = os.path.join(dirpath, relpath)
                salt.utils.dictupdate.update(roots, {env: [abspath]})

    return roots
