# ！/usr/bin/env python3
# -*- coding:utf-8 -*-
'貌似只能测试文件拓展名是否包含正确的str!'
import os
def findFile(findPath='.',findType=''):
	fileList = []
	for i in os.listdir(findPath):
		
		curPath = os.path.join(findPath,i)
		if os.path.isfile(curPath):
			if findType == '':  
				fileList.append(curPath)
			elif os.path.splitext(curPath)[1][1:] == findType:  # 确保文件后缀完全匹配，findType='xls'则必须匹配到.xls,如后缀为.xlsx则不匹配
				fileList.append(curPath)
		elif os.path.isdir(curPath):
			fileList += findFile(curPath,findType)
	return fileList
rst = findFile(findType='py')
print(rst)
