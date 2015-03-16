#!/usr/bin/env python
# -*- coding:utf-8 -*-
#---------------------------------------------------------------------------
# Name:        api.py
# Purpose:     api
#
# Author:      Kosuke Akizuki
#
# Created:     2015/03/11
# Copyright:   (c) Kosuke Akizuki 2015
# Licence:     The MIT License (MIT)
#---------------------------------------------------------------------------

__author__ = "Kosuke Akizuki <slife1080@gmail.com>"
__status__ = "OK"
__version__ = "0.1"
__date__    = "11 Mar 2015"

import processing

def merge(dir_src, dir_dst, pattern, symlinks=False):
    if _isNotNone(dir_src, dir_dst, pattern) and \
       _isNotEmpty(dir_src, dir_dst, pattern):
        status_code = processing.execute(dir_src, dir_dst, pattern, symlinks)
        # マージが実行されなかった時に、falseが返ってくるので、
        # その時は警告を発する
        if status_code == False:
            raise SyntaxWarning('''Not able to merge it with this pass or date pattern.
               Please confirm it!!!''')
    else:
        raise ValueError('''The value of the argument is "None" or empty.
            The value except "None" or empty, please.''')

def _isNotNone(*args):
    for arg in args:
        if arg is None:
            return False
    return True

def _isNotEmpty(*args):
    for arg in args:
        if not str(arg):
            return False
    return True

if __name__ == '__main__':
    merge('../test/src/', '../test/out/', "a")
