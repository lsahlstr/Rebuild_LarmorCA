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
        d = dict()
        for atom in self.atoms:
            if atom.res_num not in d:
                d[atom.res_num] = {}        
    
        for atom in self.atoms:
            d[atom.res_num][atom.atom_name.strip()] = atom.xcoor    

        return d
    
    def ycoors(self):
        '''Get dictionary of Y coordinates for each atom'''
        d = dict()
        for atom in self.atoms:
            if atom.res_num not in d:
                d[atom.res_num] = {}        
    
        for atom in self.atoms:
            d[atom.res_num][atom.atom_name.strip()] = atom.ycoor    

        return d
    
    def zcoors(self):
        '''Get dictionary of Z coordinates for each atom'''
        d = dict()
        for atom in self.atoms:
            if atom.res_num not in d:
                d[atom.res_num] = {}        
    
        for atom in self.atoms:
            d[atom.res_num][atom.atom_name.strip()] = atom.zcoor    

        return d