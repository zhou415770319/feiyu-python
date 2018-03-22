# -*- coding: utf-8 -*-
import json
import re

from bs4 import BeautifulSoup


def getZHYSNavis(html):
    soup = BeautifulSoup(html, 'html.parser')

    allmenu = soup.find('div', class_='allmenu')
    navArr = allmenu.find_all('dl')
    typeNavis = []
    for navi in navArr:
        title = navi.find('dt').a.string
        print(title)
        url = navi.find('dt').a['href']
        subnavis = navi.find('dd')

        arr = subNavi(subnavis)

        dict = {'title': title, 'url': url, 'subNavis': arr}

        typeNavis.append(dict)

    str = json.dumps(typeNavis)
    return str

def subNavi (content):
    list = []
    arr = content.find_all('a')
    # print arr[1]

    for subnavi in arr:
        title = subnavi.string
        url = subnavi['href']
        dict = {'title': title, 'url': url}
        list.append(dict)
    return list

# 未完成功能
# def getZHYSTypeInfo(html):
#     soup = BeautifulSoup(html, 'html.parser')
#
#     allmenuContent = soup.find('div',class_ ='ip3')
#
#     allmenu = soup.find_all('div',class_ = re.compile("icate"))
#
#     typeInfos = []
#     for typeInfo in allmenu:
#         # typeI = BeautifulSoup(typeInfo)
#         title = typeInfo.find('div',class_ = 'tit').h3.string
#         url = typeInfo.find('a',class_ = 'more')
#         str = typeInfo.span
#
#         dict = {'title': title ,'url':url }
#         typeInfos.append(dict)
#
#     print allmenuContent
#     return json.dumps(['zh', 'fei'])


def getZHYSItems(html):
    soup = BeautifulSoup(html,'html.parser')
    content = soup.find('ul' ,class_ = 'newslists')
    items = content.find_all('li')
    zhysItems = []
    for item in items:
        image = item.img['src']
        url = item.h5.a['href']
        title = item.h5.string
        des = item.p.string
        time = item.span.string

        dict = {'image':image,'url':url,'title':title,'des':des,'time':time}
        zhysItems.append(dict)

    # print zhysItems

    return json.dumps(zhysItems)