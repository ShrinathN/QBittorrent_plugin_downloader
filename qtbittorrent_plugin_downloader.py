#!/bin/python
import requests
import bs4
import re

#constants
PAGE_URL = 'https://github.com/qbittorrent/search-plugins/wiki/Unofficial-search-plugins'

sess = requests.session()
page_data = sess.get(PAGE_URL)
bs = bs4.BeautifulSoup(page_data.text,features="lxml")
atags = bs.findAll('a')
links_list = []
for i in atags:
	try:
		if(i['href'].find('.py') != -1):
			links_list.append(i['href'])
	except KeyError:
		continue
total_files = len(links_list)
counter = 1
print('[INFO]\t' + str(total_files) + ' found')
for i in links_list:
	filename = re.findall('.[^/]*', i[::-1])[0]
	print('[INFO]\tDownloading ' + str(counter) + ' / ' + str(total_files) + ' ' + filename[::-1] + '...', end='')
	file_descriptor = open(filename[::-1], 'w')
	file_data = sess.get(i)
	file_descriptor.write(file_data.text)
	file_descriptor.close()
	print('Done!')
	counter = counter + 1