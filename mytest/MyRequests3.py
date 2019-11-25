import requests
payload = {
    "key1":"value1",
    "key2":"value2"
}
response = requests.post("http://httpbin.org/post",data = payload)
print(response.text)
payload = (("key1","value1"),("key1","value2"))
response = requests.post("http://httpbin.org/post",data = payload)
print(response.text)