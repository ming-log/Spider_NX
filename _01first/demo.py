# 乌海市公共资源交易中心  http://www.whggzy.com/
# 路径搜索/front/search/category，XHR断点查看真正的数据加载方式

import requests

url = 'http://www.whggzy.com/front/search/category'

headers = {
    "Accept": "*/*",
    "Content-Type": "application/json",
    "X-Requested-With": "XMLHttpRequest",
}

data = '{"utm":"sites_group_front.188479ff.0.0.48148460d60811ed992ee5ef25d2e7eb","categoryCode":"GovernmentProcurement","pageSize":15,"pageNo":1}'
response = requests.post(url, headers=headers, data=data)

print(response.text)
