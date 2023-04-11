# -- coding: utf-8 --
"""
@Name: demo1_sign加密.py
@Auth: Ming-Log
@Date: 2023/4/11-19:28
@Desc: 
"""
import time
import execjs

# 模拟sign参数
token = '98db12d56bb5e26159c2c0e16743d0c0'
i = int(time.time() * 1000)
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
    'cookie': 'lid=luo736704198; alicnweb=touch_tb_at%3D1680934612278; _m_h5_tk=98db12d56bb5e26159c2c0e16743d0c0_1681220346823; _m_h5_tk_enc=fb7429c7b227adfe55c512741839e415; cookie1=BxSpHzb8GFsmSZHfbbB2adm%2FkInUN6kmS5LxVyBbwTk%3D; cookie2=166d0849c545842eeffd74dfaf147c9c; cookie17=UUGiHQt0GQ%2BU%2FQ%3D%3D; sgcookie=E10075e0oW6bDw5X8dlaQDOiIR0vgWI%2BpmsqdF%2FlAo9M6UlMoIqVMOxCAs7TF5EHvCnYNssyu8aagDM0vx7nDQHHjLvE801aXHKdHiP9xlB2Zck%3D; t=73833a3ac4c852d0f5656f3778fb2fff; _tb_token_=333efe5eee54b; sg=85d; csg=5e2d3c90; unb=2906023675; uc4=nk4=0%40DfV%2FByDhGKnRdwQiYyWpvjxAjEKwc6o%3D&id4=0%40U2OVFc7GR%2FBF8IuOJ%2FZPP0%2Fk2IT8; __cn_logon__=true; __cn_logon_id__=luo736704198; ali_apache_track=c_mid=b2b-2906023675ae282|c_lid=luo736704198|c_ms=1; ali_apache_tracktmp=c_w_signed=Y; _nk_=luo736704198; last_mid=b2b-2906023675ae282; _csrf_token=1681213129057; __mwb_logon_id__=luo736704198; mwb=ng; x5sec=7b226d746f703b32223a22656661303666666434383563396433376463376165353361303661353332303243494b5131614547454e663671746134745a587068774561444449354d4459774d6a4d324e7a55374d544362396657592f762f2f2f2f384251414d3d227d; cna=6QwQGjcvqQ0CAatxtqzgPaAk; l=fBMhOOe4NSPHmkzvXOfaFurza77OSIRYYuPzaNbMi9fP9k1B5yUcW1g7-A86C3GVFsdkR3o-P8F6BeYBq3xonxvtjsx8SPDmndLHR35..; isg=BAUFck8ezbE5senoi1gnyHIBFEE_wrlUWmfejgdqwTxLniUQzxLJJJN4qMJo3tEM',
    'referer': 'https://sale.1688.com/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}

res = requests.get(url, params=params, headers=headers)
print(res.text)
