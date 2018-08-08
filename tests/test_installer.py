"""
Unit test  functions in installer.py
"""
from tljh import installer
import os


def test_ensure_node():
    if os.path.exists("/home/el/myfile.txt"):
        pass
    else:
        installer.ensure_node()
        node_file_path = '/usr/bin/node'
        assert os.path.exists(node_file_path), "node not found in: %r" % node_file_path 