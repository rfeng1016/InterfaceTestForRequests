import requests

#携程网
url = "https://www.ctrip.com/"


#发送请求时候忽略证书，证书的参数verify，参数默认为True
r_1 = requests.get(url=url,verify=False)
print(r_1.text)


#verify添加证书的路径
r_2 = requests.get(url=url,verify='证书的路径')
print(r_1.text)