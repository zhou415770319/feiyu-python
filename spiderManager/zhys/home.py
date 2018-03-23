# -*- coding: utf-8 -*-
import json
import re

from bs4 import BeautifulSoup


def getCenterList(soup):
    content = soup.find('div', class_='center')
    items = content.find_all('li')
    temItems = []
    for item in items:
        image = item.img['src']
        url = item.a['href']
        title = item.a['title']
        dict = {'image': image, 'url': url, 'title': title}
        temItems.append(dict)
    return temItems


def getShipuList(soup):
    content = soup.find('div', class_='ishipu')
    items = content.find_all('li')
    temItems = []
    for item in items:
        image = item.img['src']
        url = item.a['href']
        title = item.b.string
        dict = {'image': image, 'url': url, 'title': title}
        temItems.append(dict)
    return temItems


def getLatestList(soup):
    content = soup.find('div', class_='right')
    items = content.find_all('li')
    temItems = []
    for item in items:
        url = item.a['href']
        title = item.a['title']
        dict = {'url': url, 'title': title}
        temItems.append(dict)
    return temItems