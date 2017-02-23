import requests
from bs4 import BeautifulSoup


def setCookie():
    f = open(r'cookie.txt', 'r')  # 打开所保存的cookies内容文件
    cookies = {}  # 初始化cookies字典变量
    for line in f.read().split(';'):  # 按照字符：进行划分读取
        # 其设置为1就会把字符串拆分成2份
        name, value = line.strip().split('=', 1)
        cookies[name] = value  # 为字典cookies添加内容
    return cookies

cookieUsing = setCookie()
res = requests.get("http://weibo.cn/", cookies=cookieUsing)
soup = BeautifulSoup(res.text)

print(res.text)