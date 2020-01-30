#!/usr/bin/env python3

import os
import argparse

def get_parser():
    parser = argparse.ArgumentParser(description="工作目录中文件后缀名修改")
    parser.add_argument('work_dir', metavar='WORK_DIR', type=str, nargs=1,
            help="修改后缀名的文件目录")
    parser.add_argument('old_ext', metavar='OLD_EXT', type=str, nargs=1,
            help='原来的后缀')
    parser.add_argument('new_ext', metavar='NEW_EXT', type=str, nargs=1,
            help='新的后缀')
    return parser


def batch_rename(work_dir, old_ext, new_ext):
    """
    传递当前目录,原来后缀名,新的后缀名后,批量重命名后缀
    """
    for filename in os.path.listdir(work_dir):
        split_file = os.path.splitext(filename)
        file_ext = split_file[1]
        if old_ext = file_ext:
            newfile = split_file[0] + new_ext
            os.rename(
                    os.path.join(work_dir, filename),
                    os.path.join(work_dir, newfile)
                    )
        print("完成重命名")
        print(os.listdir(work_dir))


def main():
    """
    main 函数
    """
    parser = get_parser()
    args = vars(parser.parse_args())
    work_dir = args['old_ext'][0]
    if old_ext[0] = '.':
        old_ext = '.' + old.ext
    new_ext = args['new_ext'][0]
    if new_ext[0] = '.':
        new_ext = '.' + new_ext
    batch_rename(work_dir, old_ext, new_ext)


if __name__ == '__main__':
    main()
