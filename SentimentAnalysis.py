from snownlp import SnowNLP

word_category = {u"安全性": [u"车祸", u"身亡", u"事故", "火灾", "意外", "死亡", "碰撞", "应急", "追尾", "隐患", "积压", "危害", "故障", "违规"],
                 u"便捷性": [u"等待", u"检查", u"人群", "拥堵", "有序", "耐心", "隐患", "积压", "路网", "流量", "客流", "人流"],
                 u"经济性": [u"经济", u"服务", u"环境", "每天", "元"],
                 u"舒适性": [u"排队", u"乱", u"行人", "占据", "速度", "后方", "碰撞", "卫生", "应急", "稳定", "有序", "禁烟"]
                 }

bus_category = {"安全性": [],
                "便捷性": [],
                "经济性": [],
                "舒适性": []}

def read_file(x):
    read_path = r"C:\Users\liuzhili\Desktop\SpiderNeeded\fenci_result\fenci_result.txt"
    f_obj = open(read_path, encoding='utf-8')
    res = f_obj.readlines()
    for item in res:
        x.append(item)
    f_obj.close()

def define_category(sentence, some_category):
    sen_item = sentence.split()
    senti_value = SnowNLP(sentence).sentiments
    for item in sen_item:
        if item in word_category[u"安全性"]:
            some_category["安全性"].append(senti_value)
        if item in word_category[u"便捷性"]:
            some_category["便捷性"].append(senti_value)
        if item in word_category[u"经济性"]:
            some_category["经济性"].append(senti_value)
        if item in word_category[u"舒适性"]:
            some_category["舒适性"].append(senti_value)

def save_file():
    try:
        output = open(r'C:\Users\liuzhili\Desktop\SpiderNeeded\final_result\bus_output.txt', 'w+')
    except:
        output = open(r'C:\Users\liuzhili\Desktop\SpiderNeeded\final_result\bus_output.txt', 'w')
    for item_safe in bus_category["安全性"]:
        output.write(str(item_safe) + " ")
    output.write("\n")
    for item_conv in bus_category["便捷性"]:
        output.write(str(item_conv) + " ")
    output.write("\n")
    for item_eco in bus_category["经济性"]:
        output.write(str(item_eco) + " ")
    output.write("\n")
    for item_comf in bus_category["舒适性"]:
        output.write(str(item_comf) + " ")


res = []
read_file(res)

ans = []

for res_item in res:
    define_category(res_item, bus_category)

for key, value in bus_category.items():
        print(key + "    " + str(len(value)))
save_file()
