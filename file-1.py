#!/usr/bin/env python3

f = open('/tmp/testfile', 'w', encoding='utf-8')
print(f.write("测试文件写入 1"))
f.close()

f = open('/tmp/testfile', 'a', encoding='utf-8')
print(f.write("测试文件写入 2"))
f.close()

with open("/tmp/testfile", 'a') as f:
    f.write("测试文件写入 3")
