#!/usr/bin/env python3


# 统计文件个数
def statLineCnt(statfile):
    cnt = 0
    with open(statfile, 'r', encoding='utf-8') as f:
        while f.readline():
            cnt += 1
    return cnt


# 
