#!/usr/bin/env python
# -*- coding:utf-8 -*-
#---------------------------------------------------------------------------
# Name:        mercre.py
# Purpose:     mercre
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

def main():
    mercre.merge(SOURCE_FOLDER, OUTPUT_FOLDER, \
                DATE_FORMAT_PATTERN, False, IGNORE)
    print(OKGREEN + COMPLETE_MESSAGE + ENDC)

if __name__ == '__main__':
    main()
