from math import sqrt
import numpy as np

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
            #flag = 1

            # central residue (i)
            x = xcoors.get(i, {}).get('CA')
            y = ycoors.get(i, {}).get('CA')
            z = zcoors.get(i, {}).get('CA')
            
            # previous residue (i-1)
            xminus1 = xcoors.get(i-1, {}).get('CA')
            yminus1 = ycoors.get(i-1, {}).get('CA')
            zminus1 = zcoors.get(i-1, {}).get('CA')

            # next residue (i+1)
            xplus1 = xcoors.get(i+1, {}).get('CA')
            yplus1 = ycoors.get(i+1, {}).get('CA')
            zplus1 = zcoors.get(i+1, {}).get('CA')  

            # i-2
            xminus2 = xcoors.get(i-2, {}).get('CA')
            yminus2 = ycoors.get(i-2, {}).get('CA')
            zminus2 = zcoors.get(i-2, {}).get('CA')

            # i+2
            xplus2 = xcoors.get(i+2, {}).get('CA')
            yplus2 = ycoors.get(i+2, {}).get('CA')
            zplus2 = zcoors.get(i+2, {}).get('CA')  

            # i-3
            xminus3 = xcoors.get(i-3, {}).get('CA')
            yminus3 = ycoors.get(i-3, {}).get('CA')
            zminus3 = zcoors.get(i-3, {}).get('CA')

            # i+3
            xplus3 = xcoors.get(i+3, {}).get('CA')
            yplus3 = ycoors.get(i+3, {}).get('CA')
            zplus3 = zcoors.get(i+3, {}).get('CA')  
                

            # i-4
            xminus4 = xcoors.get(i-4, {}).get('CA')
            yminus4 = ycoors.get(i-4, {}).get('CA')
            zminus4 = zcoors.get(i-4, {}).get('CA')

            # i+4
            xplus4 = xcoors.get(i+4, {}).get('CA')
            yplus4 = ycoors.get(i+4, {}).get('CA')
            zplus4 = zcoors.get(i+4, {}).get('CA')  
                
            # i-5
            xminus5 = xcoors.get(i-5, {}).get('CA')
            yminus5 = ycoors.get(i-5, {}).get('CA')
            zminus5 = zcoors.get(i-5, {}).get('CA')

            # i+5
            xplus5 = xcoors.get(i+5, {}).get('CA')
            yplus5 = ycoors.get(i+5, {}).get('CA')
            zplus5 = zcoors.get(i+5, {}).get('CA')  
                    
            # Compute geometric features if necessary coordinates exist and i is 
            # more than 6 residues away from the first residue (for determining j)
            # and more than 6 residues away from the last residue (for determining k)
    
            # Feature 1: Distance => i, i-5
            if xminus5 and yminus5 and zminus5:
                f1 = abs(sqrt((x-xminus5)**2 + (y-yminus5)**2 + (z-zminus5)**2))
            else:
                f1 = 999.0

            # Feature 2: Distance => i, i-4
            if xminus4 and yminus4 and zminus4:
                f2 = abs(sqrt((x-xminus4)**2 + (y-yminus4)**2 + (z-zminus4)**2))
            else:
                f2 = 999.0

            # Feature 3: Distance => i, i-3
            if xminus3 and yminus3 and zminus3:
                f3 = abs(sqrt((x-xminus3)**2 + (y-yminus3)**2 + (z-zminus3)**2))
            else:
                f3 = 999.0

            # Feature 4: Distance => i, i-2
            if xminus2 and yminus2 and zminus2:
                f4 = abs(sqrt((x-xminus2)**2 + (y-yminus2)**2 + (z-zminus2)**2))
            else:
                f4 = 999.0
                
            # Feature 5: Distance => i, i-1
            if xminus1 and yminus1 and zminus1:
                f5 = abs(sqrt((x-xminus1)**2 + (y-yminus1)**2 + (z-zminus1)**2))
            else:
                f5 = 999.0

            # Feature 6: Distance => i, i+1
            if xplus1 and yplus1 and zplus1:
                f6 = abs(sqrt((x-xplus1)**2 + (y-yplus1)**2 + (z-zplus1)**2))
            else:
                f6 = 999.0

            # Feature 7: Distance => i, i+2
            if xplus2 and yplus2 and zplus2:
                f7 = abs(sqrt((x-xplus2)**2 + (y-yplus2)**2 + (z-zplus2)**2))
            else:
                f7 = 999.0

            # Feature 8: Distance => i, i+3
            if xplus3 and yplus3 and zplus3:
                f8 = abs(sqrt((x-xplus3)**2 + (y-yplus3)**2 + (z-zplus3)**2))
            else:
                f8 = 999.0
                
            # Feature 9: Distance => i, i+4
            if xplus4 and yplus4 and zplus4:
                f9 = abs(sqrt((x-xplus4)**2 + (y-yplus4)**2 + (z-zplus4)**2))
            else:
                f9 = 999.0

            # Feature 10: Distance => i, i+5
            if xplus5 and yplus5 and zplus5:
                f10 = abs(sqrt((x-xplus5)**2 + (y-yplus5)**2 + (z-zplus5)**2))
            else:
                f10 = 999.0
            
            # Feature 11: Angle => i-1, i, i+1
            if xminus1 and yminus1 and zminus1 and xplus1 and yplus1 and zplus1:
                d23 = abs(sqrt((x-xminus1)**2 + (y-yminus1)**2 + (z-zminus1)**2))
                d12 = abs(sqrt((x-xplus1)**2 + (y-yplus1)**2 + (z-zplus1)**2))
                d13 = abs(sqrt((xminus1-xplus1)**2 + (yminus1-yplus1)**2 + (zminus1-zplus1)**2))
                f11 = np.degrees(np.arccos((d23**2 + d12**2 - d13**2)/(2 * d23 * d12)))
            else:
                f11 = 999.0
            
            # Feature 12: Dihedral angle => i, i+1, i+2, i+3
            # wiki_dihedral here: http://stackoverflow.com/questions/20305272/dihedral-torsion-angle-from-four-points-in-cartesian-coordinates-in-python
            if xplus1 and yplus1 and zplus1 and xplus2 and yplus2 and zplus2 and xplus3 and yplus3 and zplus3:
                p0 = np.asarray([x,y,z])
                p1 = np.asarray([xplus1,yplus1,zplus1])
                p2 = np.asarray([xplus2,yplus2,zplus2])
                p3 = np.asarray([xplus3,yplus3,zplus3])

                b0 = -1 * (p1 - p0)
                b1 = p2 - p1
                b2 = p3 - p2

                tmp1 = np.cross(b0,b1)
                tmp2 = np.cross(b2,b1)
                tmp3 = np.cross(tmp1,tmp2)

                y = np.dot(tmp3,b1) * (1.0/np.linalg.norm(b1))
                x = np.dot(tmp1,tmp2)

                f12 = np.degrees(np.arctan2(y, x))
            else:
                f12 = 999.0
            
            # Feature 13: Angle => i-2, i, i+2
            if xminus2 and yminus2 and zminus2 and xplus2 and yplus2 and zplus2:
                d23 = abs(sqrt((x-xminus2)**2 + (y-yminus2)**2 + (z-zminus2)**2))
                d12 = abs(sqrt((x-xplus2)**2 + (y-yplus2)**2 + (z-zplus2)**2))
                d13 = abs(sqrt((xminus2-xplus2)**2 + (yminus2-yplus2)**2 + (zminus2-zplus2)**2))
                f13 = np.degrees(np.arccos((d23**2 + d12**2 - d13**2)/(2 * d23 * d12)))
            else:
                f13 = 999.0
            
            # Store features that only depend on the ith residue
            features_res_tmp = (f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13)
                                
            #### j: closest residue to i that is at least 6 residues FORWARD in sequence ####
            closest_res = 0  # WILL NEED TO STORE THIS FOR DETERMINING j+1, j+2, ETC.
            min_dist = 9999
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
            if xminus1 and yminus1 and zminus1 and xj_minus2 and yj_minus2 and zj_minus2:
                f14 = abs(sqrt((xminus1-xj_minus2)**2 + (yminus1-yj_minus2)**2 + (zminus1-zj_minus2)**2))
            else:
                f14 = 999.0
            
            # Feature 15: Distance => i-1, j-1
            if xminus1 and yminus1 and zminus1 and xj_minus1 and yj_minus1 and zj_minus1:
                f15 = abs(sqrt((xminus1-xj_minus1)**2 + (yminus1-yj_minus1)**2 + (zminus1-zj_minus1)**2))
            else:
                f15 = 999.0
                
            # Feature 16: Distance => i-1, j
            if xminus1 and yminus1 and zminus1 and xj and yj and zj:
                f16 = abs(sqrt((xminus1-xj)**2 + (yminus1-yj)**2 + (zminus1-zj)**2))
            else:
                f16 = 999.0
            
            # Feature 17: Distance => i-1, j+1
            if xminus1 and yminus1 and zminus1 and xj_plus1 and yj_plus1 and zj_plus1:
                f17 = abs(sqrt((xminus1-xj_plus1)**2 + (yminus1-yj_plus1)**2 + (zminus1-zj_plus1)**2))
            else:
                f17 = 999.0
                
            # Feature 18: Distance => i-1, j+2
            if xminus1 and yminus1 and zminus1 and xj_plus2 and yj_plus2 and zj_plus2:
                f18 = abs(sqrt((xminus1-xj_plus2)**2 + (yminus1-yj_plus2)**2 + (zminus1-zj_plus2)**2))
            else:
                f18 = 999.0
            
            # Feature 19: Distance => i, j-2
            if x and y and z and xj_minus2 and yj_minus2 and zj_minus2:
                f19 = abs(sqrt((x-xj_minus2)**2 + (y-yj_minus2)**2 + (z-zj_minus2)**2))
            else:
                f19 = 999.0
                
            # Feature 20: Distance => i, j-1
            if x and y and z and xj_minus1 and yj_minus1 and zj_minus1:
                f20 = abs(sqrt((x-xj_minus1)**2 + (y-yj_minus1)**2 + (z-zj_minus1)**2))
            else:
                f20 = 999.0
            
            # Feature 21: Distance => i,j (min_dist above)
            if min_dist:
                f21 = min_dist
            else:
                f21 = 999.0
            
            # Feature 22: Distance => i, j+1
            if x and y and z and xj_plus1 and yj_plus1 and zj_plus1:
                f22 = abs(sqrt((x-xj_plus1)**2 + (y-yj_plus1)**2 + (z-zj_plus1)**2))
            else:
                f22 = 999.0
            
            # Feature 23: Distance => i, j+2
            if x and y and z and xj_plus2 and yj_plus2 and zj_plus2:
                f23 = abs(sqrt((x-xj_plus2)**2 + (y-yj_plus2)**2 + (z-zj_plus2)**2))
            else:
                f23 = 999.0
            
            # Feature 24: Distance => i+1, j-2
            if xplus1 and yplus1 and zplus1 and xj_minus2 and yj_minus2 and zj_minus2:
                f24 = abs(sqrt((xplus1-xj_minus2)**2 + (yplus1-yj_minus2)**2 + (zplus1-zj_minus2)**2))
            else:
                f24 = 999.0
            
            # Feature 25: Distance => i+1, j-1
            if xplus1 and yplus1 and zplus1 and xj_minus1 and yj_minus1 and zj_minus1:
                f25 = abs(sqrt((xplus1-xj_minus1)**2 + (yplus1-yj_minus1)**2 + (zplus1-zj_minus1)**2))
            else:
                f25 = 999.0
            
            # Feature 26: Distance => i+1, j
            if xplus1 and yplus1 and zplus1 and xj and yj and zj:
                f26 = abs(sqrt((xplus1-xj)**2 + (yplus1-yj)**2 + (zplus1-zj)**2))
            else:
                f26 = 999.0
            
            # Feature 27: Distance => i+1, j+1
            if xplus1 and yplus1 and zplus1 and xj_plus1 and yj_plus1 and zj_plus1:
                f27 = abs(sqrt((xplus1-xj_plus1)**2 + (yplus1-yj_plus1)**2 + (zplus1-zj_plus1)**2))
            else:
                f27 = 999.0
            
            # Feature 28: Distance => i+1, j+2
            if xplus1 and yplus1 and zplus1 and xj_plus2 and yj_plus2 and zj_plus2:
                f28 = abs(sqrt((xplus1-xj_plus2)**2 + (yplus1-yj_plus2)**2 + (zplus1-zj_plus2)**2))
            else:
                f28 = 999.0

            # Store features that depend on the ith and jth residues
            features_res_tmp = features_res_tmp + (f14,f15,f16,f17,f18,f19,f20,f21,
                                                    f22,f23,f24,f25,f26,f27,f28)
                                    
            #### k: closest residue to i that is at least 6 residues BACKWARDS in sequence ####
            closest_res = 0   # reset min_res; WILL NEED TO STORE THIS FOR DETERMINING k+1, k+2, ETC.
            min_dist = 9999 # reset min_dist
            for k in range(i-6,resnums[2]-1,-1):  # count backwards (-1 for decrement); have to go to resnum[2]-1
        
                xk = xcoors.get(k, {}).get('CA')
                yk = ycoors.get(k, {}).get('CA')
                zk = zcoors.get(k, {}).get('CA')
        
                dist = abs(sqrt((x-xk)**2 + (y-yk)**2 + (z-zk)**2))
                if dist < min_dist:
                    min_dist = dist
                    closest_res = k 
            
            # k
            k = closest_res  # rename closest_res to k for clarity below
            
            xk = xcoors.get(k, {}).get('CA')
            yk = ycoors.get(k, {}).get('CA')
            zk = zcoors.get(k, {}).get('CA')
            
            # k-1
            xk_minus1 = xcoors.get(k-1, {}).get('CA')
            yk_minus1 = ycoors.get(k-1, {}).get('CA')
            zk_minus1 = zcoors.get(k-1, {}).get('CA')
            
            # k+1
            xk_plus1 = xcoors.get(k+1, {}).get('CA')
            yk_plus1 = ycoors.get(k+1, {}).get('CA')
            zk_plus1 = zcoors.get(k+1, {}).get('CA')
            
            # k-2
            xk_minus2 = xcoors.get(k-2, {}).get('CA')
            yk_minus2 = ycoors.get(k-2, {}).get('CA')
            zk_minus2 = zcoors.get(k-2, {}).get('CA')
            
            # k+2
            xk_plus2 = xcoors.get(k+2, {}).get('CA')
            yk_plus2 = ycoors.get(k+2, {}).get('CA')
            zk_plus2 = zcoors.get(k+2, {}).get('CA')
            
            # Feature 29: Distance => i-1, k-2
            if xminus1 and yminus1 and zminus1 and xk_minus2 and yk_minus2 and zk_minus2:
                f29 = abs(sqrt((xminus1-xk_minus2)**2 + (yminus1-yk_minus2)**2 + (zminus1-zk_minus2)**2))
            else:
                f29 = 999.0
            
            # Feature 30: Distance => i-1, k-1
            if xminus1 and yminus1 and zminus1 and xk_minus1 and yk_minus1 and zk_minus1:
                f30 = abs(sqrt((xminus1-xk_minus1)**2 + (yminus1-yk_minus1)**2 + (zminus1-zk_minus1)**2))
            else:
                f30 = 999.0
            
            # Feature 31: Distance => i-1, k
            if xminus1 and yminus1 and zminus1 and xk and yk and zk:
                f31 = abs(sqrt((xminus1-xk)**2 + (yminus1-yk)**2 + (zminus1-zk)**2))
            else:
                f31 = 999.0
            
            # Feature 32: Distance => i-1, k+1
            if xminus1 and yminus1 and zminus1 and xk_plus1 and yk_plus1 and zk_plus1:
                f32 = abs(sqrt((xminus1-xk_plus1)**2 + (yminus1-yk_plus1)**2 + (zminus1-zk_plus1)**2))
            else:
                f32 = 999.0
            
            # Feature 33: Distance => i-1, k+2
            if xminus1 and yminus1 and zminus1 and xk_plus2 and yk_plus2 and zk_plus2:
                f33 = abs(sqrt((xminus1-xk_plus2)**2 + (yminus1-yk_plus2)**2 + (zminus1-zk_plus2)**2))
            else:
                f33 = 999.0
            
            # Feature 34: Distance => i, k-2
            if x and y and z and xk_minus2 and yk_minus2 and zk_minus2:
                f34 = abs(sqrt((x-xk_minus2)**2 + (y-yk_minus2)**2 + (z-zk_minus2)**2))
            else:
                f34 = 999.0
            
            # Feature 35: Distance => i, k-1
            if x and y and z and xk_minus1 and yk_minus1 and zk_minus1:
                f35 = abs(sqrt((x-xk_minus1)**2 + (y-yk_minus1)**2 + (z-zk_minus1)**2))
            else:
                f35 = 999.0
            
            # Feature 36: Distance => i,k (min_dist above)
            if min_dist:
                f36 = min_dist
            else:
                f36 = 999.0
            
            # Feature 37: Distance => i, k+1
            if x and y and z and xk_plus1 and yk_plus1 and zk_plus1:
                f37 = abs(sqrt((x-xk_plus1)**2 + (y-yk_plus1)**2 + (z-zk_plus1)**2))
            else:
                f37 = 999.0
            
            # Feature 38: Distance => i, k+2
            if x and y and z and xk_plus2 and yk_plus2 and zk_plus2:
                f38 = abs(sqrt((x-xk_plus2)**2 + (y-yk_plus2)**2 + (z-zk_plus2)**2))
            else:
                f38 = 999.0
            
            # Feature 39: Distance => i+1, k-2
            if xplus1 and yplus1 and zplus1 and xk_minus2 and yk_minus2 and zk_minus2:
                f39 = abs(sqrt((xplus1-xk_minus2)**2 + (yplus1-yk_minus2)**2 + (zplus1-zk_minus2)**2))
            else:
                f39 = 999.0
            
            # Feature 40: Distance => i+1, k-1
            if xplus1 and yplus1 and zplus1 and xk_minus1 and yk_minus1 and zk_minus1:
                f40 = abs(sqrt((xplus1-xk_minus1)**2 + (yplus1-yk_minus1)**2 + (zplus1-zk_minus1)**2))
            else:
                f40 = 999.0
            
            # Feature 41: Distance => i+1, k
            if xplus1 and yplus1 and zplus1 and xk and yk and zk:
                f41 = abs(sqrt((xplus1-xk)**2 + (yplus1-yk)**2 + (zplus1-zk)**2))
            else:
                f41 = 999.0
            
            # Feature 42: Distance => i+1, k+1
            if xplus1 and yplus1 and zplus1 and xk_plus1 and yk_plus1 and zk_plus1:
                f42 = abs(sqrt((xplus1-xk_plus1)**2 + (yplus1-yk_plus1)**2 + (zplus1-zk_plus1)**2))
            else:
                f42 = 999.0
            
            # Feature 43: Distance => i+1, k+2
            if xplus1 and yplus1 and zplus1 and xk_plus2 and yk_plus2 and zk_plus2:
                f43 = abs(sqrt((xplus1-xk_plus2)**2 + (yplus1-yk_plus2)**2 + (zplus1-zk_plus2)**2))
            
            features_res_tmp = features_res_tmp + (f29,f30,f31,f32,f33,f34,f35,f36,
                                                    f37,f38,f39,f40,f41,f42,f43)  
            
            
            features_tmp.append(features_res_tmp)
            responses_tmp.append(cs)

        
    # For residue i features, combine with features for i+1 and i-1 
    #responses = responses_tmp[1:len(responses)-1]
    for i in range(1,len(features_tmp)-1):
        tmp = features_tmp[i] + features_tmp[i+1] + features_tmp[i-1]
        features.append(tmp)
        responses.append(responses_tmp[i])
    
    return(features, responses)