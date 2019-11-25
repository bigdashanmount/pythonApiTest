import requests
url="http://pycmstest.lexue.com/basic/campusRegion/listCampusRegion"
params = {"id": "0", "selectId": "0"}
print(type(params))
headers = {'appKey': '201820011141153',
           'isAdmin': '2',
           'signature': '2549059CB2A1A7D855940251D05003960A4EEB7B',
           'token': 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIyNzAxIiwic3ViIjoi5a2f56Wl5bGxIiwiaWF0IjoxNTc0NDE5MzA5LCJleHAiOjE1NzQ1MDU3MDl9._dG2AxxYKxTf1XLzonLSojLljnvHWBQFpp6I2_7FzVc',
           'userId': '2701'}
r = requests.get(url, params=params,headers=headers)

print(r.text)