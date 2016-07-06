from math import sqrt

def Features(i, nucleus, xcoors, ycoors, zcoors):
    '''Function for computing geometric features for a nucleus of residue number i.
    Simply return an empty tuple if the coordinates for a nucleus do not exist.'''
    
    # Flag for determining whether coordinates exist for computing geometric features
    flag = 1
    
    # Tuple for storing geometric features (want to append to list)
    features = ()
    
    # central residue (i)
    x = xcoors.get(i, {}).get(nucleus)
    y = ycoors.get(i, {}).get(nucleus)
    z = zcoors.get(i, {}).get(nucleus)
    if not x and not y and not z:
        flag = 0
                
    # previous residue (i-1)
    if flag == 1:
		xminus1 = xcoors.get(i-1, {}).get(nucleus)
		yminus1 = ycoors.get(i-1, {}).get(nucleus)
		zminus1 = zcoors.get(i-1, {}).get(nucleus)
		if not xminus1 and not yminus1 and not zminus1:
			flag = 0
    
    # next residue (i+1)
    if flag == 1:
		xplus1 = xcoors.get(i+1, {}).get(nucleus)
		yplus1 = ycoors.get(i+1, {}).get(nucleus)
		zplus1 = zcoors.get(i+1, {}).get(nucleus)  
		if not xplus1 and not yplus1 and not zplus1: 
			flag = 0
    
    # i-2
    if flag == 1:
		xminus2 = xcoors.get(i-2, {}).get(nucleus)
		yminus2 = ycoors.get(i-2, {}).get(nucleus)
		zminus2 = zcoors.get(i-2, {}).get(nucleus)
		if not xminus2 and not yminus2 and not zminus2:
			flag = 0
    
    # i+2
    if flag == 1:
		xplus2 = xcoors.get(i+2, {}).get(nucleus)
		yplus2 = ycoors.get(i+2, {}).get(nucleus)
		zplus2 = zcoors.get(i+2, {}).get(nucleus)  
		if not xplus2 and not yplus2 and not zplus2: 
			flag = 0
	
	# i-3
    if flag == 1:
		xminus3 = xcoors.get(i-3, {}).get(nucleus)
		yminus3 = ycoors.get(i-3, {}).get(nucleus)
		zminus3 = zcoors.get(i-3, {}).get(nucleus)
		if not xminus3 and not yminus3 and not zminus3:
			flag = 0
	
	# i+3
    if flag == 1:
		xplus3 = xcoors.get(i+3, {}).get(nucleus)
		yplus3 = ycoors.get(i+3, {}).get(nucleus)
		zplus3 = zcoors.get(i+3, {}).get(nucleus)  
		if not xplus3 and not yplus3 and not zplus3: 
			flag = 0
	
	# i-4
    if flag == 1:
		xminus4 = xcoors.get(i-4, {}).get(nucleus)
		yminus4 = ycoors.get(i-4, {}).get(nucleus)
		zminus4 = zcoors.get(i-4, {}).get(nucleus)
		if not xminus4 and not yminus4 and not zminus4:
			flag = 0
	
	# i+4
    if flag == 1:
		xplus4 = xcoors.get(i+4, {}).get(nucleus)
		yplus4 = ycoors.get(i+4, {}).get(nucleus)
		zplus4 = zcoors.get(i+4, {}).get(nucleus)  
		if not xplus4 and not yplus4 and not zplus4: 
			flag = 0
	
	# i-5
    if flag == 1:
		xminus5 = xcoors.get(i-5, {}).get(nucleus)
		yminus5 = ycoors.get(i-5, {}).get(nucleus)
		zminus5 = zcoors.get(i-5, {}).get(nucleus)
		if not xminus5 and not yminus5 and not zminus5:
			flag = 0
	
	# i+5
    if flag == 1:
		xplus5 = xcoors.get(i+5, {}).get(nucleus)
		yplus5 = ycoors.get(i+5, {}).get(nucleus)
		zplus5 = zcoors.get(i+5, {}).get(nucleus)  
		if not xplus5 and not yplus5 and not zplus5: 
			flag = 0
    
    # Compute geometric features if necessary coordinates exist
    if flag == 1:
        
        # Feature 1: Distance => i, i-5
        f1 = abs(sqrt((x-xminus5)**2 + (y-yminus5)**2 + (z-zminus5)**2))
        
        # Feature 2: Distance => i, i-4
        f2 = abs(sqrt((x-xminus4)**2 + (y-yminus4)**2 + (z-zminus4)**2))
        
        # Feature 3: Distance => i, i-3
        f3 = abs(sqrt((x-xminus3)**2 + (y-yminus3)**2 + (z-zminus3)**2))
        
        # Feature 4: Distance => i, i-2
        f4 = abs(sqrt((x-xminus2)**2 + (y-yminus2)**2 + (z-zminus2)**2))
        
        # Feature 5: Distance => i, i-1
        f5 = abs(sqrt((x-xminus1)**2 + (y-yminus1)**2 + (z-zminus1)**2))
    
        # Feature 6: Distance => i, i+1
        f6 = abs(sqrt((x-xplus1)**2 + (y-yplus1)**2 + (z-zplus1)**2))
        
        # Feature 7: Distance => i, i+2
        f7 = abs(sqrt((x-xplus2)**2 + (y-yplus2)**2 + (z-zplus2)**2))
        
        # Feature 8: Distance => i, i+3
        f8 = abs(sqrt((x-xplus3)**2 + (y-yplus3)**2 + (z-zplus3)**2))
        
        # Feature 9: Distance => i, i+4
        f9 = abs(sqrt((x-xplus4)**2 + (y-yplus4)**2 + (z-zplus4)**2))
        
        # Feature 10: Distance => i, i+5
        f10 = abs(sqrt((x-xplus5)**2 + (y-yplus5)**2 + (z-zplus5)**2))
        
        features = (f1,f2,f3,f4,f5,f6,f7,f8,f9,f10)
    
    return(features)