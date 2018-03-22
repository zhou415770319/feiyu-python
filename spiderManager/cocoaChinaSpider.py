# -*- coding: utf-8 -*-

import json
from bs4 import BeautifulSoup
import re
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


    return json.dumps(result)
