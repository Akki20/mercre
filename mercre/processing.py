#!/usr/bin/env python
# -*- coding:utf-8 -*-
#---------------------------------------------------------------------------
# Name:        processing.py
# Purpose:     excuteが処理を実行するメイン関数です。
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

import os
import re
import shutil
from datetime import datetime

from .packages   import merger
from .dateformat import dateformat
from .compat     import is_osx

def execute(dir_src, dir_dst, pattern, symlinks=False, ignore=list()):
    """
    マージ処理を実行するメイン関数です。

    Return:    True:  マージに成功したとき
               False: マージに失敗したか、マージをするフォルダが存在しない
    """

    # フォルダリストをゲット
    try:
        dirs = _getdirs(dir_src)
    except WindowsError as e:
        # 元データ(dir_src以下のフォルダ)がなかったら例外をはく
        sys.stderr.write(str(e))
        exit(1)

    # 全データのセット
    # target_data[0]:   パスネーム
    # target_data[1]:   date
    # target_data[2]:   date以降の文字列
    target_data = list()

    if is_osx:
        # mac環境でディレクトリの名前をpythonで探すと、 "/" が ":" に変化するらしいので、それに合わせた対応
        pattern = pattern.replace('/', ':')

    # フォルダリストから、日付データとパスのセットをゲット
    target_data = _analyze_pathname(dirs, pattern)

    # ここで 'target_data == 0' の時、パターンに合うデータが存在しない
    # マージをするフォルダが存在しないので、Falseを返す
    if len(target_data) == 0:
        return False

    # 未来日付は対象外にする
    now = datetime.now()
    target_data = [x for x in target_data if x[1] < now]

    # 同じカテゴリーネームは最新のものを適応
    target_data = _uniq_category(target_data)

    # ソート
    target_data.sort(key=lambda x: x[1])

    # パス部分だけを抽出
    paths = [x[0] for x in target_data]

    # 出力先を初期化 存在していたら、全消去
    if os.path.exists(dir_dst):
        shutil.rmtree(dir_dst)

    # マージ作業
    merger.merge(paths, dir_dst, symlinks, shutil.ignore_patterns(*ignore))

    # マージに成功したので、Trueを返す
    return True

def _uniq_category(targets):
    """
    カテゴリーネームが一意なリストを抽出
    """
    result = list()
    targets.sort(key=lambda x: (x[2], x[1]), reverse=True)
    category = ""
    for target in targets:
        if category != target[2]:
            result.append(target)
            category = target[2]

    return result


def _getdirs(path):
    """
    パスの直下にあるディレクトリのリストを返す
    """
    dirs = list()
    listdir = os.listdir(path)
    for item in listdir:
        fullpath = os.path.join(path,item)
        if os.path.isdir(fullpath):
            dirs.append(os.path.abspath(fullpath))
    return dirs


def _analyze_pathname(dirs, pattern):
    """
    ディレクトリネームを解析して、パスと日付のセットを返す
    """
    data = list()
    for dir in dirs:
        basename = os.path.basename(dir)
        date = dateformat(basename, pattern)
        category_name = _cat_pathname(basename, pattern)
        if _isNotNone(date, category_name):
           data.append((dir, date, category_name))
    return data


def _cat_pathname(basename, pattern):
    """
    ディレクトリ名から、patternにマッチした部分以後の文字列を取り出す
    """
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
    p = re.compile(dst + '(?P<tail>.*$)')
    match = p.search(basename)
    if match:
        return match.group('tail')
    else:
        return None

def _isNotNone(*args):
    for arg in args:
        if arg is None:
            return False
    return True


if __name__ == '__main__':
    execute('../test/src/', '../test/out/', pattern="%Y.%m.%d_%H%M", ignore=['2014_01_01_hogehoge1.txt'])
    # for item in getdirs('../test/src/2014_01_01_2014_01_01_hogehoge1'):
    #     print(os.path.basename(item))
    # pprint(getdirs('../test/src/2014_01_01_2014_01_01_hogehoge1'))
