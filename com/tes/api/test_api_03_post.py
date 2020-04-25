import requests


#requests发送post请求，有两种请求数据格式
#一种数据格式：from-data，表单格式
#二种数据格式：json格式

'''
案例：
1、注册接口，数据格式是data格式
URL地址：http://106.12.126.197:8080/register
请求方式：post请求
请求参数：username password
2、登录接口，数据格式是json格式
URL地址：http://106.12.126.197:8080/login
请求方式：post请求
请求参数：username password
'''


#注册接口
url_reg="http://106.12.126.197:8080/register"
#表单数据格式，参数data，数据都是字典去保存
data = {
    "username":"jrApp",
    "password":"jrApp123"
}
#发送请求，表单格式的数据，用data
r_reg = requests.post(url=url_reg,data=data)
print(r_reg.text)           #打印返回的正文
print(r_reg.status_code)    #打印返回的状态码
print(r_reg.cookies)        #打印返回的cookies
print(r_reg.url)            #URL值


#登录接口
url_login="http://106.12.126.197:8080/login"
#json数据格式，定义值，也是字典去保存
json = {
    "username":"jrApp",
    "password":"jrApp123"
}
#发送请求，表单格式的数据，用data
r_login = requests.post(url=url_login,json=json)
print(r_login.text)           #打印返回的正文
print(r_login.status_code)    #打印返回的状态码
print(r_login.cookies)        #打印返回的cookies
print(r_login.url)            #URL值