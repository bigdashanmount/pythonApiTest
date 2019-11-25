import requests
url="http://pycmstsl.lexue.com/system/sysUser/login"
payload = {"loginName": "13671388253", "password": "388253"}
headers = {
           "appKey": "201820011141153",
           "Content-Type":"application/x-www-form-urlencoded",
           "signature": "1119E9D5C9468DD944A9F96E61D7365B3F47D5A4"}
r = requests.post(url, headers=headers, data=payload)

print(r.text)