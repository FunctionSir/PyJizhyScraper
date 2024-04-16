#!/bin/python3
'''
Author: FunctionSir
License: AGPLv3
Date: 2024-04-16 18:32:04
LastEditTime: 2024-04-16 19:28:23
LastEditors: FunctionSir
Description: https://www.jizhy.com/44/rank/school scraper.
FilePath: /jizhyrank.py
'''

import os
import hashlib
import time

### SPECIAL DEPENDENCY ###
# Curl is required.

### CONFIG HERE ###
OutputFile: str = ""
ExtraCurlArgs: str = ""
ArgPage: str = "1"
ArgPageLen: str = "2000"


# MAKE URL #
def make_url() -> str:
    ts: str = str(int(time.time()*1000))
    data: str = "{app_id=98357f659cf8fb6001cff80f7c6b85f2&diploma_id=7&page="+ArgPage+"&page_len="+ArgPageLen+"&platform=desktop&ts=" + \
        ts+"&v=210&wenli=0}&key=146fd1e66513611ac7af69f21f1d7725"
    sign: str = hashlib.md5(data.encode("utf-8")).hexdigest().upper()
    url: str = "https://www.jizhy.com/open/sch/rank-list?page=1&page_len=2000&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=" + \
        ts+"&platform=desktop&v=210&sign="+sign
    return url


# CHECK OUTPUT FILE PATH #
if len(OutputFile) < 1:
    print("! YOU SHOULD CONFIG THE PATH OF THE OUTPUT FILE FIRST !")
    exit(1)

# USE CURL TO DOWNLOAD #
os.system("curl \'"+make_url()+"\' -o "+OutputFile+" "+ExtraCurlArgs)
