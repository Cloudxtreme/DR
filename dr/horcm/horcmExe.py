#!/usr/bin/python
__author__ = 'Jonathan Stoker'

import subprocess


class HorcmExe:

    def __init__(self, horcmmode, horcmcol):
        """
        object constructor for the horcmexecution class
        :param horcmmode: 1 or 0, 1 does a full takeover 0 will do a test
        :param horcmcol: this is the object for the horcm collection

        """

        self.currentmode = horcmmode
        self.currentcol = horcmcol
        self.currentgroups = self.currentcol.collectgroups(self.currentcol.whichhorcm.getter)
        if (self.currentmode < 0) or (self.currentmode > 1):
            print "please provide an interger between and 0\n 1 for true DR and 0 for Test"

    def horcmsane(self):
        """
        Method to check the status of the pairs in all groups in horcm

        :return:
        """
        groupsane = []
        for group in self.currentgroups:
            returncode = subprocess.call("/usr/bin/pairdisplay -ITC" + self.currentcol.whichhorcm.getter+"-g" + group +
                                         " -l | awk '{print $8}' | grep -i pair", shell=True)
            if returncode == 0:
                groupsane.append(group)
        if len(self.currentgroups) == len(groupsane):
            return True
        else:
            return False

    def horcmsaneind(self, group):
        """
        method to check individual groups
        :param group: this is the group name
        :return:
        """
        groupid = group
        returncode = subprocess.call("/usr/bin/pairdisplay -ITC" + self.currentcol.whichhorcm.getter + " -g " + groupid
                                     + " -l | awk '{print $8}' | grep -i pair", shell=True)
        if returncode == 0:
            return True
        else:
            return False

    def horcmsplitind(self, group):
        """
        Method to split an individual group for testing of DR
        :param group: this is the group name
        :return:
        """
        groupid = group
        if self.currentmode == 0:
            print "disks will be split and set RW for the group "+group+"\n"
            if self.horcmsaneind(groupid) is True:
                print "The group "+groupid+" is in the correct state\n"
                print "the disks will now be split"
                returncode = subprocess.call("/usr/bin/pairsplit -ITC" + self.currentcol.whichhorcm.getter + " -g " +
                                             groupid + " -rw", shell=True)
                if returncode == 0:
                    print "the disks were split"
                    return 0
                elif returncode == 1:
                    print "an error has occured"
                    return 1
            elif self.horcmsaneind(groupid) is False:
                print "The group "+groupid+" is in the wrong state"
        if self.currentmode == 1:
            print "this will takeover the disks from the primary site for "+group + "\n"
            selection = raw_input("Are you sure?[ Y/N]:")
            if (selection == "Y") or (selection == "y"):
                print "taking over disk"+group
                returncode = subprocess.call("/usr/bin/horcmtakeover -ITC" + self.currentcol.whichhorcm.getter + " -g "
                                             + group, shell=True)
                if returncode == 0:
                    print "disks takenover for "+group
                    return 0
                elif returncode == 1:
                    print "failure to take"
                    return 1
            if (selection == "n") or (selection == "N"):
                print "returning"
                return 2

    def horcmsplit(self):
        """
        Method to split all groups in horcm file

        """
        if self.currentmode == 0:
            group = self.currentcol.collectgroups(self.currentcol.whichhorcm.getter)
            for groupid in group:
                print "splitting the disks for "+group+" now\n"
                returncode = subprocess.call("/usr/bin/pairsplit -ITC" + self.currentcol.whichhorcm.getter + " -g " +
                                             groupid + " -rw", shell=True)
                if returncode == 0:
                    print "the disks were split\n"
                elif returncode == 1:
                    print "an error has occured in group "+groupid+"\n"
            return 0
        if self.currentmode == 1:
            group = self.currentcol.collectgroups(self.currentcol.whichhorcm.getter)
            selection = raw_input("This will takeover all volumes in the horcm "+self.currentcol.whichhorcm.getter +
                                  " are you sure? [Y/N]:")
            if (selection == "Y") or (selection == "y"):
                print "this will now take over the disks from the primary site to here\n"
                for groupid in group:
                    returncode = subprocess.call("/usr/bin/hormtakeover -ITC" + self.currentcol.whichhorcm.getter +
                                                 " -g" + groupid, shell=True)
                    if returncode == 0:
                        print "disk taken over\n"
                    elif returncode == 1:
                        print "disks could note be taken\n"
                return 0
            if (selection == "n") or (selection == "N"):
                print "returning\n"
                return 2
