#encoding=gbk

import urllib.request
import re
import pandas as pd
import numpy as np
import csv
import requests
import time

# 设置头部和cookie，反爬，伪装
header = {'Content-Type':'text/html; charset=utf-8','User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
Cookie = {'Cookie':'SUHB=0nl-t-jpott3lQ; SCF=ArfHZrR50j2dIBHthBCgbug0SIY3DMTR8lWwBE7L5h_ANIIE_nFkxL5wEMvyK4SIdpZcQIvW3HE8r_9YaG1GqSs.; ALF=1590484838; _T_WM=75965031443; SUB=_2A25zoSI5DeRhGeBG41sW8SzNwjWIHXVRak5xrDV6PUJbktANLVfFkW1NQfza9ocru9-jgkjuLFGSId3vfab05o_d; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFI3IIVqQEH4F-YPcpzGZQr5JpX5K-hUgL.FoqR1h.NeKzp1K.2dJLoIpQLxK-L1K2LBo-LxK-L1K2LBo-peKzEeLY0e7tt; MLOGIN=1; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D102803'}

weibo_comment_df=pd.read_csv('weibo_comment.csv',header=None,usecols=[1])
weibo_comments=weibo_comment_df.values.tolist()
print(len(weibo_comments))
for i in range(len(weibo_comments)):
	#print(type(weibo_comment[0]))
	url_base_1="http://weibo.cn/"
	url_base_2="/info"
	url=url_base_1+str(weibo_comments[i][0])+url_base_2
	print(i)
	print(url)
	try:
		html = requests.get(url,headers=header,cookies=Cookie)
		nickname=re.findall(r'<div class="c">昵称:(.*?)<br/>',html.text)
		print(nickname)
		sex=re.findall(r'<br/>性别:(.*?)<br/>',html.text)
		print(sex)
		location=re.findall(r'<br/>地区:(.*?)<br/>',html.text)
		print(location)
		data1=[(nickname[0],sex[0],location[0])]
		data2 = pd.DataFrame(data1)
		data2.to_csv('weibo_user.csv', header=False, index=False, mode='a+')
	except:
		print("something is wrong")
		data1=[('haha','男','南京')]
		data2 = pd.DataFrame(data1)
		data2.to_csv('weibo_user.csv', header=False, index=False, mode='a+')
	time.sleep(1)
	
