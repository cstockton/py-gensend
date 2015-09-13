#!/usr/bin/env python
from os import path
from sys import path as sys_path


def append_path():
    file_dir = path.dirname(path.realpath(__file__))
    gensend_dir = path.abspath(path.join(file_dir, '..', '..'))
    sys_path.insert(0, gensend_dir)


if __name__ == "__main__":
    append_path()
    from gensend import cmd
    cmd.execute_gensend()
