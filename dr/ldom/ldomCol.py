#!/usr/bin/python
__author__ = 'Jonathan Stoker'

import subprocess

class LdomCol:

    def __init__(self):


    def ldomcollector(self):
        filename = "/var/opt/SUNWldm/ldom-db.xml"
        ldomfile = open(filename, 'r')
        ldomarray = []
        for line in ldomfile:
            line = line.rstrip()
            if not line.startswith('<ldom_name>'):
                continue
            elif line.startswith('<ldom_name>'):
                name = line[line.find(">")+1:line.find("<")]
                ldomarray.append(name)
        return ldomarray