import sys, re, os, glob
from math import sqrt
from pdbReader import PDBReader
from csReader import CSReader
from features import Features
import numpy as np

def OrganizeData(nucleus, flag='test'):
    print str(flag) + " set for nucleus " + str(nucleus)

    features = []     # List for storing geometric features
    responses = []    # List for storing cs values (responses)
    features2 = []
    responses2 = []
    
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
        xhalfcoors, yhalfcoors, zhalfcoors = mc.halfcoors()
        
        # Get features and responses
        features, responses = Features(features, responses, resnums, cs_info, nucleus, xcoors, ycoors, zcoors)
        
        # Convert lists to numpy arrays
        features_arr = np.asarray(features)
        responses_arr = np.asarray(responses)
    
    return(features_arr, responses_arr)