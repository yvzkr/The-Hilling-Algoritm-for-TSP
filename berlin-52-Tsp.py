# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 15:31:30 2019

@author: yavuz

"""

import random
import matplotlib.pyplot as plt
import math
import itertools


def lokasyon_oku(p,X,Y):
    sehirler=[]
    with open("berlin52.tsp.txt") as b:
        locations = b.read()
        for location in locations.split("NODE_COORD_SECTION")[1:]:
            sehirler=(location.splitlines()[1:-1])
    p=[0]
    X=[]
    Y=[]
    for i in sehirler:
        p.append(int(i.split(" ")[0]))
        X.append(float(i.split(" ")[1]))
        Y.append(float(i.split(" ")[2]))
    return p[:-1],X,Y




def hillClimbing(p= [0,1,2,3,4],X = [5,19,70,8,22],Y= [78,40,2,55,36],ITER_MAX = 100):
    D = len(X)
    def ObjFunc():
        cost = 0
        for i in range(D-1):
            xd = X[p[i]] - X[p[i+1]]
            yd = Y[p[i]] - Y[p[i+1]]
            
            dis = math.sqrt(xd * xd + yd*yd)
            cost = cost + dis
        
        return cost
    
    best_Obj = ObjFunc()
    print("asdsad")
    
    result = []
    
    for iter in range(ITER_MAX):
        
        swap1 = random.randrange(D)
        swap2 = random.randrange(D)
        while swap1 == swap2:
            swap2 = random.randrange(D)
    
        temp = p[swap1]
        p[swap1] = p[swap2]
        p[swap2] = temp
    
        new_Obj = ObjFunc()
        
        result.append(new_Obj)
        
            
        if new_Obj < best_Obj:
            best_Obj = new_Obj
        else:
            temp = p[swap1]
            p[swap1] = p[swap2]
            p[swap2] = temp
          
    
    
    print("Best: ", best_Obj)
    
    
    
    print(result)
    print("en dusuk",min(result))
        

    

X=[]
Y=[]
p=[]
p,X,Y=lokasyon_oku(p,X,Y)
print(X,Y)
#hillClimbing(p,X,Y,5000000)