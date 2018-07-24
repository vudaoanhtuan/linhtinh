# -*- coding: utf-8 -*-

"""Translate text to Vietnamese.
Usage: vi <text>
Example: vi hello
"""

from albertv0 import *
import sqlite3 as S
import json
import re
import urllib.request
import urllib.parse

__iid__ = "PythonInterface/v0.1"
__prettyname__ = "Dictionary En - Vi"
__version__ = "1.0"
__trigger__ = "v "
__author__ = "Vu Dao Anh Tuan"
__dependencies__ = []


iconPath = iconLookup('config-language')
if not iconPath:
    iconPath = ":python_module"

def is_mean(s):
    if s.count('=') == 10 and s.find('[[') == -1:
        print(s.find('[['))
        return True
    return False


def handleQuery(query):
    results = []

    if query.isTriggered:
            
        fields = query.string.split()
        item = Item(id=__prettyname__, icon=iconPath, completion=query.rawString)
        if len(fields) >= 1:
            src = "en"
            dst = "vi"
            word = " ".join(fields[0:])


            conn = S.connect("/home/vdat/project/dictionary-albert/dic.db")
            sql = "SELECT mean FROM words WHERE word=?"

            c = conn.execute(sql, (word,))

            raw = c.fetchall()

            if len(raw) == 0:
                return []

            raw = raw[0][0]

            list_mean = re.split("[^=]==[^=]+==[^=]", raw)
            
            id = 0

            if list_mean[0].find('font color') >= 0:
                id = 1

            mean = [m for m in list_mean[id].split("\n") if len(m) > 0 and m[0] == '=']

            i = 0

            list_type = ['other']

            res = {'other':[]}

            while True:
                if not i<len(mean):
                    break
                s = mean[i]
                if s.count('=') == 6:
                    word_type = s.replace('=', '')
                    i+=1
                    l = []
                    while i<len(mean) and is_mean(mean[i]):
                        l.append(mean[i].replace('=', ''))
                        i+=1
                    res[word_type] = l
                    list_type.append(word_type)
                else:
                    if is_mean(mean[i]):
                        res['other'].append(mean[i].replace('=', ''))
                    i+=1

            for k in list_type:
                l = res[k]
                if len(l) > 0:
                    for m in l:
                        results.append(
                            Item(
                                id=__prettyname__,
                                icon=iconPath,
                                text="%s" % (m),
                                subtext="%s" % k,
                            )
                        )
            

            conn.close()

        else:
            item.text = __prettyname__
            item.subtext = "Enter a query in the form of \"vi &lt;word&gt;\""
            return item
    return results