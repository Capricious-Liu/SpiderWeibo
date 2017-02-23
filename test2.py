import re
import urllib
import urllib.request
import gzip


def ungzip(data):
    try:
        print('正在解压......')
        data=gzip.decompress(data)
        print('解压完毕！')
    except:
        print('未经压缩，无需解压')
    return data

def getXSRF(data):
    cer=re.compile('name=\"_xsrf\" value=\"(.*)\"', flags = 0)

url='http://www.zhihu.com'
urlop=urllib.request.urlopen(url)

data=urlop.read().decode('utf-8')
print(data)