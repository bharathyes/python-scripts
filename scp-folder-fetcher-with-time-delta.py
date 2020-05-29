#!/usr/bin/python

import sys
import os
from datetime import date, timedelta

yesterday = date.today() - timedelta(days=1)
date = yesterday.strftime("%Y%m%d")

if len(sys.argv) == 2:
    date = sys.argv[1]

print "Pulling files for  date " + date

scp_cmd = "sshpass -p 'password' scp -r sftpuser@13.07.47.74:/home/sftpuser/data/" + date +"/ /home/user/NAS/"
os.system(scp_cmd)

print "Completed. Quitting script."
