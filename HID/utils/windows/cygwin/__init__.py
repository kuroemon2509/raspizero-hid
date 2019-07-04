# encoding=utf-8
import os
import time
import re

from tqdm import tqdm

import HID


def c_drive():
    HID.type_string('cd /cydrive/c\n')


def mkdir(filepath, recursive=True):
    HID.type_string('mkdir -r {}\n'.format(filepath))


def vim(filepath, insert_mode=False):
    HID.type_string('vi {}\n'.format(filepath))

    if insert_mode:
        time.sleep(0.2)
        HID.type_string('i')


def vim_wq():
    HID.press(HID.CHARS['ESC'])
    time.sleep(0.2)
    HID.type_string(':wq\n')


def type_file_to_vim(filepath, at_c_root=True):
    assert os.path.exists(filepath)

    if at_c_root:
        c_drive()

    parent_dir, filename = os.path.split(filepath)
    mkdir(parent_dir)
    time.sleep(0.2)
    vim(filepath, insert_mode=True)
    # get line count for progress bar
    num_lines = HID.utils.line_count(filepath)
    # open file to read content
    with open(filepath, encoding='utf-8') as inp_file:
        # use generator with tqdm for progress visualization
        for line in tqdm(inp_file, total=num_lines):
            HID.type_string(line)

    vim_wq()
