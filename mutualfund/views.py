from django.shortcuts import render
from profiles.models import profiles
from django.contrib.auth.models import User
from .models import Mutualfunds
# Create your views here.
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 07:53:09 2017

@author: sgoku
"""


import numpy as np
#import matplotlib.pyplot as plt
from sklearn import svm, preprocessing
import pandas as pd
#from matplotlib import style
#import statistics
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

#from collections import Counter

profile = profiles.objects.all()


invduration = 0
invdur = 0
        
features = [
            
            
            
            'returns',
            'durations'
            
            
            ]



def Status_Calc(durations, returns):
    
    #count=0
    
    print(invduration)
    if durations<= invduration+730 and durations>= invduration-500:
        if returns >= 5:
            #print( count+1)
           
            return 1
        
        else:
            return 0
    else:
        return 0
    

def Build_Data_Set(username):

    for p in profile:
        if p.username == username:
            
            invdur = p.durinv

    #amount_to_deposit=6000000
    global invduration
    invduration = invdur * 365

    data_df = pd.DataFrame.from_csv("mutual_funds.csv")
    
    
    data_df["Status2"] = list(map(Status_Calc, data_df["durations"], data_df["returns"]))
    
    X = np.array(data_df[features].values)
    y = (data_df["Status2"].values)
    print(y)
    X = preprocessing.scale(X)
     
    return X,y
    

def Analysis(request):
    username = None
    if request.user.is_authenticated():
        username = request.user.username

    print(username)

    
    X, y = Build_Data_Set(username)
    #print (len(X))
    
    clf = svm.SVC(kernel="linear", C= 1.0)
    clf.fit(X,y)
    
    
    data_df = pd.DataFrame.from_csv("mutual_funds.csv")
 
    
   

    X = np.array(data_df[features].values)
    

    X = preprocessing.scale(X)

    Z = data_df["id1"].values.tolist()
    
    

    invest_list = []

    for i in range(len(X)):
       
        p = clf.predict(X[i])[0]
        
       
        if p == 1:
            #print(Z[i])
            invest_list.append(Z[i])
        
            
    #print(len(invest_list))
    print(invest_list)
    #print(data_df.loc[data_df['id1'].isin(invest_list)])
    plan=[]
   
    all_plans = Mutualfunds.objects.all()
    
    
    #return invest_list
    return render(request, 'mutualfund/mutualfund.html',{'plan':all_plans,'invest':invest_list})

    

