#!/usr/bin/env python
# -*- coding:utf-8 -*-
#---------------------------------------------------------------------------
# Name:        fileUtil.py
# Purpose:     fileUtil
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

import re
import os
import shutil

def copytree_overwritte(src, dst, symlinks=False, ignore=None):
    """
    srcディレクトリから、dstディレクトリにフォルダごと、
    上書きコピーを行います
    """
    names = os.listdir(src)

    if ignore is not None:
        ignored_names = ignore(src, names)
    else:
        ignored_names = set()

    if not os.path.exists(dst):
        os.makedirs(dst)
    errors = []

    for name in names:
        if name in ignored_names:
            continue

        srcname = os.path.join(src, name)
        dstname = os.path.join(dst, name)

        try:
            if symlinks and os.path.islink(srcname):
                linkto = os.readlink(srcname)
                os.symlink(linkto, dstname)
            elif os.path.isdir(srcname):
                copytree_overwritte(srcname, dstname, symlinks, ignore)
            else:
                shutil.copy2(srcname, dstname)
            # XXX What about devices, sockets etc.?
        except OSError as why:
            errors.append((srcname, dstname, str(why)))
        # catch the Error from the recursive copytree so that we can
        # continue with other files
        except StandardError as err:
            errors.extend(err)
    try:
        shutil.copystat(src, dst)
    except OSError as why:
        # can't copy file access times on Windows
        if why.winerror is None:
            errors.extend((src, dst, str(why)))
    if errors:
        raise StandardError(errors)
