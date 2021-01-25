#encoding=gbk

import pandas as pd
from snownlp import SnowNLP
from snownlp import sentiment

#读取抓取的csv文件，标题在第3列，序号为2
df=pd.read_csv('数据采集.csv',usecols=[0])

#将dataframe转换为list
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
