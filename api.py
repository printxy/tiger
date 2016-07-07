import requests
import json
import os
import shutil 



url = 'http://apis.baidu.com/txapi/mvtp/meinv'
headers = {'apikey':'0a43040abc9e1362b6d49d86472f0525'}
params = {'num':'30'}

r = requests.get(url,params = params,headers=headers)
r = r.json()

def saveImage(imgUrl,imgName= 'default.jpg'):
	response = requests.get(imgUrl,stream = True)
	image = response.content
	path = imgName
	print ('save the file:'+path)
	with open(path,'wb') as img:
		img.write(image)
	img.close()
	doc = [x for x in os.listdir('/Users/shengrenfengcai/Desktop') if os.path.isfile(x) and os.path.splitext(x)[1]=='.jpg']
	for files in doc:
		sourceFile = os.path.join('/Users/shengrenfengcai/Desktop',files) 
		shutil.move(sourceFile,'Users/shengrenfengcai/Desktop/美女照片')

		
	
def run():
	for line in r['newslist']:
   		title = line['title']
   		picUrl = line['picUrl']
   		saveImage(picUrl,imgName=title+'.jpg')
run()