#!/usr/bin/env python
# -*- coding: utf-8 -*-


#############################################################################
# Imports					 												#
#############################################################################
import sys
import time
from optparse import OptionParser
import fileinput
import os
import hashlib
import datetime

#############################################################################
# Version & Info                                                            #
#############################################################################

APP_NAME = "SMBTouch scanner (x86)"
APP_VERSION = "0.4a"
APP_AUTHOR="op7ic"

#############################################################################
# Console Colour                                                            #
#############################################################################
#TODO add coloring to output
class bgcolors:
        OKGREEN = '\033[92m'
        FAIL='\033[93m'
        ENDC='\033[0m'

#############################################################################
# Functions                                                                 #
#############################################################################

#On signal restore config
def RestoreConfigOnError(xml_new_host):
    _xml_orig_host = '      <value>192.168.1.1</value>'
    for line in fileinput.input('Smbtouch-1.1.1.xml',inplace=True):
        print line.rstrip().replace(xml_new_host,_xml_orig_host)

#Check exploits
def CheckExploits(file):
    for line in open(file,"r").readlines():
        if "FB" in line:
            print line.rstrip().strip("\t")
        elif "FB/DANE" in line:
            print line.rstrip().strip("\t")
        elif "DANE" in line:
            print line.rstrip().strip("\t")

# Check for failed run. Check content + file size
def CheckConditions(out_file):
    out_size = len(out_file.readlines())
    if out_file.read().find("[-] Touch failed") == -1 and out_size > 60:
        return False
    elif out_size < 50:
        return True

# Parse target list
def ReadTargets(targetlist,verbose):
    li = open(targetlist,"r")
    _targ_list = list()
    for t in li.readlines():
        _targ_list.append(t.rstrip())
    return _targ_list

# Read output to determine if host is vulnerable
def ReadOutput(file, ip):
    #Read output file and parse to check for success
    out_file = open(file,"r")
    if CheckConditions(out_file) == False:
        # We have successful check
        print "[+] Success - IP %s is vulnerable " % (ip)
        CheckExploits(file)
    else:
        # SMBTouch failed - not vulnerable or can't access. 
        print "[-] SMBTouch check failed on IP: %s" % (ip)


def ScanAndReplace(targetlist,verbose,output_folder):
    if verbose:
        print "[+] Target Filename: %s: File MD5: %s " % (targetlist, hashlib.md5(b'%s' %(open(targetlist,"r"))).hexdigest())
    
    _for_target = ReadTargets(targetlist,verbose)
    _xml_orig_host = '      <value>192.168.1.1</value>'
    #TODO add ability to append port (139 instead of 445 etc)
    _xml_orig_port = '      <value>445</value>'

    for elems in _for_target:
        try:
            if verbose:
                print "[+] Adding %s to target list" % (elems.rstrip())
            xml_new_host='      <value>%s</value>' % (elems)
            for line in fileinput.input('Smbtouch-1.1.1.xml',inplace=True):
                print line.rstrip().replace(_xml_orig_host,xml_new_host)
            if "win" in sys.platform.lower():
                out_file = "%s\%s.txt" % (output_folder,elems)
                prep_cmd = r"Smbtouch-1.1.1.exe > %s" % (out_file)
            else:
                out_file = "%s/%s.txt" % (output_folder,elems)
                prep_cmd = r"wine Smbtouch-1.1.1.exe > %s" % (out_file)
            f_exec = os.popen(prep_cmd)
            time.sleep(3)
            ReadOutput(out_file,elems)
            if verbose:
                print "[+] Sleeping 3 sec to let it execute" 
            if verbose:
                print "[+] Restoring original config for IP %s " % (elems)
            for line in fileinput.input('Smbtouch-1.1.1.xml',inplace=True):
                print line.rstrip().replace(xml_new_host,_xml_orig_host)
        except KeyboardInterrupt:
            print "[+] Signal caught. Cleaning up"
            RestoreConfigOnError(xml_new_host)
            print "[+] Exit"
            sys.exit(255)
        except IOError,io:
            print "[+] IO Exception caught: %s " % (io)
            RestoreConfigOnError(xml_new_host)
            sys.exit(255)


#############################################################################
# Help & Args																#
#############################################################################


class Options:
    def get_args(self):
        parser = OptionParser()
        parser.add_option('-l','--list' ,action="store", dest="target_list", help="List of Target IPs separated by newline")
        parser.add_option('-d','--dir',action="store", dest="output_dir",default=".",help="Output Directory")
        parser.add_option('-v','--verbose', help="Verbose debug mode",action="store_true", dest="verbose",default=False)
        (o, a) = parser.parse_args()
        return o,a


#############################################################################
# Main																		#
#############################################################################


print("-=[ {0} v{1} ]=-\n\t\tby {2}\n".format(APP_NAME, APP_VERSION,APP_AUTHOR))

def main():
    (o,a) = Options().get_args()
    if o.verbose:
        print "[+] Starting at %s " % (datetime.datetime.now())
    try:
        ScanAndReplace(o.target_list,o.verbose,o.output_dir)
    except TypeError:
        print "No argument passed. Type -h for help"
if __name__=="__main__":
    main()
