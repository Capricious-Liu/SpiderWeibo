from gensim.models import Word2Vec
from gensim.models import word2vec
import logging

# logging.basicConfig(format='%(asctime)s:%(levelname)s: %(message)s', level=logging.INFO)
# sentences = word2vec.Text8Corpus(r"C:\Users\liuzhili\Desktop\SpiderNeeded\fenci_result.txt")  # 加载语料
# model = word2vec.Word2Vec(sentences, size=200)  #训练skip-gram模型，默认window=5
#
# model.save('word2vector2.model')

model = Word2Vec.load('word2vector2.model')
# sentences = word2vec.Text8Corpus(r"C:\Users\liuzhili\Desktop\SpiderNeeded\fenci_result.txt")
# model.train(sentences)
# model.save('word2vector2.model')

y = model.most_similar(u"车祸", topn=20)
for item in y:
    print(item[0]+"     "+str(item[1]))
# print("配套设施")
# y = model.most_similar(u"设施", topn=20)
# for item in y:
#     print(item[0]+"     "+str(item[1]))
# y = model.most_similar(u"灭火器", topn=20)
# for item in y:
#     print(item[0]+"     "+str(item[1]))
# y = model.most_similar(u"", topn=20)
# for item in y:
#     print(item[0]+"     "+str(item[1]))
# print("------------------\n")
