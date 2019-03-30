#coding:utf-8

from . import tool
from . import ZHYSSpider
from . import cocoaChinaSpider
from bs4 import BeautifulSoup


def spiderWithUrl(url,res):
    message = "正则规则必填"
    html = tool.getHtml(url)
    soup = BeautifulSoup(html, 'html.parser')
    # print(soup)

    if len(res):
        print(res)
        content = soup
        result = ''
        for index in range(len(res)):
            print(index)
            re = res[index]
            if index+1 == len(res):
                result = findOrFindall(content,re)
            else:
                content = findOrFindall(content,re)
        print(result)


def findOrFindall(content,re):
    if re['type'] == 'find':
        print('find+' + str(re))

        return getContentFromHtml(content, re['re'])

    elif re['type'] == 'findall':
        print('findall+' + str(re))
        return getContentsFromHtml(content, re['re'])
    else:
        return "正则错误" + str(re)

def getContentFromHtml(content,re):
    message = "正则规则必填"
    if re:
        return content.find(re['name'], class_=re['class'])



def getContentsFromHtml(content,re):
    message = "正则规则必填"
    if re:
        arr = content.find_all(re['name'])
        print(re['attrs'])
        results = []
        #获取单个元素
        for item in arr:
            # print(item)
            result = getResultWithAttrs(item,re['attrs'])
            results.append(result)

        print('results+++++++'+ str(results))

        return results

#根据attrs 获取爬取的内容
def getResultWithAttrs(content,attrs):
    try:
        #结果
        result = {}
        for attr in attrs:
            try:
                if attr['type'] == 'find':
                    print('find+' + str(attr))

                    return getContentFromHtml(content, attr['re'])
                elif attr['type'] == 'findall':
                    print('findall+' + str(attr))
                    return getContentsFromHtml(content, attr['re'])
                else:
                    nametypes = attr['nametypes']
                    print('nametypes+++++' + str(nametypes))
                    #
                    tem = BeautifulSoup("", 'html.parser')
                    # 拼接规则
                    for nametype in nametypes:
                        #h5标签转换
                        if nametype == 'a':
                            tem = content.a
                        elif nametype == 'img':
                            tem = content.img
                        elif nametype == 'p':
                            tem = content.p
                        elif nametype == 'span':
                            tem = content.span
                        else:
                            tem = content.str(nametype)
                        print('tem' + str(tem))

                    # 获取属性值
                    temattr = attr['attr']
                    if temattr == 'string':
                        tem = tem.string
                    else:
                        tem = tem[str(temattr)]
                    key = attr['content']
                    print('key++++++' + key)

                    result[key] = tem
                    print('title++++++' + str(tem))
            except:
                print('抓取失败' +str(attr))


        return result
    except:
        print('抓取失败')
        return '抓取失败'

def spiderZHYSNavis():
    url = 'http://www.zhys.com'

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

def spiderCocoaChinaIosListData():
    url = 'http://www.cocoachina.com/ios/list_69_1.html'

    html = tool.getHtml(url)

    homeData = cocoaChinaSpider.getIosListData(html)
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