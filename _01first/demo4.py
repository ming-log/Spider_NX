# -- coding: utf-8 --
"""
@Name: demo4.py
@Auth: Ming-Log
@Date: 2023/4/8-16:55
@Desc: 
"""
# 全国建筑市场监督公共服务平台    https://jzsc.mohurd.gov.cn/data/company
import requests
import execjs
import json

api = 'https://jzsc.mohurd.gov.cn/APi/webApi/dataservice/query/comp/list'

params = {
    'pg': 2,
    'pgsz': 15,
    'total': 450,
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'Referer': 'https://jzsc.mohurd.gov.cn/data/company'

}
response = requests.get(api, params=params, headers=headers)
data = response.text

with open('demo4.js', 'r', encoding='UTF-8') as f:
    jscode = f.read()

ctx = execjs.compile(jscode).call('h', data)
print(ctx)

# 第一次运行报错，错误参考 https://blog.csdn.net/Liquor6/article/details/120782193 解决
