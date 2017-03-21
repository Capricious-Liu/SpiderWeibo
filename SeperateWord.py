import jieba
import xlrd


def readExcel2txt():
    data = xlrd.open_workbook(r'C:\Users\liuzhili\Desktop\SpiderNeeded\output.xls')
    table = data.sheets()[0]

    nrows = table.nrows
    str = ""
    for i in range(1, nrows):
        str += table.cell(i, 2).value
        str += '\n'

    f = open(r"C:\Users\liuzhili\Desktop\SpiderNeeded\fenci.txt", "w", encoding='utf-8')
    f.write(str)
    f.close()

def jiebaUsing():
    f1 = open(r"C:\Users\liuzhili\Desktop\SpiderNeeded\fenci.txt", encoding='utf-8')
    f2 = open(r"C:\Users\liuzhili\Desktop\SpiderNeeded\fenci_result.txt", 'a', encoding='utf-8')

    lines = f1.readlines()  # 读取全部内容
    for line in lines:
        line.replace('\t', '').replace('\n', '').replace(' ', '')
        seg_list = jieba.cut(line, cut_all=False)
        f2.write(" ".join(seg_list))

    f1.close()
    f2.close()

readExcel2txt()
jiebaUsing()
