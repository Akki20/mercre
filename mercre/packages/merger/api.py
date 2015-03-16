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

__author__  = "Kosuke Akizuki <slife1080@gmail.com>"
__status__  = "OK"
__version__ = "1.0"
__date__    = "11 Mar 2015"

from .fileUtil import copytree_overwritte

def merge(srcs, dsts, symlinks=False):

    if isinstance(srcs, str) and isinstance(dsts, str):
        copytree_overwritte(srcs, dsts, symlinks)

    elif (isinstance(srcs, list) or isinstance(srcs, tuple)) and \
          isinstance(dsts, str):
        for src in srcs:
            copytree_overwritte(src, dsts, symlinks)

    elif isinstance(srcs, str) and \
        (isinstance(dsts, list) or isinstance(dsts, tuple)):
        for dst in dsts:
            copytree_overwritte(srcs, dst, symlinks)

    elif (isinstance(srcs, list) or isinstance(srcs, tuple)) and \
         (isinstance(dsts, list) or isinstance(dsts, tuple)):
        for src in srcs:
            for dst in dsts:
                copytree_overwritte(src, dst, symlinks)

    else:
        raise ValueError("Invalid argument.")
