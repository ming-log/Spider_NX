# 乌海市公共资源交易中心  http://www.whggzy.com/
# 路径搜索/front/search/category，XHR断点查看真正的数据加载方式

import requests

url = 'http://www.whggzy.com/front/search/category'

headers = {
    "Accept": "*/*",
    "Content-Type": "application/json",
    "X-Requested-With": "XMLHttpRequest",
    "Referer": "http://www.whggzy.com/PoliciesAndRegulations/index.html?utm=sites_group_front.2ef5001f.0.0.ea6f6640d5cb11ed9547cf4018e15eea",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}

data = '{"utm":"sites_group_front.2ef5001f.0.0.ea6f6640d5cb11ed9547cf4018e15eea","categoryCode":"GovernmentProcurement","pageSize":15,"pageNo":1}'

response = requests.post(url, headers=headers, data=data)

print(response.text)

