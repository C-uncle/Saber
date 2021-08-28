def readfile(path):
	fp = open(path, "r")
	content = fp.read()
	fp.close()
	return content

#path = input("请输入文件路径：")
path = "1.txt"
content = readfile(path)
print(type(content))