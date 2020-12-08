#! /bin/python
import subprocess
def uname_func():
    uname="uname"
    uname_arg="-a"
    print "Gatering informantion using %s \n" %uname
    subprocess.call ([uname,uname_arg])

def diskspace_func():
    diskspace="df"
    diskspace_arg="-h"
    print "Gathering system info using %s \n" %diskspace
    subprocess.call ([diskspace, diskspace_arg])
def main():
    uname_func()
    diskspace_func()

main();
