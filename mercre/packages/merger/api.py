#!/usr/bin/env python
# -*- coding:utf-8 -*-
#---------------------------------------------------------------------------
# Name:        api.py
# Purpose:     api
#
# Author:      Kosuke Akizuki
#
# Created:     2015/03/11
# Copyright:   (c) Kosuke Akizuki 2015-2018
# Licence:     The MIT License (MIT)
#---------------------------------------------------------------------------

__author__  = "Kosuke Akizuki <kosuke19952000@gmail.com>"
__status__  = "OK"
__version__ = "1.0"
__date__    = "11 Mar 2015"

from .fileUtil import copytree_overwritte

def merge(srcs, dsts, symlinks=False, ignore=None):

    if isinstance(srcs, str) and isinstance(dsts, str):
        copytree_overwritte(srcs, dsts, symlinks, ignore)

    elif (isinstance(srcs, list) or isinstance(srcs, tuple)) and \
          isinstance(dsts, str):
        for src in srcs:
            copytree_overwritte(src, dsts, symlinks, ignore)

    elif isinstance(srcs, str) and \
        (isinstance(dsts, list) or isinstance(dsts, tuple)):
        for dst in dsts:
            copytree_overwritte(srcs, dst, symlinks, ignore)

    elif (isinstance(srcs, list) or isinstance(srcs, tuple)) and \
         (isinstance(dsts, list) or isinstance(dsts, tuple)):
        for src in srcs:
            for dst in dsts:
                copytree_overwritte(src, dst, symlinks, ignore)

    else:
        raise ValueError("Invalid argument.")
