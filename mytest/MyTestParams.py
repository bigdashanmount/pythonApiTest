# coding:utf-8
params = "cityId=110100&gradeName=五年级"
dict_params={"cityId":"110100","gardeName":"五年级","userId":"999"}
#print(type(dict_params))
global global_str_params
global_str_params=""
for key in dict_params:
  params_key_value=key + "=" + dict_params[key]
  print(params_key_value)
  global_str_params += params_key_value + "&"
  
print(global_str_params[0:(len(global_str_params)-1)])
