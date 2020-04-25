import requests


#headers发送请求，这个参数不是每个接口都必须参加，都是开发自定义


#不需要添加headers，前程无忧搜索职位接口
url_51job='https://search.51job.com/list'
r_51job = requests.get(url=url_51job)
print(r_51job.text)         #第一次打印返回的中文为乱码
print(r_51job.encoding)     #打印返回html界面的编码方式，html默认的编码方式：ISO-8859-1
r_51job.encoding='gb2312'   #修改返回的编码方式
print(r_51job.text)         #第二次打印返回的文本

#需要添加headers，12306查询车票需要添加参数headers
url_12306='https://kyfw.12306.cn/otn/leftTicket/query'
headers={
    'cookie':'XXXXXXXXXXXXXXXXXXXXXX'
}
r_12306 = requests.get(url=url_12306,headers=headers)
print(r_12306.text)

























