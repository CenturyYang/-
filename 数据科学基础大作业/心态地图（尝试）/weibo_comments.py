#encoding=gbk

import requests
import pandas as pd
import json
import time
import re
 
# ����ͷ����cookie��������αװ
header = {'Content-Type':'application/json; charset=utf-8','User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
Cookie = {'Cookie':'SUHB=0nl-t-jpott3lQ; SCF=ArfHZrR50j2dIBHthBCgbug0SIY3DMTR8lWwBE7L5h_ANIIE_nFkxL5wEMvyK4SIdpZcQIvW3HE8r_9YaG1GqSs.; ALF=1590484838; _T_WM=75965031443; SUB=_2A25zoSI5DeRhGeBG41sW8SzNwjWIHXVRak5xrDV6PUJbktANLVfFkW1NQfza9ocru9-jgkjuLFGSId3vfab05o_d; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFI3IIVqQEH4F-YPcpzGZQr5JpX5K-hUgL.FoqR1h.NeKzp1K.2dJLoIpQLxK-L1K2LBo-LxK-L1K2LBo-peKzEeLY0e7tt; XSRF-TOKEN=7f3292; WEIBOCN_FROM=1110006030; MLOGIN=1; M_WEIBOCN_PARAMS=uicode%3D10000011%26fid%3D102803'}
#���۷�ҳ�Ĺؼ��ֶ�
max_id = ""
#����ѭ��
while True:
	#���۵�һҳmax_idΪ��ֵ
	if max_id == "":
		url = "https://m.weibo.cn/comments/hotflow?id=4498609959453960&mid=4498609959453960&max_id_type=0"
	else:
		#��ʾmax_id
		print(max_id)
		#���ۺ�һҳurl�е�max_idΪǰһҳ�������Ĳ���
		url = "https://m.weibo.cn/comments/hotflow?id=4498609959453960&mid=4498609959453960&max_id="+str(max_id)+"&max_id_type="+str(max_id_type) 
	print("�����url�ǣ�"+url)
	#request�����ȡ
	response = requests.get(url, headers=header, cookies=Cookie) 
	#json��ʽ����
	comment = response.json()
	print("requestion����״̬:"+str(comment['ok']))
	#���OkֵΪ1����ʾ�����ɹ�
	if comment['ok'] == 0:
		break
	#��ȡmax_idֵ
	max_id = comment["data"]["max_id"]
	max_id_type = comment["data"]["max_id_type"]
	print("max_id is:"+str(max_id))
	print("max_id_type is:"+str(comment["data"]["max_id_type"]))
	#��ȡ�����ı��������˷��ź�Ӣ���ַ�
	for comment_data in comment["data"]["data"]:
		data = comment_data["text"]
		p = re.compile(r'(<span.*>.*</span>)*(<a.*>.*</ a>)?')
		data = re.sub('[^\u4e00-\u9fa5]', '', data)
		data = p.sub(r'', data)
		data1=[(comment_data['created_at'],comment_data['user']['id'],comment_data['user']['screen_name'],data)]
		data2 = pd.DataFrame(data1)
		data2.to_csv('weibo_comment.csv', header=False, index=False, mode='a+')
		
	#����3�룬��ֹ��ϵͳ��Ϊ������
	time.sleep(3)
	
	
