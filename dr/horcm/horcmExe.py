#!/usr/bin/python
__author__ = 'Jonathan Stoker'

import subprocess


class HorcmExe:

    def __init__(self, horcmnode, horcmcol, group):
        self.groupexe = group
        self.currentmode = horcmnode
        self.currentcol = horcmcol
        self.currentgroups = self.currentcol.collectgroups(self.currentcol.whichhorcm.getter)
        if (self.currentmode < 0) or (self.currentmode > 1):
            print "please provide an interger between and 0\n 1 for true DR and 0 for Test"

    def horcmsane(self):
        groupsane = []
        for group in self.currentgroups:
            returncode = subprocess.call("/usr/bin/pairdisplay -ITC"+self.currentcol.whichhorcm.getter+"-g"+group+" -l \
            | awk '{print $8}' | grep -i pair", shell=True)
            if returncode == 0:
                groupsane.append(group)
        if len(self.currentgroups) == len(groupsane):
            return True
        else:
            return False

    def horcmsaneind(self, group):
        groupid = group
        returncode = subprocess.call("/usr/bin/pairdisplay -ITC"+self.currentcol.whichhorcm.getter+" -g "+groupid+" -l \
        | awk '{print $8}' | grep -i pair", shell=True)
        if returncode == 0:
            return True
        else:
            return False

    def horcmsplitind(self, group):
        groupid = group
        if (self.currentmode == 0) and (self.groupexe == 0):
            print "disks will be split and set RW for the group "+group
            if self.horcmsaneind(groupid) is True:
                print "The group"+groupid+"is in the correct state\n"
                print "the disks will now be split"
                returncode = subprocess.call("/usr/bin/pairsplit -ITC"+self.currentcol.whichhorcm.getter+" -g "+groupid
                                             + " -rw")
                if returncode == 0:
                    print "the disks were split"
                    return 0
                elif returncode == 1:
                    print "an error has occured"
                    return 1