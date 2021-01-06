"""
command line operate method
"""
import os


def cl_run(command: str) -> bool:
    return os.system(command) == 256


def cl_return(command: str) -> list:
    val = os.popen(cmd=command)
    l = []
    for v in val.readlines():
        l.append(v.replace('\n', ''))
    return l
