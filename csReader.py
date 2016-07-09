import sys

def CSReader(file):
    '''Read chemical shift file and store list of residue number, nucleus,
    and chemical shift value.'''
    
    resnums = []
    cs_info = dict()
    
    for row in file.readlines():
        row = row.split()
        resname = str(row[0])
        resnum = int(row[1])
        nuc = str(row[2])
        cs = float(row[3])
                
        if resnum not in cs_info:
            resnums.append(resnum)
            cs_info[resnum] = {}
        
        cs_info[resnum][nuc] = cs
    
    return(cs_info)