#coding=utf-8
from urllib import request 
import re

def getHtml(url):
    page = request.urlopen(url)
    html = page.read()
    html=html.decode('utf-8')
    return html

def getImg(html):
    reg = r'src="(.+?\.png)" alt'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    for imgurl in imglist:
    	request.urlretrieve(imgurl, imgurl.split("/")[-1])

html = getHtml("https://www.cnblogs.com/fnng/p/3576154.html")
img = getImg(html)