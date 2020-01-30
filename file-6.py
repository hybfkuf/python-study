#!/usr/bin/env python3

import os

def old_to_new(work_dir):
    old_ext = '.txt'
    new_ext = '.sh'
    for old_file in os.listdir(work_dir):
        file_split = os.path.splitext(old_file)
        file_ext = file_split[1]
        if file_ext == old_ext:
            new_file = file_split[0] + new_ext
            os.rename(
                    os.path.join(work_dir, old_file),
                    os.path.join(work_dir, new_file)
                    )
    print("完成重命名")
    print(os.listdir(work_dir))


work_dir='/tmp/hyb'

old_to_new(work_dir)
