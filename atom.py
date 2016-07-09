#!/usr/bin/env python

class Atom(object):
    '''An atom with a number, symbol, and coordinates.'''
    
    def __init__(self, atom_label, atom_num, atom_name, alt_conf, res_name, \
                    chain, res_num, res_insert, xcoor, ycoor, zcoor, \
                    occu, bfac):
        '''Create at Atom with all elements from PDB-formatted line.'''
        self.atom_label = atom_label
        self.atom_num = atom_num
        self.atom_name = atom_name
        self.alt_conf = alt_conf
        self.res_name = res_name
        self.chain = chain
        self.res_num = res_num
        self.res_insert = res_insert
        self.xcoor = xcoor
        self.ycoor = ycoor
        self.zcoor = zcoor
        self.occu = occu
        self.bfac = bfac
        self.center = (xcoor,ycoor,zcoor)
    
        
    def __str__(self):
        '''Return a string representation of the atom in PDB format:
        
            (SYMBOL, X, Y, Z)
        '''   
        return "%-6s%5d %4s%1s%3s %1s%4d%1s   %8.3f%8.3f%8.3f%6.2f%6.2f" % \
                          (self.atom_label, self.atom_num, self.atom_name, \
                           self.alt_conf, self.res_name, self.chain, \
                           self.res_num, self.res_insert, self.xcoor, \
                           self.ycoor, self.zcoor, self.occu, self.bfac)
    
    #def resname(self):
    #'''Get residue name of this atom.'''
    
    #return(self.res_name)
    
    #def resnum(self):
    #'''Get residue number of this atom.'''
        
    #return(self.res_num)    
    