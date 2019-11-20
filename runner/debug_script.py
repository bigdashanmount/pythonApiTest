# coding:utf-8

import requests
import urllib3


urllib3.disable_warnings()

url = "https://gkapisdev.lexue.com/cart/v1/add"
headers = {'did': '7F42B8F7AC6E4AFEBEEFC6E1C5B37BEE',
           'grade': '3',
           'OS': 'iPhone',
           'client': 'SENIOR_TEACH',
           'version': '3.2.3',
           'lgtk': '+RCFfw4G09fjnUrVigWnkLH27oRz6dIPy82SCNHLLgIy/Xbqcj+1XjoX7rMTMMFtv69/PeYKGGhz7LeBRCGP3utB5ctxVCes'}
params = "activityId=-1&productId=74100000"
res = requests.get(url=url, headers=headers, params=params, verify=False)
print(res.text)

