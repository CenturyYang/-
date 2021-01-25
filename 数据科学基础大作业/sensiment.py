#encoding=gbk
import pandas as pd
from snownlp import SnowNLP
from snownlp import sentiment
f = open('3月到4月.txt', encoding='gb18030', errors='ignore')
word = []
score= []
for line in f:
        s = SnowNLP(line[0])
        score.append(s.sentiments)

data2 = pd.DataFrame(score)
data2.to_csv('sentiment.csv', header=False, index=False, mode='a+')
