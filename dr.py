#!/usr/bin/python
__author__ = 'Jonathan Stoker'

import dr.horcm.horcmExe
import dr.horcm.horcmCol
import dr.ldom.ldomCol
import dr.ldom.ldomImport
import dr.ldom.ldomExecute
import os

menuinput = ""
while menuinput != 4:
    os.system('clear')
    print "1. Test DR\n\n \
            2. Initiate DR\n\n \
            3. check status\n\n \
            4. exit\n"
    selection = raw_input("Please make a selection: [1-4]")
    if selection == 1:
        horcmsel = ""
        while horcmsel != 3:
            os.system('clear')
            print "please choose a file: \n\n \
                  1. Horcm100 - UNIX DR \n\n \
                 2. horcm200 - ESX DR \n\n \
                 3. Return\n"
            horcmsel = raw_input("please make a selection: [1-3]")
            if horcmsel == 1:
                horcm = dr.horcm.horcmCol.HorcmCol(100)
                horcmexe = dr.horcm.horcmExe.HorcmExe(0, horcm)
                print "Current groups available:\n\n"
                for element in horcm.collectgroups(horcm.whichhorcm):
                    print element+"\n\n"
                indisel = raw_input("Would you like to only test one group?[Y/N]")
                if (indisel == "Y") or (indisel == "y"):
                    group = horcm.selectgroup()
                    horcmexe.horcmsplitind(group)
                if (indisel == "n") or (indisel == "N"):
                    fulltest = raw_input("Would you like to test full DR?[Y/N")
                    if (fulltest == "y") or (fulltest == "Y"):
                        "Now splitting disks"
                        if horcmexe.horcmsplit() == 0:
                            print "now starting Ldoms"
            elif horcmsel == 2:
                horcm = dr.horcm.horcmCol.HorcmCol(200)
                horcmexe = dr.horcm.horcmExe.HorcmExe(0, horcm)
                print "none functioning - exiting"
                exit()
