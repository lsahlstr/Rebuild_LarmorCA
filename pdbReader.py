import sys, re
from molecule import Molecule
from atom import Atom

def PDBReader(file):
    '''Read PDB ATOM lines that are in the Atomic Coordinate Entry Format Version 3.3 format:
    http://www.wwpdb.org/documentation/file-format-content/format33/sect9.html#ATOM
    Currently, this script only considers heavy atoms (i.e., not "H")'''
    
    molecule = Molecule()
    
    for line in file.readlines():
              
        if (line.startswith('ATOM')):
            line = line.rstrip()
            
            atom_label = str(line[0:6])
            atom_num = int(line[6:11])
            atom_name = str(line[12:16])
            alt_conf = str(line[16:17])
            res_name = str(line[17:20])
            chain = str(line[21:22])
            res_num = int(line[22:26])
            res_insert = str(line[26:27])
            xcoor = float(line[30:38])
            ycoor = float(line[38:46])
            zcoor = float(line[46:54])
            occu = float(line[54:60])
            bfac = float(line[60:66])                  
        
            # Only want C-alpha atoms
            match = re.search('CA', atom_name)
            if match:
                if alt_conf == ' ' or alt_conf == 'A':  # Only consider alt_conf A
                    atom = Atom(atom_label, atom_num, atom_name, alt_conf, res_name, \
                            chain, res_num, res_insert, xcoor, ycoor, zcoor, \
                            occu, bfac)
            
                molecule.add(atom)
                
    return (molecule)