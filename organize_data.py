import sys, re, os, glob
from math import sqrt
from pdbReader import PDBReader
from csReader import CSReader
from features import Features
import numpy as np

def OrganizeData(nucleus, flag='test'):
    print str(flag) + " set for nucleus " + str(nucleus)

    features = []     # List for storing geometric features for Ca coordinates
    responses = []    # List for storing cs values (responses) corresponding to Ca coordinates
    features2 = []	  # List for storing geometric features for pseudocenters
    responses2 = []	  # List for storing cs values (responses) corresponding to pseudocenters
    
    # Determine whether to organize data for the training or testing set
    if flag == 'test':
        globfiles = 'coors/A*.pdb'
    else:
        globfiles = 'coors/R*.pdb'
        
    for filename in glob.glob(globfiles):
        
        print filename
        
        # PDB file name
        pdbfilename = filename
        
        # CS file name
        filename = re.sub('.pdb', '', filename)
        filename = re.sub('coors/', 'data/measured_shifts_', filename)
        csfilename = str(filename) + '.dat'
        
        # Read CS file
        csfile = open(csfilename, 'r')
        cs_info = CSReader(csfile)
        
        # Read PDB files; stored as instances of Molecule class
        pdbfile = open(pdbfilename, 'r')
        mc = PDBReader(pdbfile)
        
        # Coordinate dictionaries
        xcoors = mc.xcoors()
        ycoors = mc.ycoors()
        zcoors = mc.zcoors()
                    
        # Resnum list
        resnums = list(set(mc.resnums()))
        
        # Atom name lists
        atomnames = mc.atom_names()
        
        # Get half coordinates
        xpseudocenters, ypseudocenters, zpseudocenters = mc.pseudocenters()
        
        # Get features and responses
        features, responses = Features(features, responses, resnums[:-1], cs_info, \
                                        nucleus, xcoors, ycoors, zcoors)
        features2, responses2 = Features(features2, responses2, resnums[:-1], cs_info, \
                                        nucleus, xpseudocenters, ypseudocenters, zpseudocenters)
        
        # Convert lists to numpy arrays
        features_arr = np.asarray(features)
        features2_arr = np.asarray(features2)
        responses_arr = np.asarray(responses)
        
        # Concatenate the lists built from Ca coordinates and the pseudocenters
        features_combined_arr = np.concatenate((features_arr, features2_arr), axis=1)
        print features_combined_arr.shape
    
    return(features_combined_arr, responses_arr)