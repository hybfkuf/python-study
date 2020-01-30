#!/usr/bin/env python3

import os

def xls_to_xlsx(work_dir):
    old_ext = '.xls'
    new_ext = '.xlsx'
    for filename in os.path.listdir(work_dir):
        old_file = os.path.splitext(filename)
        file_ext = old_file[1]
        if file_ext == old_ext:
            new_file = old_file[0] + new_ext
            os.rename(os.path.join(work_dir, old_file), os.path.join(work_dir, new_file))
    print("完成重命名")
    print(os.listdir(work_dir))
