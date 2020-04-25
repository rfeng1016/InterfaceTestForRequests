import requests

#携程网上传个人图片
url = "https://www.ctrip.com/MyInfo/Ajax/UploadPhoto.ashx"

#文件参数的名字：uploadFile_852
#文件名：XXXX.jpg
#打包本地的一个文件：open('图片的路径','rb')
#文件的格式：image/jpeg
files = {
    'uploadFile_852':('XXXX.jpg',open('图片的路径','rb'),'image/jpeg')
}


r = requests.post(url=url,files=files,verify=False)
print(r.text)



