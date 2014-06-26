#!/usr/bin/python
__author__ = 'Jonathan Stoker'


class HorcmCol:

    def __init__(self, horcmfile):
        """
        Object constructor for the horcm collection class
        :param horcmfile:
        """
        self._whichhorcm = horcmfile

    @property
    def whichhorcm(self):
        """
        getter for the horcmfile attribute
        :return:
        """
        return self._whichhorcm

    @whichhorcm.setter
    def whichhorcm(self, value):
        """
        setter for the horcm file number
        :param value:
        """
        self._whichhorcm = value

    @whichhorcm.getter
    def whichhorcm(self):
        return self._whichhorcm

    def collectgroups(self, horcm):
        """
        Method to collect the data out of the
        horcm files for group identification
        :return:
        """
        if horcm != HorcmCol.whichhorcm.getter:
            print "this should be equal to the original horcm file"
        print "Collecting Horcm information for file /etc/horcm"+self.whichhorcm+".conf\n"
        filename = "/etc/horcm"+self.whichhorcm+".conf"
        horcmin = open(filename, 'r')
        filearray = []
        for line in horcmin:
            newlinex = line.split(' ')[0]
            newliney = "".join(newlinex.split())
            if newliney.find("DR") == -1:
                filearray.append(newliney)
        filearray = list(set(filearray))
        return filearray
