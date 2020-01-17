# coding:utf-8
cars = {'BMW': 8.5, 'BENS': 8.3, 'AUDI': 7.9}
print(type(cars))
# 对存在的key-value对赋值，改变key-value对
cars['BENS'] = 4.3
cars['AUDI'] = 3.8
print(cars) # {'BMW': 8.5, 'BENS': 4.3, 'AUDI': 3.8}