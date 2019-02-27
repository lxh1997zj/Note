# !/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
list1 = []
def find_file(path,key):
	find_path = os.listdir(path)
	for now_path in find_path:
		file_path = os.path.join(path,now_path)
		if os.path.isfile(file_path):
			if now_path.find(key) != -1:
				list1.append(file_path)
				# print(list1)
		else:
			find_file(file_path,key)
	return list1
if __name__ == '__main__':
	test = find_file('.','IOday')
	for i in test:
		print(i)
