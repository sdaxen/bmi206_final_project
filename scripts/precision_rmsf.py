#!/usr/bin/env python

'''precision_rmsf.py
Calculates the within- and between-cluster RMSD (=precision)
It uses the IMP.pmi.analysis.Precision class
Also calculates within-cluter residue mean square fluctuation (RMSF)
'''

import IMP
import IMP.pmi
import IMP.pmi.analysis
import IMP.pmi.output
import IMP.atom
import glob
import os
import sys
from itertools import combinations_with_replacement

# common settings
test_mode = False                        # runs on every 10 frames
cwd = os.getcwd()

# choose components for the precision calculation
# key is the named precision item
# value is a list of selection tuples [either "domain_name" or (start,stop,"domain_name") ]
selections={"Hub":["Nup145c","Sec13","Seh1","Nup85"], "Nup84": ["Nup84"], 
            "Nup85": ["Nup85"], "Nup120": ["Nup120"], "Nup133": ["Nup133"],
            "Nup145c": ["Nup145c"], "Seh1": ["Seh1"], "Sec13": ["Sec13"]}


##############################
# don't change anything below
##############################

# setup Precision calculator
model = IMP.Model()
pr = IMP.pmi.analysis.Precision(model,resolution=1,selection_dictionary=selections)
pr.set_precision_style('pairwise_drmsd_k')


# gather the RMF filenames for each cluster
rmf_list=[]
frame_list=[]
cluster_dirs=sys.argv[1:]
if test_mode:
  # runs on the first 10 structures to test if it runs smoothly
  for d in cluster_dirs:
      rmf_list.append(glob.glob(d+'/*.rmf3')[0::10])
      frame_list.append([0]*len(rmf_list[-1]))
else:
  for d in cluster_dirs:
      rmf_list.append(glob.glob(d+'/*.rmf3'))
      frame_list.append([0]*len(rmf_list[-1]))

#print frame_list

# add them to the Precision object
for rmfs,frames,cdir in zip(rmf_list,frame_list,cluster_dirs):
    pr.add_structures(zip(rmfs,frames),cdir)

# calculate intra-cluster and inter-cluster precision
print "calculating precision"
for clus1,clus2 in combinations_with_replacement(range(len(rmf_list)),2):
    pr.get_precision(cluster_dirs[clus1],
                     cluster_dirs[clus2],
                     cwd+"/precision."+str(clus1)+"."+str(clus2)+".out")

# compute residue mean-square fluctuation (RMSF)
print "calculating RMSF"
for d in cluster_dirs:
    pr.get_rmsf(structure_set_name=d,outdir=d)

print "done"
