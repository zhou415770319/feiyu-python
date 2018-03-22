# -*- coding: utf-8 -*-

import urllib.request

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

def writeFile (jsonStr, fileName):
    f = open('files/'+fileName, 'w')
    f.write(jsonStr)
    f.closed

