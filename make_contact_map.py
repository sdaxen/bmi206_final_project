import os
import matplotlib
matplotlib.use('Agg')
import xltable
import glob
import sys
import cPickle as pkl

cluster_directory=sys.argv[1]

field_map={}
field_map["prot1"]=0
field_map["prot2"]=2
field_map["res1"]=1
field_map["res2"]=3
field_map["score"]=4

prot_list=["Nup84", "Nup85", "Nup120", "Nup133", "Nup145c", "Seh1", "Sec13"]


print "loading data"
### loading data

xlt=xltable.XLTable(contact_threshold=35)
xlt.load_crosslinks('../../nup84/data/yeast_Nup84_DSS.new.dat',field_map)
xlt.load_crosslinks('../../nup84/data/EDC_XL_122013.new.dat',field_map)
for prot in prot_list:
    xlt.load_sequence_from_fasta_file(
                       fasta_file="../../nup84/data/protein_fasta.%s.txt" % prot,
                       id_in_fasta_file=prot,
                       protein_name=prot)  

print "loading coordinates"
for rmf in glob.glob(os.path.join(cluster_directory, "*.rmf3"))[0::20]:
   xlt.load_rmf_coordinates(rmf,0,prot_list)

print "creating contact map"
### creating contact map
xlt.setup_contact_map()

print "plotting"
### plotting

xlt.plot_table(prot_listx=prot_list,
           prot_listy=prot_list,
           alphablend=0.4,
           scale_symbol_size=1.5,
           gap_between_components=50,
           filename=os.path.join(cluster_directory, "XL_table.pdf"),
           contactmap=True,
           crosslink_threshold=35.0,
           display_residue_pairs=True,
           color_crosslinks_by_distance=True)

pkl.dump(xlt.xl_dist_diffs, open(os.path.join(cluster_directory, "XL_threshold_diff_dict.pkl"), 'w'))
