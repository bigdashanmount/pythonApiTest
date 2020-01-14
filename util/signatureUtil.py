import hmac 
import csv
import pymysql
from hashlib import sha1

class Signature:

	def hash_mac(self,appSecret,string_dict,sha1):
		hmac_code = hmac.new(appSecret.encode(),string_dict.encode(),sha1)
		return hmac_code.hexdigest()

	def hmac_string(self,string_dict):
		# set appSecret
		appSecret = "661ee319dff061d4fb6532787f7b6wgl";
		str3 = self.hash_mac(appSecret, string_dict, sha1)
		return str3

	def get_string(self,dict1):
		string_dict = ""
		if dict1 != {}:
			sorted_list = sorted(dict1.items(),key = lambda d:d[0])
			# print(sorted_list)
			for i in iter(sorted_list):
				str1 = i[0] + "=" + i[1] + "&" 
				string_dict += str1
				#print(string_dict)
			print(string_dict[0:-1])	
		return string_dict[0:-1]	

	# dict1--传入字典

	def get_signature(self,dict1):
		if dict1==None:
			signature = "79E48482F30ED5CA96DCBB4DFA43D1576DBC2B74"
			return signature
		string_dict = self.get_string(dict1)
		signature = self.hmac_string(string_dict).upper()
		return signature
if __name__ =="__main__":
	testSignature = Signature()
	#dict={"loginName":"13671388253","password":"388253"}
	#dict={"mobile": "13671388253", "password": "123456","deviceId":"869633047841059"}
	#print(type(dict))
	#dict = {"cityId": "110100", "gradeName": "五年级"}
	dict ={"cartIds": "3731", "userId": "1410"}
	Signature=testSignature.get_signature(dict)
	print(Signature)
