#!/usr/bin/python
import os
import sys
from subprocess import call

merge_script = "nup84.merge.py"
cwd = os.getcwd()
nclusters = [1, 2]
subdir="scripts"
directories = [['nup84_replicate0'],
['nup84_replicate1'],
['nup84_replicate2'],
['nup84_rep_combined', 'nup84_replicate0', 'nup84_replicate1', 'nup84_replicate2'],
['nup84_cv0'],
['nup84_cv1'],
['nup84_cv2'],
['nup84_cv3'],
['nup84_cv4'],
['nup84_cv5'],
['nup84_cv6'],
['nup84_cv7'],
['nup84_cv8'],
['nup84_cv9']]

for dir_list in directories:
    chdir = os.path.join(cwd,dir_list[0],subdir)
    os.chdir(chdir)
    #cmd = ['cd', chdir]
    #print " ".join(cmd)
    #call(cmd)

    if len(dir_list) > 1:
        merge_dir = [os.path.join(cwd,x,subdir) for x in dir_list[1:]]
    else:
        #merge_dir=[]
        merge_dir = [os.path.join(cwd,dir_list[0],subdir)]

    for n in nclusters:
        cmd_args = ['python', os.path.join(cwd, merge_script)]
        print "-------------------------------------------------------------------"
        print "Running %s on %s with %d clusters" % (merge_script, dir_list[0], n)
        print "-------------------------------------------------------------------"
        if n > 1 or len(merge_dir) > 0:
            cmd_args.append(str(n))
            cmd_args.extend(merge_dir)
        print " ".join(cmd_args)
        call(cmd_args)

    os.chdir(cwd)
    #cmd = ['cd', cwd]
    #print " ".join(cmd)
    #call(cmd)

