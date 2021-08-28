def readfile(path):
 fp = open(path,"rb")#读取二进制文件
 content = fp.read()#二进制转换为str
 fp.close()
 return content

content1=readfile("test.zip")
print(content1)
