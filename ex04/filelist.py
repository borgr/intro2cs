#!/usr/bin/env python3

from autotest import filelist_test,res_code
from sys import argv

required = ["README",
            "ex4.py",
            "battleship.py",
            ]

try:
    filelist_test(argv[1], required)
except:
    res_code("tarfile",output="Testing tar file failed...")
    exit(-1)
