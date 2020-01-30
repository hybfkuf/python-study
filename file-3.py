#!/usr/bin/env python3

import os

files=os.listdir('/tmp/hyb')

for filename in files:
    portion = os.path.splitext(filename)
    if portion[1] == ".txt":
        newname = portion[0] + ".sh"
        os.rename(filename, newname)
