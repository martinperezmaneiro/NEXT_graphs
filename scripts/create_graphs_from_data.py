import os
import sys
import torch

from invisible_cities.core.configure  import configure
from NEXT_graphNN.utils.data_loader import graphDataset

if __name__ == "__main__":

    config  = configure(sys.argv).as_namespace
    file_in = os.path.expandvars(config.file_in)
    fileout = os.path.expandvars(config.fileout)
    
    if os.path.isfile(fileout):
        raise Exception('output file exist, please remove it manually')
    
    dataset = graphDataset(file_in, 
                           group             = config.group, 
                           table             = config.table,
                           id_name           = config.id_name, 
                           features          = config.features, 
                           label_n           = config.label_n, 
                           norm_features     = config.norm_features,
                           max_distance      = config.max_distance, 
                           ener_name         = config.ener_name,
                           coord_names       = config.coord_names, 
                           directed          = config.directed, 
                           fully_connected   = config.fully_connected, 
                           simplify_segclass = config.simplify_segclass)
    
    torch.save(dataset, fileout)






