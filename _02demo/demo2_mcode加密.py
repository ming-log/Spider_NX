# -- coding: utf-8 --
"""
@Name: demo2_mcode加密.py
@Auth: Ming-Log
@Date: 2023/4/11-20:08
@Desc: 
"""
# 目标网址：https://webapi.cninfo.com.cn/#/marketDataDate
# 请求头加密

"""
base64:有以下内容构成 A-Z a-z 0-9 \/; =
"""
import execjs

with open('demo2_mcode加密.js', 'r', encoding='UTF-8') as f:
    jscode = f.read()

mcode = execjs.compile(jscode).call('getResCode')

import requests

url = 'https://webapi.cninfo.com.cn/api/sysapi/p_sysapi1007'

data = {
    'tdate': '2023-03-29',
    'market': 'SZE'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    # 'mcode': 'MTY4MTIxNjAyOA==',
    'mcode': mcode,
    'Origin': 'https://webapi.cninfo.com.cn',
    'Referer': 'https://webapi.cninfo.com.cn/'
}

res = requests.post(url, data=data, headers=headers)
print(res.text)
