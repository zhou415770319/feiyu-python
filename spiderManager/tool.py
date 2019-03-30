# -*- coding: utf-8 -*-
import urllib
# from urllib import parse
from urllib import request

def getHtml(url):

    url_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    referer = 'http://www.feiyu.com/'
    postdata = {'username': 'qwe', 'password': 'qwe123'

                }
    # header = {'User-Agent': url_agent,'Referer': referer}
    # info 需要被编码成urllib 能理解的格式
    # data = parse.urlencode(postdata)
    req = request.Request(url)
    req.add_header('User-Agent', url_agent)
    # req.add_header('Referer', referer)
    # req.data = data
    response = request.urlopen(req)
    html = response.read()
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

def writeFile (jsonStr, fileName):
    f = open('files/'+fileName, 'w')
    f.write(jsonStr)
    f.closed

