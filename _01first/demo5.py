# 目标网址：https://ys.endata.cn/BoxOffice/Ranking
import requests

url = 'https://ys.endata.cn/enlib-api/api/home/getrank_mainland.do'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
}

data = {
    'r': 0.03378353702444792,
    'top': 50,
    'type': 0
}

response = requests.post(url, data=data, headers=headers)
print(response.text)



