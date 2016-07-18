from math import sqrt
#import sys

def Features(features, responses, resnums, cs_info, nucleus, xcoors, ycoors, zcoors):
    '''Function for computing geometric features and returning the responses (i.e., the
    chemical shift value) for a given nucleus across all residues. If the coordinates 
    for a nucleus do not exist, then the features and responses are ignored. This is 
    taken care of by the "flag" variable below; it is set to zero if the coordinates do
    not exist.'''
    
    features_tmp = [] # temporary feature list just for this molecule
    responses_tmp = [] # temporary response list just for this molecule
    
    # Loop over all residue numbers
    for i in range(resnums[0],resnums[-1]+1):
        #print "Residue number " + str(i)
        
        cs = cs_info.get(i, {}).get(nucleus)  # Get the chemical shift for nucleus of interest
        
        # Only compute geometric features if cs exists for residue i
        if cs:
            
            #print "CS exists"
            
            # Tuple for storing geometric features for residue i (want to append to list)
            features_res_tmp = ()
            
            # Flag for determining whether coordinates exist for computing geometric features
            flag = 1

            # central residue (i)
            x = xcoors.get(i, {}).get('CA')
            y = ycoors.get(i, {}).get('CA')
            z = zcoors.get(i, {}).get('CA')
            if not x and not y and not z:
                flag = 0
            
            # previous residue (i-1)
            if flag == 1:
                xminus1 = xcoors.get(i-1, {}).get('CA')
                yminus1 = ycoors.get(i-1, {}).get('CA')
                zminus1 = zcoors.get(i-1, {}).get('CA')
                if not xminus1 and not yminus1 and not zminus1:
                    flag = 0

            # next residue (i+1)
            if flag == 1:
                xplus1 = xcoors.get(i+1, {}).get('CA')
                yplus1 = ycoors.get(i+1, {}).get('CA')
                zplus1 = zcoors.get(i+1, {}).get('CA')  
                if not xplus1 and not yplus1 and not zplus1: 
                    flag = 0

            # i-2
            if flag == 1:
                xminus2 = xcoors.get(i-2, {}).get('CA')
                yminus2 = ycoors.get(i-2, {}).get('CA')
                zminus2 = zcoors.get(i-2, {}).get('CA')
                if not xminus2 and not yminus2 and not zminus2:
                    flag = 0

            # i+2
            if flag == 1:
                xplus2 = xcoors.get(i+2, {}).get('CA')
                yplus2 = ycoors.get(i+2, {}).get('CA')
                zplus2 = zcoors.get(i+2, {}).get('CA')  
                if not xplus2 and not yplus2 and not zplus2: 
                    flag = 0

            # i-3
            if flag == 1:
                xminus3 = xcoors.get(i-3, {}).get('CA')
                yminus3 = ycoors.get(i-3, {}).get('CA')
                zminus3 = zcoors.get(i-3, {}).get('CA')
                if not xminus3 and not yminus3 and not zminus3:
                    flag = 0

            # i+3
            if flag == 1:
                xplus3 = xcoors.get(i+3, {}).get('CA')
                yplus3 = ycoors.get(i+3, {}).get('CA')
                zplus3 = zcoors.get(i+3, {}).get('CA')  
                if not xplus3 and not yplus3 and not zplus3: 
                    flag = 0

            # i-4
            if flag == 1:
                xminus4 = xcoors.get(i-4, {}).get('CA')
                yminus4 = ycoors.get(i-4, {}).get('CA')
                zminus4 = zcoors.get(i-4, {}).get('CA')
                if not xminus4 and not yminus4 and not zminus4:
                    flag = 0

            # i+4
            if flag == 1:
                xplus4 = xcoors.get(i+4, {}).get('CA')
                yplus4 = ycoors.get(i+4, {}).get('CA')
                zplus4 = zcoors.get(i+4, {}).get('CA')  
                if not xplus4 and not yplus4 and not zplus4: 
                    flag = 0

            # i-5
            if flag == 1:
                xminus5 = xcoors.get(i-5, {}).get('CA')
                yminus5 = ycoors.get(i-5, {}).get('CA')
                zminus5 = zcoors.get(i-5, {}).get('CA')
                if not xminus5 and not yminus5 and not zminus5:
                    flag = 0

            # i+5
            if flag == 1:
                xplus5 = xcoors.get(i+5, {}).get('CA')
                yplus5 = ycoors.get(i+5, {}).get('CA')
                zplus5 = zcoors.get(i+5, {}).get('CA')  
                if not xplus5 and not yplus5 and not zplus5: 
                    flag = 0
                    
            # Compute geometric features if necessary coordinates exist and i is 
            # more than 6 residues away from the first residue (for determining j)
            # and more than 6 residues away from the last residue (for determining k)
            if flag == 1 and (i > resnums[5] and i < resnums[-6]):
    
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
                
                # Store features that only depend on the ith residue
                features_res_tmp = (f1,f2,f3,f4,f5,f6,f7,f8,f9,f10)
                                
                #### j: closest residue to i that is at least 6 residues FORWARD in sequence ####
                f21 = 0
                closest_res = 0  # WILL NEED TO STORE THIS FOR DETERMINING j+1, j+2, ETC.
                min_dist = 999999
                if i < resnums[-9]:  # i must be more than 6 residues from the last residue, plus two additional for j+2
                    for j in range(i+6,resnums[-3]): # need to stop two early so can call j+2
                        
                        xj = xcoors.get(j, {}).get('CA')
                        yj = ycoors.get(j, {}).get('CA')
                        zj = zcoors.get(j, {}).get('CA')
                        
                        dist = abs(sqrt((x-xj)**2 + (y-yj)**2 + (z-zj)**2))
                        if dist < min_dist:
                            min_dist = dist
                            closest_res = j                    
                    
                    # j
                    j = closest_res  # rename closest_res to j for clarity below
                    
                    xj = xcoors.get(j, {}).get('CA')
                    yj = ycoors.get(j, {}).get('CA')
                    zj = zcoors.get(j, {}).get('CA')
                    
                    # j-1
                    xj_minus1 = xcoors.get(j-1, {}).get('CA')
                    yj_minus1 = ycoors.get(j-1, {}).get('CA')
                    zj_minus1 = zcoors.get(j-1, {}).get('CA')
                    
                    # j+1
                    xj_plus1 = xcoors.get(j+1, {}).get('CA')
                    yj_plus1 = ycoors.get(j+1, {}).get('CA')
                    zj_plus1 = zcoors.get(j+1, {}).get('CA')
                    
                    # j-2
                    xj_minus2 = xcoors.get(j-2, {}).get('CA')
                    yj_minus2 = ycoors.get(j-2, {}).get('CA')
                    zj_minus2 = zcoors.get(j-2, {}).get('CA')
                    
                    # j+2
                    xj_plus2 = xcoors.get(j+2, {}).get('CA')
                    yj_plus2 = ycoors.get(j+2, {}).get('CA')
                    zj_plus2 = zcoors.get(j+2, {}).get('CA')
                    
                    # Feature 14: Distance => i-1, j-2
                    f14 = abs(sqrt((xminus1-xj_minus2)**2 + (yminus1-yj_minus2)**2 + (zminus1-zj_minus2)**2))
                    
                    # Feature 15: Distance => i-1, j-1
                    f15 = abs(sqrt((xminus1-xj_minus1)**2 + (yminus1-yj_minus1)**2 + (zminus1-zj_minus1)**2))
                    
                    # Feature 16: Distance => i-1, j
                    f16 = abs(sqrt((xminus1-xj)**2 + (yminus1-yj)**2 + (zminus1-zj)**2))
                    
                    # Feature 17: Distance => i-1, j+1
                    f17 = abs(sqrt((xminus1-xj_plus1)**2 + (yminus1-yj_plus1)**2 + (zminus1-zj_plus1)**2))
                    
                    # Feature 18: Distance => i-1, j+2
                    f18 = abs(sqrt((xminus1-xj_plus2)**2 + (yminus1-yj_plus2)**2 + (zminus1-zj_plus2)**2))
                    
                    # Feature 19: Distance => i, j-2
                    f19 = abs(sqrt((x-xj_minus2)**2 + (y-yj_minus2)**2 + (z-zj_minus2)**2))
                    
                    # Feature 20: Distance => i, j-1
                    f20 = abs(sqrt((x-xj_minus1)**2 + (y-yj_minus1)**2 + (z-zj_minus1)**2))
                    
                    # Feature 21: Distance => i,j (min_dist above)
                    f21 = min_dist
                    
                    # Feature 22: Distance => i, j+1
                    f22 = abs(sqrt((x-xj_plus1)**2 + (y-yj_plus1)**2 + (z-zj_plus1)**2))
                    
                    # Feature 23: Distance => i, j+2
                    f23 = abs(sqrt((x-xj_plus2)**2 + (y-yj_plus2)**2 + (z-zj_plus2)**2))
                    
                    # Feature 24: Distance => i+1, j-2
                    f24 = abs(sqrt((xplus1-xj_minus2)**2 + (yplus1-yj_minus2)**2 + (zplus1-zj_minus2)**2))
                    
                    # Feature 25: Distance => i+1, j-1
                    f25 = abs(sqrt((xplus1-xj_minus1)**2 + (yplus1-yj_minus1)**2 + (zplus1-zj_minus1)**2))
                    
                    # Feature 26: Distance => i+1, j
                    f26 = abs(sqrt((xplus1-xj)**2 + (yplus1-yj)**2 + (zplus1-zj)**2))
                    
                    # Feature 27: Distance => i+1, j+1
                    f27 = abs(sqrt((xplus1-xj_plus1)**2 + (yplus1-yj_plus1)**2 + (zplus1-zj_plus1)**2))
                    
                    # Feature 28: Distance => i+1, j+2
                    f28 = abs(sqrt((xplus1-xj_plus2)**2 + (yplus1-yj_plus2)**2 + (zplus1-zj_plus2)**2))  
                
                # Store features that depend on the ith and jth residues
                features_res_tmp = features_res_tmp + (f14,f15,f16,f17,f18,f19,f20,f21,
                										f22,f23,f24,f25,f26,f27,f28)
                                        
                #### k: closest residue to i that is at least 6 residues BACKWARDS in sequence ####
                f36 = 0
                closest_res = 0  # reset min_res; WILL NEED TO STORE THIS FOR DETERMINING k+1, k+2, ETC.
                min_dist = 999999 # reset min_dist
                if i > resnums[5]:  # i must be more than 6 residues from the first residue
                    #print 'i = ' + str(i)
                
                    for k in range(i-6,resnums[0]-1,-1):  # count backwards (-1 for decrement); have to go to resnum[0]-1
                        #print k
                    
                        xk = xcoors.get(k, {}).get('CA')
                        yk = ycoors.get(k, {}).get('CA')
                        zk = zcoors.get(k, {}).get('CA')
                    
                        dist = abs(sqrt((x-xk)**2 + (y-yk)**2 + (z-zk)**2))
                        #print dist
                        if dist < min_dist:
                            min_dist = dist
                            closest_res = k
                            
                        #print 'min dist: ' + str(min_dist)
                    
                    f36 = min_dist
                
                #features_res_tmp = (f21,f36)
                #features_res_tmp = features_res_tmp + (f36,)
                #features_res_tmp = (f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f20,f21,f22,f36)
                
                features_tmp.append(features_res_tmp)
                responses_tmp.append(cs)
    	#print ""
    # For residue i features, combine with features for i+1 and i-1 
    #responses = responses_tmp[1:len(responses)-1]
    for i in range(1,len(features_tmp)-1):
        tmp = features_tmp[i] + features_tmp[i+1] + features_tmp[i-1]
        features.append(tmp)
        responses.append(responses_tmp[i])
    
    return(features, responses)