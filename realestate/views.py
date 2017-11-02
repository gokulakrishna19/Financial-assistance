from django.shortcuts import render
from .models import Realestate
from profiles.models import profiles

# Create your views here.
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm, preprocessing
import pandas as pd

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

#from collections import Counter
profile = profiles.objects.all()



typ = "0"
emis = 0
duration = 0
saving = 0
msaving = 0
inner= "minimum"
residential="avg_price"
commercial="max_price"

        
features = [
            
            
            
            'avg_growth',
            'minimum',
            'avg_price',
            'max_price'
            
            
            
            ]

def Status_Calc(minimum, avg_growth):
    
    #count=0
    price_1000sqft= minimum * 1000
    print(minimum)
    if price_1000sqft<= saving:
        if avg_growth >= 0:
            #print( count+1)
           
            return 1
        
        else:
            return 0
    else:
        return 0
    

def Build_Data_Set(answer):
   


    if answer == "interior":
        types="minimum"
    elif answer == "residential":
        types="avg_price"
    elif answer == "commercial":
        types="max_price"

    global  typ
    typ = types
    data_df = pd.DataFrame.from_csv("real_estate.csv")
    
    
    data_df["Status2"] = list(map(Status_Calc, data_df[types], data_df["avg_growth"]))
    
    X = np.array(data_df[features].values)
    y = (data_df["Status2"].values)

    X = preprocessing.scale(X)
     
    return X,y
    

def Analysis(request):

    username = None
    if request.user.is_authenticated():
        username = request.user.username

    

    answer = "interior"
    dur = 0;
    emi = 0;
    msav = 0;
    csav = 0;
   
    if request.method == 'POST':
        answer = request.POST['type'] 
        dur = int(request.POST['ldur']) 
        emi = float(request.POST['emi'] )
        

    for p in profile:
        if p.username == username:
            csav = p.csaving
            msav = p.pmsaving


    if dur == 5:
        inr=0.1971
    elif dur == 10:
        inr= 0.3422
    elif dur == 15:
        inr= 0.4523
    elif dur == 20:
        inr= 0.5369
    elif dur == 25:
        inr= 0.6028
    elif dur == 30:
        inr= 0.6548
    elif dur == 0:
        inr= 0

    ins = inr * 100
    
    global msaving
    msaving = msav
    emis = msaving * emi
    duration = dur * 12
    totalpay = duration * emis
    interest = (emis * duration)*inr
    loan = (emis * duration)- interest 
    global saving
    saving = csav + loan
    print(csav)

    X, y = Build_Data_Set(answer)
    #print (len(X))
   # print (y)
    
    clf = svm.SVC(kernel="linear", C= 1.0)
    clf.fit(X,y)
    
    #w = clf.coef_[0]
    #a = -w[0] / w[1]
    #xx = np.linspace(min(X[:, 0]), max(X[:, 0]))
    #yy = a * xx - clf.intercept_[0] / w[1]

    #plt.plot(xx,yy, "k-", label="non weighted")

    #plt.scatter(X[:, 0],X[:, 1],c=y)
    #plt.ylabel("Price")
    #plt.xlabel("growth")
    #plt.legend()

    #plt.show()
    
    
    data_df = pd.DataFrame.from_csv("real_estate.csv")
 
    #print( data_df[features])
   

    X = np.array(data_df[features].values)
    

    X = preprocessing.scale(X)

    Z = data_df["area"].values.tolist()
    

    invest_list = []

    for i in range(len(X)):
       
        p = clf.predict(X[i])[0]
        
       
        if p == 1:
            #print(Z[i])
            invest_list.append(Z[i])

    #print(len(invest_list))
    print(invest_list)
    all_plans = Realestate.objects.all()
    #print(data_df.loc[data_df['area'].isin(invest_list)])
    
    #return invest_list
    return render(request, 'realestate/Real estate.html',{'plan':all_plans, 'typ':typ, 'totalpay':totalpay,'invest':invest_list, 'answer':answer,'loan':loan,'total':saving,'emi':emis, 'inr':ins,})