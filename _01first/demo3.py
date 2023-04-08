# -- coding: utf-8 --
# https://www.qimingpian.com/finosda/project/pinvestment
# 网页出现加密该怎么做，通过检索无法找到，无法定位数据接口

# Python调用js
# 1. 使用 pyexecjs   pip install pyexecjs   这个是用得最多的库
# 2. 使用PyV8   仅支持Python3.3
# 3. 使用js2py    将JS代码转化为Python代码    仅适用于比较短的JS代码

# 使用Python调用js代码
import execjs
import requests

#
# print(execjs.get().name)
# ctx = execjs.compile("""
#     function add(x, y){
#         return x + y
#     }
# """)
# print(ctx.call('add', 1, 2))

# -------------
# 获取data
# url = 'https://vipapi.qimingpian.cn/DataList/productListVip'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
# }
# data = {
#     'time_interval': '',
#     'tag': '',
#     'tag_type': '',
#     'province': '',
#     'lunci': '',
#     'page': 1,
#     'num': 20,
#     'unionid': ''
# }
#
# string_ = requests.post(url, headers=headers, data=data).json()['encrypt_data']
#
# # 调用JS代码进行反解密
# with open('demo3.js', 'r', encoding='UTF-8') as f:
#     jscode = f.read()
#
# ctx = execjs.compile(jscode).call('s', string_).replace('\/', '/')
# print(ctx.encode("utf-8").decode("unicode_escape"))

# -------------------

# import PyV8  # 下载时需要先安装对应二进制文件 https://github.com/emmetio/pyv8-binaries
# 只支持3.3已弃用
# ----------------------
# import js2py
#
# # 将JS代码编译成Python代码进行执行
# add = js2py.eval_js("""
#     function add(x, y){
#         return x + y
#     }
# """)
#
# print(add(2, 3))
