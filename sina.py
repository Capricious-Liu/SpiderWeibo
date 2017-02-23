import requests
from bs4 import BeautifulSoup


def setCookie():
    f = open(r'C:\Users\liuzhili\Desktop\cookie.txt', 'r')  # 打开所保存的cookies内容文件
    cookies = {}  # 初始化cookies字典变量
    for line in f.read().split(';'):  # 按照字符：进行划分读取
        # 其设置为1就会把字符串拆分成2份
        name, value = line.strip().split('=', 1)
        cookies[name] = value  # 为字典cookies添加内容
    return cookies

def initParam(keyword,page):
    # keywordCoded=
    param={'hideSearchFrame': '',
           'keyword': keyword,
           'advancedfilter': '1',
           'endtime': '20170223',
           'sort': 'time',
           'page': str(page)}
    return param


cookieUsing = setCookie()
page = 1
while page < 51:
    paramsUsing = initParam('交通', page)
    res = requests.get("http://weibo.cn/search/mblog", cookies=cookieUsing, params=paramsUsing)


    soup = BeautifulSoup(res.text)

    print(soup.body.text)
    page += 1
