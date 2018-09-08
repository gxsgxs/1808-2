name = input("请输入要备份的文件名字")
p = name.rfind(".")#找到.索引
s = name[:p]
e = name[p:]
newname = s+"备份"+e
f = open(name,"r")
f1 = open(newname,"w")
while True:
	content = f.read(1024)
	f1.write(content)
	if len(content) == 0:
		break
f1.close()
f.close()
