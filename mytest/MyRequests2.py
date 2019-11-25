import requests
r = requests.get("https://api.github.com/events")
print(r)                # <Response [200]>
print(type(r))          # <class 'requests.models.Response'>
print(r.status_code)    # 200
response1 = requests.get("http://httpbin.org/get?key1=value1")
print(response1.url)
#http://httpbin.org/get?key1=value1
parameter = {
            "key1":"value1",
            "key2":"value2"
            }
response2 = requests.get("http://httpbin.org/get",params = parameter)
print(response2.url)
# http://httpbin.org/get?key1=value1&key2=value
parameter = {
            "key1":"value1",
            "key2":["value21","value22"]
}
response3 = requests.get("http://httpbin.org/get",params = parameter)
print(response3.url)
# http://httpbin.org/get?key1=value1&key2=value21&key2=value22
parameter = {
            "key1":"value",
            "key2":None
}
response4 = requests.get("http://httpbin.org/get",params = parameter)
print(response4.url)    #http://httpbin.org/get?key1=value
response = requests.get("https://api.github.com/events")
print(response)         # <Response [200]>
# print(response.text)  # Json格式
import requests

new_headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36"
}

response = requests.get("https://www.zhihu.com",headers = new_headers)
print(response.text)