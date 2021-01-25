#encoding=gbk

import pandas as pd
from snownlp import SnowNLP
from snownlp import sentiment

#��ȡץȡ��csv�ļ��������ڵ�3�У����Ϊ2
df=pd.read_csv('���ݲɼ�.csv',usecols=[0])

#��dataframeת��Ϊlist
contents=df.values.tolist()
print(len(contents))
word=[]
score=[]
for content in contents:
	#print(content)
	try:
		s=SnowNLP(content[0])
		score.append(s.sentiments)
	except:
		print("something is wrong")
		score.append(0.5)
print(len(score))
data2 = pd.DataFrame(score)
data2.to_csv('sentiment11.csv', header=False, index=False, mode='a+')
