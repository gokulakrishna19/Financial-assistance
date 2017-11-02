from django.shortcuts import render
from .models import insurance

# Create your views here.

import pandas as pd

duration = 3

invduration=duration * 365 



def Analysis(request):
    invest_list = []
    data_df = pd.DataFrame.from_csv("insurance.csv")
    
    #data_df["Status2"] = list(map(Status_Calc, data_df["duration"], data_df["interest"], data_df["id1"]))
    z = data_df["id1"].values.tolist()
    y = data_df["duration"].values.tolist()
    x = data_df["interest"].values.tolist()
    
    
    for i in range(len(x)):
         if y[i]<= invduration+365 and y[i]>= invduration-365:
            #print(interest)
            if x[i] >= 10:
               
                invest_list.append( z[i])
                
    print(invest_list)
    plan=[]
    
    all_plans = insurance.objects.all()
    print(data_df.loc[data_df['id1'].isin(invest_list)])

    return render(request, 'insurance/insurance.html',{'plan':all_plans,'invest':invest_list})

