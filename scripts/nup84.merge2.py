import IMP
import IMP.pmi
import IMP.pmi.macros
import sys
import os

cwd = os.getcwd()

matrix_filename = "distance.rawmatrix.pkl" 

n_best_models = 100

load_matrix=False
#if os.path.isfile("%s.npy" % matrix_filename) and os.path.isfile("%s.data" % matrix_filename):
#    load_matrix=True

nclusters=1
merge_directories = [os.getcwd().rstrip('/')]
if len(sys.argv) > 1:
    nclusters=int(sys.argv[1])
if len(sys.argv) > 2:
    merge_directories = [x.rstrip('/') for x in sys.argv[2:]]

show_plot=False
rmsd_names=None
if nclusters>1:
  n_best_models=100
  rmsd_names = {"Nup84": "Nup84", "Nup120": "Nup120", "Nup133": "Nup133", "Nup145c": "Nup145c", 'Seh1': 'Seh1', "Sec13": "Sec13", "Nup85": "Nup85"}
  show_plot=True

density_names={"Nup84": ["Nup84"], "Nup85": ["Nup85"], "Nup120": ["Nup120"], "Nup133": ["Nup133"], "Nup145c": ["Nup145c"], "Seh1": ["Seh1"], "Sec13": ["Sec13"], "all": ["Nup84", "Nup85", "Nup120", "Nup133", "Nup145c", "Seh1", "Sec13"]}
#rmsd_names = {"Nup84": "Nup84", "Nup120": "Nup120", "Nup133": "Nup133", "Nup145c": "Nup145c", 'Seh1': 'Seh1', "Sec13": "Sec13", "Nup85": "Nup85"}
align_names=None
#align_names={"Nup84": "Nup84", "Nup120": "Nup120", "Nup133": "Nup133", "Nup145c": "Nup145c", 'Seh1': 'Seh1', "Sec13": "Sec13", "Nup85": "Nup85"}


model=IMP.Model()

mc=IMP.pmi.macros.AnalysisReplicaExchange0(model,
                  stat_file_name_suffix="stat",
                  merge_directories=merge_directories,
                  global_output_directory="output.1")

feature_list=["ISDCrossLinkMS_Distance_intrarb",
              "ISDCrossLinkMS_Distance_interrb",
              "ElectronMicroscopy2D",
              "ISDCrossLinkMS_Data_Score",
              "ISDCrossLinkMS_Psi_1.0_",
              "ISDCrossLinkMS_Sigma_1_",
              "LinkerRestraint",
              "ExcludedVolumeSphere_",
              "SimplifiedModel_Link_"]

prefiltervalue=300,
if '--test' in sys.argv: prefiltervalue=800
mc.clustering("SimplifiedModel_Total_Score_None",
              "rmf_file",
              "rmf_frame_index",
              distance_matrix_file=matrix_filename,
              load_distance_matrix_file=load_matrix,
              number_of_best_scoring_models=n_best_models,
              prefiltervalue=prefiltervalue,
              #first_and_last_frames=[0.0,0.5],
              outputdir="kmeans_%d_%d" % (n_best_models, nclusters),
              feature_keys=feature_list,
              display_plot=show_plot,
              exit_after_display=False,
              density_custom_ranges=density_names,
              get_every=1,
              skip_clustering=False,
              number_of_clusters=nclusters,
              alignment_components=align_names,
              rmsd_calculation_components=rmsd_names)
