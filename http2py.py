def readfile(path):
	fp = open(path, "rb")
	content = fp.read()
	fp.close()
	return content

def split_request(content):
	r = content.split(b'\r\n\r\n')
	new_r = []
	for i in r:
		new_r.append(i)
	return new_r

def get_url(l1, l2):
	return l2.split(': ')[1] + l1.split(' ')[1]

def deal_header(text):
	r = text.split(b'\r\n')
	n = len(r)
	url = get_url(r[0].decode('utf-8'), r[1].decode('utf-8'))
	header = []
	header.append(url)
	for i in range(2, n):
		tmp = r[i].decode('utf-8')
		tmp = tmp.split(': ')
		header.append((tmp[0], tmp[1]))
	return header

def deal_body(text):
	r = text.split('&')
	body = []
	for i in r:
		body.append((i.split('=')[0], i.split('=')[1]))
	return body
	
def Print(p, text):
	n = len(text)
	print('{')
	for i in range(p, n):
		print("'%s':'%s'"%(text[i][0], text[i][1]), end='')
		if i != n-1:
			print(',')
	print('\n}')

path = input("请输入文件路径：")


content = readfile(path)
header, body = split_request(content)

header = deal_header(header)

print('url=', header[0])

Print(1, header)

if body:
	body = deal_body(body.decode('utf-8'))
	Print(0, body)
