from collections import defaultdict

class Molecule(object):
    '''A molecule with a name and a list of atoms.'''
    
    def __init__(self):
        '''Create a Compound with a name and a list of Atoms.'''   
        self.atoms = []
            
    def __repr__(self):
        '''Return a string representation of this Molecule in this format:
            
            Molecule("NAME", (ATOM1, ATOM2, ...))
        '''
        
        res = ''
        for atom in self.atoms:
            res = res + repr(atom) + ', '
        
        # Strip off the last comma
        res = res[:-2]
        
        return 'Molecule(%s)' % (res)
        
    def __str__(self):
        '''Return a string representation of this Molecule in this format:
            
            (NAME, (ATOM1, ATOM2, ...))
        '''
        
        res = ''
        for atom in self.atoms:
            res = res + str(atom) + '\n'
        
        # Strip off the last comma
        res = res[:-2]
    
        return '%s' % (res)
        
    def add(self, a):
        '''Add Atom a to my list of Atoms.'''
        self.atoms.append(a)
        return(self.atoms)
    
    def resnames(self):
        '''Return a list of residue names'''
        tmp = []
        for atom in self.atoms:
            tmp.append(atom.resname())
        return tmp
    
    def resnums(self):
        '''Return a list of residue numbers'''
        tmp = []
        for atom in self.atoms:
            tmp.append(atom.res_num)
        return tmp

    def atom_names(self):
        '''Get list of atom names for each atom'''
        tmp = []
        for atom in self.atoms:
            tmp.append(atom.atom_name.strip())
        return tmp
    
    def xcoors(self):
        '''Get dictionary of X coordinates for each atom'''
        d = defaultdict(int)
        for atom in self.atoms:
            d[atom.res_num] = {}        
    
        for atom in self.atoms:
            d[atom.res_num][atom.atom_name.strip()] = atom.xcoor    

        return d
    
    def ycoors(self):
        '''Get dictionary of Y coordinates for each atom'''
        d = defaultdict(int)
        for atom in self.atoms:
            d[atom.res_num] = {}        
    
        for atom in self.atoms:
            d[atom.res_num][atom.atom_name.strip()] = atom.ycoor    

        return d
    
    def zcoors(self):
        '''Get dictionary of Z coordinates for each atom'''
        d = defaultdict(int)
        for atom in self.atoms:
            d[atom.res_num] = {}        
    
        for atom in self.atoms:
            d[atom.res_num][atom.atom_name.strip()] = atom.zcoor    

        return d
    
    def pseudocenters(self):
        '''Get dictionaries of X/Y/Z pseudocenters for each atom. The pseudo-
        center is defined as the center-of-geometry between Ca(i) and Ca(i+1).
        Thus, the pseudocenter is defined for all but the last residue.'''
        d_xpseudocenters = defaultdict(int)
        d_ypseudocenters = defaultdict(int)
        d_zpseudocenters = defaultdict(int)
        for atom in self.atoms[:-1]:  # do not consider last residue
            d_xpseudocenters[atom.res_num] = {}
            d_ypseudocenters[atom.res_num] = {}
            d_zpseudocenters[atom.res_num] = {}
                      
        for i in range(0,len(self.atoms)-1):     
            
            atom_i = self.atoms[i]
            atom_iplus1 = self.atoms[i+1]
            
            xpseudocenter = (atom_i.xcoor + atom_iplus1.xcoor)/2
            ypseudocenter = (atom_i.ycoor + atom_iplus1.ycoor)/2
            zpseudocenter = (atom_i.zcoor + atom_iplus1.zcoor)/2
            
            d_xpseudocenters[atom_i.res_num][atom_i.atom_name.strip()] = xpseudocenter
            d_ypseudocenters[atom_i.res_num][atom_i.atom_name.strip()] = ypseudocenter
            d_zpseudocenters[atom_i.res_num][atom_i.atom_name.strip()] = zpseudocenter
            
        return (d_xpseudocenters, d_ypseudocenters, d_zpseudocenters)