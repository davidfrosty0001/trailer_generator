#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date	: 2017-08-25 10:04:41
# @Author  : Lewis Tian (chasetichlewis@gmail.com)
# @Link	: https://github.com/LewisTian
# @Version : Python3.5

#		python youku_danmu.py

import requests
import time
import sys
from sys import stdout
import csv

s = requests.Session()
save_name = 'frozen'
# frozen http://v.youku.com/v_show/id_XNjk1ODc2NDMy.html?from=s1.8-3-1.1
# 2012 http://v.youku.com/v_show/id_XNjY2NzEzMjM2.html?from=s1.8-3-1.1
# insidious http://v.youku.com/v_show/id_XNjY0MzIzNTA0.html?spm=a2h0k.8191407.0.0&from=s1.8-1-1.2
# kongfu_panda http://v.youku.com/v_show/id_XMjk4ODY0MDky.html?spm=a2h0k.8191407.0.0&lang=%E5%9B%BD%E8%AF%AD
# pirates http://v.youku.com/v_show/id_XNjI0Nzg1NDg4.html?from=s1.8-3-1.1

headers = {
	'Referer':'http://v.youku.com/v_show/id_XNjk1ODc2NDMy.html?from=s1.8-3-1.1',
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36',
}

data = {
	'iid':'733779440',
	'begin':'1',
	'type':'1',
	'ct':'1001',
	'cid':'96',
	'ouid':'0',
	'lid':'0',
	'aid':'314762',
}


def main():

	req_cnt = 0
	total_cnt = 0
	times = []

	while True:
		data['begin'] = str(req_cnt)
		data['end'] = str(req_cnt + 1)
		url = "http://service.danmu.youku.com/pool"
		r = requests.post(url, headers = headers, data = data)
		json = r.json()
		
		count = json['count']
		current = json['current']
		danmu = json['data']
		req_cnt += 1 
		# print(json['data'])
		if count == 0:
			break

		# if req_cnt == 2:
		# 	break

		for x in danmu:
			# print(x)
			try:
				times.append([x['createtime'], x['playat'], x['content'], eval(x['propertis'])['size'], eval(x['propertis'])['color'], eval(x['propertis'])['pos']])
			except:
				continue
			total_cnt += 1
			stdout.write('\r%sth request, %s danmus scrapped' % (req_cnt, total_cnt))
			stdout.flush()
			# print(times[-1])

	# {'aid': 314762, 'content': '啊', 'createtime': 1518441342000, 'ct': 4002, 'id': 652018701, 'iid': 733779440, 'ipaddr': 3746176878, 'level': 0, 'lid': 0, 'mat': 0, 'ouid': 0, 'playat': 58946, 'propertis': '{"pos":"3","size":"0","color":"16777215"}', 'status': 99, 'type': 1, 'uid': 1394768021, 'ver': 1}
	
	with open('.../danmu/%s.csv' % save_name, 'w') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		for i in times:
			# print('\n', i)
			# print(type(i))
			spamwriter.writerow((i))

	print('\n------finished, \r%sth request, %s danmus scrapped' % (req_cnt, total_cnt) )

	'''
	_next = json['next']
	Danmu(danmu)
	for x in range(1, count):
		time.sleep(5)
		data['begin'] = x
		r = requests.post(url, headers = headers, data = data)
		json = r.json()
		danmu = json['data']
		Danmu(danmu)
	'''

if __name__ == '__main__':
	main()