# -- coding: utf-8 --
"""
@Name: demo1_sign加密.py
@Auth: Ming-Log
@Date: 2023/4/11-19:28
@Desc: 
"""
# 目标网址：https://sale.1688.com/factory/category.html?spm=a260k.22464671.home2019category.1.69517a6eFclvLv&mainId=10166
# get请求参数加密
import time
import execjs

# 模拟sign参数
token = '39fa28587fbbb780591c41b82f10768d'
# i = int(time.time() * 1000)
i = 1681266229197
g = '12574478'
data = '{"cid":"TpFacRecommendService:TpFacRecommendService","methodName":"execute","params":"{\\"query\\":\\"mainCate=10166&leafCate=\\",\\"sort\\":\\"mix\\",\\"pageNo\\":\\"1\\",\\"pageSize\\":\\"20\\",\\"from\\":\\"PC\\",\\"trafficSource\\":\\"pc_index_recommend\\"}"}'

sign = token + "&" + str(i) + "&" + g + "&" + data

# 读取JS文件
with open('demo1_sign加密.js', 'r', encoding='UTF-8') as f:
    jscode = f.read()
sign_key = execjs.compile(jscode).call('h', sign)
print(sign_key)


# 接下来使用sign参数获取数据
import requests

# 请求API
url = 'https://h5api.m.1688.com/h5/mtop.taobao.widgetservice.getjsoncomponent/1.0/'

params = {
    'jsv': '2.6.1',
    'appKey': '12574478',
    't': i,
    'sign': sign_key,
    'v': '1.0',
    'type': 'jsonp',
    'isSec': 0,
    'timeout': 20000,
    'api': 'mtop.taobao.widgetService.getJsonComponent',
    'dataType': 'jsonp',
    'jsonpIncPrefix': 'mboxfc',
    'callback': 'mtopjsonpmboxfc3',
    'data': data,
}

headers = {
    'cookie': '_m_h5_tk=39fa28587fbbb780591c41b82f10768d_1681273954955; _m_h5_tk_enc=0fc50b2ad31ad75886dc75b07fe63c52; cna=xmSwHB30+BoCAatxC/YGDwhg; __cn_logon__=false; cookie2=17587c37543b059c1d7ec0ffdff3ffcc; t=fded188e1a82a7fc2f7091f86afe7b3c; _tb_token_=eb373e3393543; isg=BF9fZDopRyCuKkM88OdugbVp7rPpxLNmqLKP_fGszI5UgH8C-Zc-tstRQhD-GIve; l=fBrbiHXnNM-31QhiBOfZnurza7799IRAguPzaNbMi9fP9p5p5o3RW1grVHY9CnGVFsiDR3kOuRA9BeYBq3K-nxvtjsx8SPkmne_7Qn5..',
    'referer': 'https://sale.1688.com/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}

res = requests.get(url, params=params, headers=headers)
print(res.text)
