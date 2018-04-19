#coding:utf-8

from . import tool
from . import ZHYSSpider
from . import cocoaChinaSpider


def spiderZHYSNavis():
    url = 'http://www.cnys.com'

    html = tool.getHtml(url)

    navis = ZHYSSpider.getZHYSNavis(html)
    return navis
    # tool.writeFile(navis,'zhysNavis.json')

# def spiderZHYSTypeInfo():
#     html = tool.getHtml('http://www.cnys.com')
#
#     typeInfo = ZHYSSpider.getZHYSTypeInfo(html)
#     return typeInfo

def spiderCocoaChinaScrollImage():
    url = 'http://www.cocoachina.com'

    html = tool.getHtml(url)

    scrollImages = cocoaChinaSpider.getScrollImg(html)
    return scrollImages

def spiderCocoaChinaHomeData():
    url = 'http://www.cocoachina.com'

    html = tool.getHtml(url)

    homeData = cocoaChinaSpider.getHomeData(html)
    return homeData

# 抓取中华养生网的导航
# spiderZHYSNavis()


def spiderZHYSContentItem(url):
    html = tool.getHtml(url)

    items = ZHYSSpider.getZHYSItems(html)
    return items
    # tool.writeFile(items, 'zhysitems.json')

# spiderZHYSContentItem('http://www.cnys.com/zixun/')

# 未完成
# spiderZHYSTypeInfo()

# 抓取cocoa China 滚动图
# spiderCocoaChinaScrollImage()

# print navis


def spiderZHYSHomeInfo(url):

    return ZHYSSpider.getZHYSHomeInfo(tool.getHtml(url))


def addCode(result,isSuccusess):
    if isSuccusess:
        result['code'] = 200
        result['codemsg'] = "请求成功！"
    else:
        result['code'] = 444
        result['codemsg'] = "请求失败！"
    return result