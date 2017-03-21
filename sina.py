import requests
import xlwt
from bs4 import BeautifulSoup


def setCookie():
    f = open(r'C:\Users\liuzhili\Desktop\SpiderNeeded\cookie.txt', 'r')  # 打开所保存的cookies内容文件
    cookies = {}  # 初始化cookies字典变量
    for line in f.read().split(';'):  # 按照字符：进行划分读取
        # 其设置为1就会把字符串拆分成2份
        name, value = line.strip().split('=', 1)
        cookies[name] = value  # 为字典cookies添加内容
    return cookies

def initParam(keyword, page):
    param = {'hideSearchFrame': '',
           'keyword': keyword,
           'advancedfilter': '1',
           'hasori':'1',
           'starttime':'20170311',
           'endtime': '20170320',
           'sort': 'time',
           'page': str(page)}
    return param

def saveFile(data, page):
    save_path = r'C:\Users\liuzhili\Desktop\SpiderNeeded\output'+str(page)+'.txt'
    f_obj = open(save_path, 'wb')
    f_obj.write(data)
    f_obj.close()

def readFile(page):
    read_path = r'C:\Users\liuzhili\Desktop\SpiderNeeded\output'+str(page)+'.txt'
    f_obj = open(read_path, 'rb')
    ans = f_obj.read()
    f_obj.close()
    return ans

def printList(list_all):
    for small_list in list_all:
        for key, value in small_list.items():
            print("key:  " + key + "    value:   " + value + '/n')

def outputList2Excel(list_all):
    workbook = xlwt.Workbook()
    sheet1 = workbook.add_sheet('sheet1', cell_overwrite_ok=True)
    i = 1
    for small_list in list_all:
        sheet1.write(i, 1, small_list['name'])
        sheet1.write(i, 2, small_list['blog'])
        i += 1
    workbook.save(r'C:\Users\liuzhili\Desktop\SpiderNeeded\output.xls')

def searchKeyword(context,district):
    for key in district.keys():
        if context.find(key) != -1:
            district[key] += 1

def printDistrict(district):
    for key, value in district.items():
        print(key+'    '+str(value))

def crawlWebsite(cookieUsing, page_max = 30):
    keyword = input("Please input your keyword:")
    collect_page = 1
    while collect_page <= page_max:
        paramsUsing = initParam(keyword, collect_page)
        res = requests.get("http://weibo.cn/search/mblog", cookies=cookieUsing, params=paramsUsing)
        soup = BeautifulSoup(res.text, "html.parser")
        saveFile(soup.encode('UTF-8'), collect_page)
        collect_page += 1

def SaveWebsite2Excel(page_max = 30):
    page = 1
    list_all = []
    while page <= page_max:
        file = readFile(page).decode('UTF-8')
        soup = BeautifulSoup(str(file), "html.parser")

        for item in soup.findAll('div', attrs={"class": "c", 'id': True}):
            list_single = {}
            user_name = item.find('a').string
            blog_context = ""

            whole = False
            for inner_item in item.find('span').findAll('a'):
                if inner_item.string == "全文":
                    whole_blog_url = requests.get("http://weibo.cn" + inner_item['href'], cookies=cookieUsing)
                    inner_soup = BeautifulSoup(whole_blog_url.text, "html.parser")
                    try:
                        inner_inner_item = inner_soup.find('div', attrs={'class': "c", 'id': "M_"}).find('span')
                        whole = True
                    except:
                        whole = False
                        continue

                    blog_context += inner_inner_item.get_text()

            if not whole:
                blog_context += item.find('span').get_text()
                # Here is the right choice!! Should remember

            list_single['blog'] = blog_context
            list_single['name'] = user_name

            list_all.append(list_single)
        page += 1
        print('page'+str(page)+'ok')
    outputList2Excel(list_all)

def CalculateAccidentsInDistrixt(district, page_max = 30):
    page = 1
    while page < page_max:
        file = readFile(page).decode('UTF-8')
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
                    inner_soup = BeautifulSoup(whole_blog_url.text, "html.parser")
                    inner_inner_item = inner_soup.find('div', attrs={'class': "c", 'id': "M_"}).find('span')
                    whole = True
                    blog_context += str(inner_inner_item)
            if not whole:
                blog_context += str(item.find('span'))

            list_single['blog'] = blog_context
            list_single['name'] = user_name

            list_all.append(list_single)
            searchKeyword(blog_context, district)
        page += 1
    printDistrict(district)


cookieUsing = setCookie()
district = {'闵行':0,
            '黄浦':0,
            '徐汇':0,
            '长宁':0,
            '静安':0,
            '普陀':0,
            '虹口':0,
            '杨浦':0,
            '宝山':0,
            '嘉定':0,
            '浦东':0,
            '金山':0,
            '松江':0,
            '青浦':0,
            '奉贤':0 }

print("1. Crawl the Website\n"
      "2. Save output in Excel\n"
      "3. Process outputs, Calculate Accidents!\n")

option = input("Please input your option")

if option == '1':
    crawlWebsite(cookieUsing, 100)
elif option == '2':
    SaveWebsite2Excel(100)
elif option == '3':
    CalculateAccidentsInDistrixt(district, 4)


#
#
# page = 1
# while page < 60:
#     file = readFile(page).decode('UTF-8')
#     soup = BeautifulSoup(str(file), "html.parser")
#
#     list_all = []
#     for item in soup.findAll('div', attrs={"class": "c", 'id': True}):
#         # print(item)
#         list_single = {}
#         user_name = item.find('a').string
#         blog_context = ""
#
#         whole = False
#         for inner_item in item.find('span').findAll('a'):
#             if inner_item.string == "全文":
#                 whole_blog_url = requests.get("http://weibo.cn" + inner_item['href'], cookies=cookieUsing)
#                 # print("Coming in")
#                 inner_soup = BeautifulSoup(whole_blog_url.text, "html.parser")
#                 inner_inner_item = inner_soup.find('div', attrs={'class': "c", 'id': "M_"}).find('span')
#                 whole = True
#                 blog_context += str(inner_inner_item)
#         if not whole:
#             blog_context += str(item.find('span'))
#
#         list_single['blog'] = blog_context
#         list_single['name'] = user_name
#
#         list_all.append(list_single)
#         searchKeyword(blog_context, district)
#     page += 1
# printDistrict(district)