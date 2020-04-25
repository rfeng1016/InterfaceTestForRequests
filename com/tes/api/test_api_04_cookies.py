import requests

url="http://192.168.123.1/fanwe"
data = {
    'AAAA':'AAAA',
    'BBBB':'BBBB',
    'cccc':'cccc',
    'dddd':''
}
cookies = {
    'EEEE':'EEEEEEEEEEE'
}
r = requests.post(url=url,data=data,cookies=cookies)
print(r.encoding)
#先把返回的结果转换为UTF-8，再去解码成中文的编码
print(r.text.encode('utf-8').decode('unicode_escape'))