from django.shortcuts import render
from .models import fd
from profiles.models import profiles
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm, preprocessing
import pandas as pd
from matplotlib import style
#import statistics
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


# Create your views here.
profile = profiles.objects.all()

duration = 0
interest_range = 0







        
features = [
            
            
            
            'interest',
            'min_duration',
            'max_duration',
            'amount_upto'
            
            ]

#print(interest_range)

def Status_Calc(max_duration, interest, min_duration):
    
    #count=0
    
    print(duration)
   


    if duration>=365 and duration<=729 :
        interest_range = 7
        
    elif duration>=180 and duration<365 :
        interest_range = 6.5
    elif duration>=730 and duration<=1094 :
        interest_range = 6.5
    elif duration>=1095 and duration<=1825 :
        interest_range = 6.2
    else:
        interest_range = 6

    print(interest_range)


    if max_duration<= duration+365 and min_duration>= duration-1000:
        
        if interest >= interest_range:
            #print( count+1)
           
            return 1
        
        else:
            return 0
    else:
        return 0
    

def Build_Data_Set(username):

    for p in profile:
        if p.username == username:
            csav = p.csaving
            invdur = p.durinv

    global duration
    duration = invdur * 365
    global csaving
    csaving = csav

    

    data_df = pd.DataFrame.from_csv("fixed_deposit.csv")
    
    
    data_df["Status2"] = list(map(Status_Calc, data_df["max_duration"], data_df["interest"], data_df["min_duration"]))
    
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
    
    
    #w = clf.coef_[0]
    #a = -w[0] / w[1]
    #xx = np.linspace(min(X[:, 0]), max(X[:, 0]))
    #yy = a * xx - clf.intercept_[0] / w[1]

    #plt.plot(xx,yy, "k-", label="non weighted")

    #plt.scatter(X[:, 0],X[:, 1],c=y)
   # plt.ylabel("Duration")
   # plt.xlabel("Interest")
    #plt.legend()

    #plt.show()
    
    
    data_df = pd.DataFrame.from_csv("fixed_deposit.csv")
 
    
   

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
    plan=[]
    print(invest_list)
    all_plans = fd.objects.all()

    for id in invest_list:
   		p=fd.objects.filter( pk=id )
    plans=data_df.loc[data_df['id1'].isin(invest_list)]
    for row in plans.iterrows():
        #print(str(row[0]) + " is the index of the row")
         plan.append(row[1])
    
    #return invest_list

    return render(request, 'fixeddeposit/Fixed deposit.html',{'plan':all_plans,'invest':invest_list})
