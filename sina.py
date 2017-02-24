import requests
from bs4 import BeautifulSoup


def setCookie():
    f = open(r'C:\Users\liuzhili\Desktop\SpiderNeeded\cookie.txt', 'r')  # 打开所保存的cookies内容文件
    cookies = {}  # 初始化cookies字典变量
    for line in f.read().split(';'):  # 按照字符：进行划分读取
        # 其设置为1就会把字符串拆分成2份
        name, value = line.strip().split('=', 1)
        cookies[name] = value  # 为字典cookies添加内容
    return cookies

def initParam(keyword,page):
    param={'hideSearchFrame': '',
           'keyword': keyword,
           'advancedfilter': '1',
           'endtime': '20170223',
           'sort': 'time',
           'page': str(page)}
    return param

def saveFile(data):
    save_path = r'C:\Users\liuzhili\Desktop\SpiderNeeded\output.txt'
    f_obj = open(save_path, 'wb')
    f_obj.write(data)
    f_obj.close()

def readFile():
    read_path = r'C:\Users\liuzhili\Desktop\SpiderNeeded\output.txt'
    f_obj = open(read_path, 'rb')
    ans = f_obj.read()
    return ans

def printList(list_all):
    for small_list in list_all:
        for key, value in small_list.items():
            print("key:  " + key + "    value:   " + value + '/n')

cookieUsing = setCookie()
# page = 1
# while page < 2:
    # paramsUsing = initParam('交通', page)
    # res = requests.get("http://weibo.cn/search/mblog", cookies=cookieUsing, params=paramsUsing)
    # soup = BeautifulSoup(res.text)
    # saveFile(soup.encode('UTF-8'))

    # page += 1
file = readFile().decode('UTF-8')

soup = BeautifulSoup(str(file), "html.parser")

list_all = []
for item in soup.findAll('div', attrs={"class": "c", 'id': True}):
    # print(item)
    list_single = {}
    user_name = item.find('a').string
    blog_context = ""

    whole = False
    for inner_item in item.find('span').findAll('a'):
        if inner_item.string == "全文":
            whole_blog_url = requests.get("http://weibo.cn" + inner_item['href'], cookies=cookieUsing)
            # print("Coming in")
            inner_soup = BeautifulSoup(whole_blog_url.text, "html.parser")
            inner_inner_item = inner_soup.find('div', attrs={'class': "c", 'id': "M_"}).find('span')
            whole = True
            blog_context += str(inner_inner_item)
    if not whole:
        blog_context += str(item.find('span'))

    list_single['blog'] = blog_context
    list_single['name'] = user_name

    list_all.append(list_single)
printList(list_all)
