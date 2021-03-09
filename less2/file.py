# coding=utf-8
import os

path = os.path.abspath('.')

filePath = os.path.join(path, 'less2/hello.text')

print(filePath)

f = open(filePath, "w")
f.write("hello")
f.close()

f = open(filePath, 'r')
print(f.read())

if os.path.exists(filePath):
    os.remove(filePath)
    print("删除成功")
