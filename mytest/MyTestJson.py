import json
json={
  "code" : 0,
  "message" : "SUCCESS",
  "value" : {
    "loginName" : "13671388253",
    "mobile" : "13671388253",
    "realName" : "孟祥山",
    "email" : "850512700@qq.com",
    "sex" : 1,
    "age" : 18,
    "userStatus" : 1,
    "isTeacher" : 1,
    "isAdmin" : 2,
    "roleId" : 4,
    "teacherId" : 379,
    "menus" : [ ],
    "menuTrees" : [ ],
    "campus" : [ ],
    "token" : "eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIxNjIiLCJzdWIiOiLlrZ_npaXlsbEiLCJpYXQiOjE1NzQzOTM1MTEsImV4cCI6MTU3NDQ3OTkxMX0.DhjggNJkVxNsb-T1-Y5cf-SeQjDZdoBSJL2lQEY0vNs",
    "sysUserId" : 162
  }
}
code=json.get("code")
print(code)
token=json.get("value").get("token")
userId=json().get("value").get("sysUserId")
print(token)
print(userId)