import requests

#淘宝查询手机号码归属地接口

'''
接口的URL地址：http://tcc.taobao.com/cc/json/mobile_tel_segmengt.html
接口的请求参数：tel
接口的请求方式：get
'''

#定义一个变量
#url = "http://tcc.taobao.com/cc/json/mobile_tel_segmengt.html"

#get请求，请求数据，二种方式：

#一种：请求参数保存URL地址里面，？后面添加"参数名和参数值"，如果多个值，用&连接
url_1 = "http://tcc.taobao.com/cc/json/mobile_tel_segmengt.htm?tel=18319011906"
r_1 = requests.get(url=url_1)
print(r_1.text)           #打印返回的正文
print(r_1.status_code)    #打印返回的状态码
print(r_1.cookies)        #打印返回的cookies
print(r_1.url)            #URL值


#另一种：参数保存在params中，使用字典格式进行保存
url_2 = "http://tcc.taobao.com/cc/json/mobile_tel_segmengt.htm"
params = {
    "tel" : 183190111906
}
r_2 = requests.get(url=url_2,params=params)
print(r_2.text)           #打印返回的正文
print(r_2.status_code)    #打印返回的状态码
print(r_2.cookies)        #打印返回的cookies
print(r_2.url)            #URL值