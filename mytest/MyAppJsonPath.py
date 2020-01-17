# coding:utf-8
import jsonpath
import jsonpath
import json

d = {
	"code": 0,
	"message": "SUCCESS",
	"value": {
		"studentName": "dds",
		"sex": 2,
		"headPic": "http://picspy.lexue.com/student-girl-default-picture-20190730092736.jpg",
		"cityId": 110100,
		"cityName": "北京市",
		"gradeId": 26,
		"currentSchool": "丰台五一学校",
		"studentId": 1706
	}
}
result=jsonpath.jsonpath(d,"$..studentId") #模糊匹配
# result=jsonpath.jsonpath(d,'$.stu_info') #取到stu_info这里的所有内容
# result = jsonpath.jsonpath(d, '$.stu_info[0]') #取到stu_info里的第1个元素
# result = jsonpath.jsonpath(d, '$.stu_info[0].id')  # 取到stu_info里的第1个元素中的id
print(result)
d=json.dumps(d)
