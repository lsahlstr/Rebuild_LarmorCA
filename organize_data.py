import sys, re, os, glob
sys.path.append('/Users/lsahlstr/scripts/python/modules')
from math import sqrt
from pdbReader import PDBReader
from csReader import CSReader
from features import Features
import numpy as np

def OrganizeData(nucleus, flag='test'):
    print str(flag) + " set for nucleus " + str(nucleus)

    features = []           # List for storing geometric features
    chemical_shifts = []    # List for storing cs values (responses)
    
    # Determine whether to organize data for the training or testing set
    if flag == 'test':
        globfiles = 'coors/A*.pdb'
    else:
        globfiles = 'coors/R*.pdb'
        
    for filename in glob.glob(globfiles):
        
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
        
        # Loop over all residue numbers
        for i in range(resnums[0],resnums[-1]+1):
            
            cs = cs_info.get(i, {}).get(nucleus)  # Get the chemical shift        
            
            # Only compute geometric features if cs exists for residue i
            if cs:
                
                # Compute the features; returns a tuple   
                tmp = Features(i, nucleus, xcoors, ycoors, zcoors)
                
                # If features is not empty, then store the information. Empty if 
                # not all residues have coordinates (e.g., i+1, i+2, i+3, i+4, ...)   
                if tmp:
                    features.append(tmp)
                    chemical_shifts.append(cs)
                   
        features_arr = np.asarray(features)
        chemical_shifts_arr = np.asarray(chemical_shifts)
        #print features_arr
        #print chemical_shifts_arr
        #print features_arr.shape
        #print chemical_shifts_arr.shape
        
    return(features_arr, chemical_shifts_arr)