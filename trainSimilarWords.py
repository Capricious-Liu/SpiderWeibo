from gensim.models import Word2Vec
from gensim.models import word2vec
import logging

# logging.basicConfig(format='%(asctime)s:%(levelname)s: %(message)s', level=logging.INFO)
# sentences = word2vec.Text8Corpus(r"C:\Users\liuzhili\Desktop\SpiderNeeded\fenci_result.txt")  # 加载语料
# model = word2vec.Word2Vec(sentences, size=200)  #训练skip-gram模型，默认window=5
#
# model.save('word2vector2.model')

model = Word2Vec.load('word2vector2.model')

# Train set
sentences = word2vec.Text8Corpus(r"C:\Users\liuzhili\Desktop\SpiderNeeded\fenci_result.txt")
model.train(sentences)
model.save('word2vector2.model')

# # 安全性
# keyword = [u"车祸", u"小偷", u"骚扰", u"抢劫", u"急刹车",u"急转弯",u"防护设施"]
# for item in keyword:
#     print(item)
#     try:
#         y = model.most_similar(item, topn=20)
#     except:
#         print("No such word in vocavulary")
#         y = []
#
#     for word_item in y:
#         print(word_item[0] + "    " + str(word_item[1]))
#     print("------------------------------")
# keyword = [u"身亡", u"事故", u"火灾"]
# for item in keyword:
#     print(item)
#     try:
#         y = model.most_similar(item, topn=20)
#     except:
#         print("No such word in vocavulary")
#         y = []
#
#     for word_item in y:
#         print(word_item[0] + "    " + str(word_item[1]))
#     print("------------------------------")



# 便捷性
# keyword = [u"等待", u"检查", u"人群", u"拥堵",u"有序"]
# for item in keyword:
#     print(item)
#     try:
#         y = model.most_similar(item, topn=20)
#     except:
#         print("No such word in vocavulary")
#         y = []
#
#     for word_item in y:
#         print(word_item[0] + "    " + str(word_item[1]))
#     print("------------------------------")

# # 经济性
# keyword = [u"服务", u"环境",u"钱",u"元"]
# for item in keyword:
#     print(item)
#     try:
#         y = model.most_similar(item, topn=20)
#     except:
#         print("No such word in vocavulary")
#         y = []
#
#     for word_item in y:
#         print(word_item[0] + "    " + str(word_item[1]))
#     print("------------------------------")

# # 舒适性
# keyword = [u"行人", u"占据", u"速度", u"后方"]
# for item in keyword:
#     print(item)
#     try:
#         y = model.most_similar(item, topn=20)
#     except:
#         print("No such word in vocavulary")
#         y = []
#
#     for word_item in y:
#         print(word_item[0] + "    " + str(word_item[1]))
#     print("------------------------------")