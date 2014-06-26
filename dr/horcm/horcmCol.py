#!/usr/bin/python
__author__ = 'Jonathan Stoker'


class Horcm:

    def __init__(self, horcmfile):
        """
        Object constructor for the horcm collection class
        :param horcmfile:
        """
        self._x = horcmfile

    @property
    def whichhorcm(self):
        """
        getter for the horcmfile attribute
        :return:
        """
        return self._x

    @whichhorcm.setter
    def whichhorcm(self, value):
        """
        setter for the horcm file number
        :param value:
        """
        self._x = value

    def collectgroups(self):
        """
        Method to collect the data out of the
        horcm files for group identification
        :return:
        """
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
