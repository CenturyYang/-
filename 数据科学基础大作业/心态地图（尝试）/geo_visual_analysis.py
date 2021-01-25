#encoding=gbk

import pandas as pd
from snownlp import SnowNLP
from snownlp import sentiment
import matplotlib.pyplot as plt 
from pyecharts import Map


#读取csv文件
df=pd.read_csv('weibo_user.csv')
#print(df)
grouped = df.groupby('location').describe().reset_index()
use_location=grouped['location'].values.tolist()
print(len(use_location))
print(use_location)

sentiment_average=df.groupby('location')['score'].mean()
sentiment_scores=sentiment_average.values

map = Map("中国地图", '中国地图', width=1200, height=600)
map.add("", use_location,sentiment_scores, visual_range=[0, 1], maptype='china', is_visualmap=True,
        visual_text_color="#fff")
map.render(path="中国地图.html")
