# -*- coding: utf-8 -*-

import json
from bs4 import BeautifulSoup
import re
from . import manager
def getScrollImg(html):

    soup = BeautifulSoup(html, 'html.parser')
    content = soup.find('div', class_='forum-c')
    arr = content.find_all('li')
    infos = []
    for li in arr:
        url = li.a['href']
        imgUrl = li.img['src']
        title = li.div.h4.string
        des = li.div.p.string
        dict = {'title': title, 'des': des, 'url': url, 'imgUrl': imgUrl}
        infos.append(dict)
    # print infos

    return json.dumps(infos)


def getHomeData(html):
    baseUrl = 'http://www.cocoachina.com'
    result = {}
    soup = BeautifulSoup(html, 'html.parser')
    # navis
    content = soup.find('div', class_='nav-list')
    arr = content.find_all('li')
    infos = []
    for li in arr:
        temUrl = li.a['href']
        matchObj = re.match('http://', temUrl)
        if matchObj:
            print("have http!!")
            url = temUrl
        else:
            url = baseUrl + temUrl
        title = li.a.string
        dict = {'title': title,'url': url}
        infos.append(dict)
    if not infos:
        result = manager.addCode(result,False)
        return  json.dumps(result)
    result['mainNavis'] = infos
    # print infos

    # subNavis

    content = soup.find('div', class_='nav-header-bottom')
    arr = content.find_all('li')
    infos = []
    for li in arr:
        url = baseUrl + li.a['href']
        title = li.a.string
        dict = {'title': title,'url': url}
        infos.append(dict)
    result['subNavis'] = infos
    if not infos:
        result = manager.addCode(result,False)
        return  json.dumps(result)
    tem = {}
    tem['data'] = result
    tem = manager.addCode(tem,True)

    return json.dumps(tem)

def getIosListData(html):
    baseUrl = 'http://www.cocoachina.com'
    result = {}
    soup = BeautifulSoup(html, 'html.parser')
    # navis
    content = soup.find('div', class_='leftSide')
    arr = content.find_all('li')
    print('arr+++++'+str(arr))
    infos = []
    for li in arr:
        temUrl = li.a['href']
        matchObj = re.match('http://', temUrl)
        if matchObj:
            print("have http!!")
            url = temUrl
        else:
            url = baseUrl + temUrl
        title = li.a.string
        imgurl = li.img['src']
        dict = {'title': title,'url': url,'imgurl':imgurl}
        infos.append(dict)
    if not infos:
        result = manager.addCode(result,False)
        return  json.dumps(result)
    result['mainNavis'] = infos
    # print infos

    # subNavis

    content = soup.find('div', class_='nav-header-bottom')
    arr = content.find_all('li')
    infos = []
    for li in arr:
        url = baseUrl + li.a['href']
        title = li.a.string
        dict = {'title': title,'url': url}
        infos.append(dict)
    result['subNavis'] = infos
    if not infos:
        result = manager.addCode(result,False)
        return  json.dumps(result)
    tem = {}
    tem['data'] = result
    tem = manager.addCode(tem,True)

    return json.dumps(tem)