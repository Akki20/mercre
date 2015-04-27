#!/usr/bin/env python
# -*- coding:utf-8 -*-
#---------------------------------------------------------------------------
# Name:        config.py
# Purpose:     各種設定
#
# Author:      Kosuke Akizuki
#
# Created:     2015/03/11
# Copyright:   (c) Kosuke Akizuki 2015
# Licence:     The MIT License (MIT)
#---------------------------------------------------------------------------

__author__ = "Kosuke Akizuki <waruoni.work@gmail.com>"
__status__ = "OK"
__version__ = "1.0"
__date__    = "11 Mar 2015"

import os

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

HOME = os.environ.get('HOME')

"""
このツールで使われる設定群です
"""

#[FORMAT]
DATE_FORMAT_PATTERN = '%Y.%m.%d_%H%M'

#[INOUT OUTPUT]
#SOURCE_FOLDER = join(HOME, 'Desktop/ダウンロード/KIRIN/00_input')
#OUTPUT_FOLDER = join(HOME, 'Desktop/ダウンロード/KIRIN/00_output')

#[TEST]
SOURCE_FOLDER = join(HOME, 'Desktop/mercre/test/src')
OUTPUT_FOLDER = join(HOME, 'Desktop/mercre/test/out')

#[MESSAGE]
COMPLETE_MESSAGE =\
'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 .--  .-.  |-.-  .--. | |~~| --|-- |~~|
(    |   | | | | |  | | |--    |   |--
 "--  "-"  ' ' ' |""" | =--    |=  =--
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

#[IGNORE]
IGNORE = [
    '.*',
    'Thumbs.db',
    'nbproject'
]
