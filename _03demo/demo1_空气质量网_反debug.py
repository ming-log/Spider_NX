# -- coding: utf-8 --
"""
@Name: 反debug.py
@Auth: Ming-Log
@Date: 2023/4/12-20:41
@Desc: 
"""
# 网站：https://www.aqistudy.cn/historydata/monthdata.php?city=%E6%AD%A6%E6%B1%89
# 空气质量指数
# 难点：右键被禁用，F12调试自动清空，反debugger
# 使用点击方式进入开发者工具，右键debugger使得其不再被停止，然后将开发者工具弹出浏览器即可正常分析
# 加密方式比较复杂，参数加密，结果加密
# JS动态混淆，每次刷新网页所有函数和变量全部更新
import requests
import execjs

# 获取响应参数
mHTBGYKS9 = 'GETDAYDATA'

oGX3TKciee = {'city': '武汉', 'month': '201504'}

# 调用JS获取加密参数
with open('demo1_空气质量网_参数解密.js', 'r', encoding='utf-8') as f:
    jscode1 = f.read()

mHTBGYKS9 = 'GETDAYDATA'
oGX3TKciee = {'city': '武汉', 'month': '201312'}
hrXZtrXfc = execjs.compile(jscode1).call('p0I8Eq2vSsJj4', mHTBGYKS9, oGX3TKciee)
print(hrXZtrXfc)

url = 'https://www.aqistudy.cn/historydata/api/historyapi.php'

data = {
    'hrXZtrXfc': hrXZtrXfc
}

headers = {
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': "Windows",
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Host': 'www.aqistudy.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}

# 获取到加密数据
res_key = requests.post(url, data=data, headers=headers, verify=False).text
print(res_key)

# 调用JS解密加密数据
# 调用JS获取加密参数
# with open('demo1_空气质量网_返回参数解密.js', 'r', encoding='utf-8') as f:
#     jscode2 = f.read()
#
# res = execjs.compile(jscode2).call('dr6NPmheSxfCgyfvkPpH', res_key)
#
