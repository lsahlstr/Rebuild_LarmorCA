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
    
    def halfcoors(self):
        '''Get dictionaries of X/Y/Z half coordinates for each atom. The half
        coordinate is defined as the center-of-geometry between Ca(i) and
        Ca(i+1). Thus, the half coordinate is defined for all but the last
        residue.'''
        d_xhalfcoors = dict()
        d_yhalfcoors = dict()
        d_zhalfcoors = dict()
        for atom in self.atoms[:-1]:  # do not consider last residue
            if atom.res_num not in d_xhalfcoors:
                d_xhalfcoors[atom.res_num] = {}
            if atom.res_num not in d_yhalfcoors:
                d_yhalfcoors[atom.res_num] = {}
            if atom.res_num not in d_zhalfcoors:
                d_zhalfcoors[atom.res_num] = {}
                      
        for i in range(0,len(self.atoms)-1):     
            
            atom_i = self.atoms[i]
            atom_iplus1 = self.atoms[i+1]
            
            xhalfcoor = (atom_i.xcoor + atom_iplus1.xcoor)/2
            yhalfcoor = (atom_i.ycoor + atom_iplus1.ycoor)/2
            zhalfcoor = (atom_i.zcoor + atom_iplus1.zcoor)/2
            
            d_xhalfcoors[atom_i.res_num][atom_i.atom_name.strip()] = xhalfcoor
            d_yhalfcoors[atom_i.res_num][atom_i.atom_name.strip()] = yhalfcoor
            d_zhalfcoors[atom_i.res_num][atom_i.atom_name.strip()] = zhalfcoor
            
        return (d_xhalfcoors, d_yhalfcoors, d_zhalfcoors)