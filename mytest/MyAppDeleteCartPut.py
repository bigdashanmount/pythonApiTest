import requests
url="http://pyapitest.lexue.com/order/cart/deleteCart"
payload = {"cartIds": "3731", "userId": "1410"}
headers = {"Accept-Language": "zh-CN,zh;q=0.8","appKey":"201820011141153","version": "Android","os": "3.1.0","Content-Type":"application/x-www-form-urlencoded","signature": "6C27AED46B4AA68B006539B99C278A6A7873DE8E"}
r = requests.put(url, headers=headers, data=payload)

print(r.text)