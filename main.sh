#!/bin/bash
#
# @(#) main.sh ver.1.0.0 2015.3.18
#
# Usage: ./mercre.sh
# Author:      Kosuke Akizuki
#
# Description:
#   mercre を動作させるスクリプト
#
# Created:     2015/3/18
# Copyright:   (c) Kosuke Akizuki 2015-2018
# Licence:     The MIT License (MIT)
###########################################################################

if type python3 >/dev/null 2>&1; then
  python3 __main__.py $@
  exit 0
fi
if type python >/dev/null 2>&1; then
  python __main__.py $@
  exit 0
fi

echo "python is not found!"
echo "Please install python!!"
exit 1
