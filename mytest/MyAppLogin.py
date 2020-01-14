import requests
url="http://pyapitest.lexue.com/user/user/login"
payload = {"mobile": "13671388253", "password": "123456","deviceId":"869633047841059"}
headers = {"Accept-Language": "zh-CN,zh;q=0.8","appKey":"201820011141153","version": "Android","os": "3.1.0","Content-Type":"application/x-www-form-urlencoded","signature": "0E0D02F513929767CEC819D85A7D1B325F2B647B"}
r = requests.post(url, headers=headers, data=payload)

print(r.text)
cityId=r.json().get("value").get("current").get("cityId")
print(cityId)
userId=r.json().get("value").get("current").get("userId")
print(type(userId))
print(userId)
token=r.json().get("value").get("token")
print(token)