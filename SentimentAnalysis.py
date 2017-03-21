from snownlp import SnowNLP
import time

def read_file(x):
    read_path = r"C:\Users\liuzhili\Desktop\SpiderNeeded\fenci_result.txt"
    f_obj = open(read_path, encoding='utf-8')
    res = f_obj.readlines()
    for item in res:
        x.append(item)
    f_obj.close()


res = []
read_file(res)

ans = []
start = time.clock()
for item in res:
    s = SnowNLP(item)
    ans.append(s.sentiments)


end = time.clock()

i = 1
for item in ans:
    print(str(i)+"   "+str(item))
    i += 1
print('Running time: %s Seconds' % (end-start))