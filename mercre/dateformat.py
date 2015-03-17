#!/usr/bin/env python
# -*- coding:utf-8 -*-
#---------------------------------------------------------------------------
# Name:        dateformat.py
# Purpose:     dateformat
#
# Author:      Kosuke Akizuki
#
# Created:     2015/03/11
# Copyright:   (c) Kosuke Akizuki 2015
# Licence:     The MIT License (MIT)
#---------------------------------------------------------------------------

__author__ = "Kosuke Akizuki <slife1080@gmail.com>"
__status__ = "OK"
__version__ = "1.0"
__date__    = "11 Mar 2015"

import re
from datetime import datetime

def dateformat(string, pattern):
    dst = pattern
    dst = dst.replace('%a', '(Sun|Mon|Tue|Wed|Thu|Fri|Sat)')
    dst = dst.replace('%A', '(Sunday|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday)')
    dst = dst.replace('%w', '[0-6]')
    dst = dst.replace('%d', '[0-3]?[0-9]')
    dst = dst.replace('%b', '(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)')
    dst = dst.replace('%B', '(January|February|March|April|May|June|July|August|September|October|November|December)')
    dst = dst.replace('%m', '[01]?[0-9]')
    dst = dst.replace('%y', '[0-9]{2}')
    dst = dst.replace('%Y', '[0-9]{4}')
    dst = dst.replace('%H', '[0-2]?[0-9]')
    dst = dst.replace('%I', '[0-1]?[0-9]')
    dst = dst.replace('%p', '(AM|PM)')
    dst = dst.replace('%M', '[0-5]?[0-9]')
    dst = dst.replace('%S', '[0-6]?[0-9]')
    dst = dst.replace('%f', '[0-9]{6}')
    dst = dst.replace('%z', '([+-][01][0-9][0-6][0-9])?')
    dst = dst.replace('%Z', '(UTC|EST|CST)?')
    dst = dst.replace('%j', '[0-3]?[0-9]?[0-9]')
    dst = dst.replace('%U', '[0-5]?[0-9]')
    dst = dst.replace('%W', '[0-5]?[0-9]')
    p = re.compile(dst)
    match = p.search(string)
    if match:
        return datetime.strptime(match.group(0), pattern)
    else:
        return None

if __name__ == '__main__':
    print(dateformat("2014_01_01_hogehoge1", "%Y_%m_%d"))
