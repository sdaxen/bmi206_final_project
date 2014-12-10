import os
import matplotlib
matplotlib.use('Agg')
import xltable
import glob

cluster_directory="kmeans_50_1/cluster.0"

field_map={}
field_map["prot1"]=0
field_map["prot2"]=2
field_map["res1"]=1
field_map["res2"]=3
field_map["score"]=4

prot_list=["Nup84", "Nup85", "Nup120", "Nup133", "Nup145c", "Seh1", "Sec13"]



### loading data

xlt=xltable.XLTable(contact_threshold=35)
xlt.load_crosslinks('../data/yeast_Nup84_DSS.new.dat',field_map)
xlt.load_crosslinks('../data/EDC_XL_122013.new.dat',field_map)
for prot in prot_list:
    xlt.load_sequence_from_fasta_file(
                       fasta_file="../data/protein_fasta.%s.txt" % prot,
                       id_in_fasta_file=prot,
                       protein_name=prot)  


for rmf in glob.glob(os.path.join(cluster_directory, "*.rmf3"))[0::10]:
   xlt.load_rmf_coordinates(rmf,0,prot_list)

### creating contact map
xlt.setup_contact_map()

### plotting

xlt.plot_table(prot_listx=prot_list,
           prot_listy=prot_list,
           alphablend=0.4,
           scale_symbol_size=1.5,
           gap_between_components=50,
           filename=os.path.join(cluster_directory, "XL_table.pdf"),
           contactmap=True,
           crosslink_threshold=35.0,
           display_residue_pairs=False,
           color_crosslinks_by_distance=False)
