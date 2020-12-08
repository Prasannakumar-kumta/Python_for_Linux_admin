#! /bin/python
#command 1 variables
import subprocess
uname="uname"
uname_argmnt="-a"
#command 2 variables
diskspace="df"
diskspace_argmnt="-h"

print "Gathering system info using %s command" % uname
subprocess.call([uname,uname_argmnt])
print"Gathering sytem info using %s command" %diskspace
subprocess.call([diskspace,diskspace_argmnt])
