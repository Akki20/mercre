#!/usr/bin/env python
# -*- coding:utf-8 -*-
#---------------------------------------------------------------------------
# Name:        mercre.py
# Purpose:     mercre
#
# Author:      Kosuke Akizuki
#
# Created:     2015/03/11
# Copyright:   (c) Kosuke Akizuki 2015-2018
# Licence:     The MIT License (MIT)
#---------------------------------------------------------------------------

__author__ = "Kosuke Akizuki <kosuke19952000@gmail.com>"
__status__ = "OK"
__version__ = "1.0"
__date__    = "11 Mar 2015"

import os
import mercre
from config import (
    DATE_FORMAT_PATTERN,
    SOURCE_FOLDER,
    OUTPUT_FOLDER,
    COMPLETE_MESSAGE,
    IGNORE
)

OKGREEN = '\033[92m'
ENDC = '\033[0m'

def join(*args):
    """
    パスの結合
    USAGE: join(path[, path....])
    """
    path = ''
    for e in args:
        path = os.path.join(path, e)
    path = os.path.normcase(path)
    path = os.path.normpath(path)
    return path

def main():
    if type(SOURCE_FOLDER) is str and type(OUTPUT_FOLDER) is str:
        mercre.merge(SOURCE_FOLDER, OUTPUT_FOLDER, \
                DATE_FORMAT_PATTERN, False, IGNORE)

    elif ( type(SOURCE_FOLDER) is list or type(SOURCE_FOLDER) is tuple ) and \
         ( type(OUTPUT_FOLDER) is str ):

        n = len(SOURCE_FOLDER)

        for i in range(n):
            src = SOURCE_FOLDER[i]
            dir_name = os.path.basename(src)

            mercre.merge(SOURCE_FOLDER[i], join(OUTPUT_FOLDER, dir_name), \
                DATE_FORMAT_PATTERN, False, IGNORE)

    else:
        raise ValueError('''The value of the SOURCE_FOLDER or OUTPUT_FOLDER is invalid value.''')

    print(OKGREEN + COMPLETE_MESSAGE + ENDC)

if __name__ == '__main__':
    main()
