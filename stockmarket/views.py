from django.shortcuts import render
from .models import name

import numpy as np
#import matplotlib.pyplot as plt
from sklearn import svm, preprocessing
import pandas as pd
#import quandl 
#import matplotlib.pyplot as plt
#from matplotlib import style
#import statistics
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

from collections import Counter

#style.use("ggplot")

how_much_better = 5


FEATURES =  ['DE Ratio',
             'Trailing P/E',
             'Price/Sales',
             'Price/Book',
             'Profit Margin',
             'Operating Margin',
             'Return on Assets',
             'Return on Equity',
             'Revenue Per Share',
             'Market Cap',
             'Enterprise Value',
             'Forward P/E',
             'PEG Ratio',
             'Enterprise Value/Revenue',
             'Enterprise Value/EBITDA',
             'Revenue',
             'Gross Profit',
             'EBITDA',
             'Net Income Avl to Common ',
             'Diluted EPS',
             'Earnings Growth',
             'Revenue Growth',
             'Total Cash',
             'Total Cash Per Share',
             'Total Debt',
             'Current Ratio',
             'Book Value Per Share',
             'Cash Flow',
             'Beta',
             'Held by Insiders',
             'Held by Institutions',
             'Shares Short (as of',
             'Short Ratio',
             'Short % of Float',
             'Shares Short (prior ']

def Status_Calc(stock, sp500):
    difference = stock - sp500

    if difference > how_much_better:
        return 1
    else:
        return 0


def Build_Data_Set():
    data_df = pd.DataFrame.from_csv("key_stats_acc_perf_NO_NA.csv")

    #data_df = data_df[:100]
    data_df = data_df.reindex(np.random.permutation(data_df.index))
    data_df = data_df.replace("NaN",0).replace("N/A",0)

    data_df["Status2"] = list(map(Status_Calc, data_df["stock_p_change"], data_df["sp500_p_change"]))
    

    X = np.array(data_df[FEATURES].values)#.tolist())

    y = (data_df["Status2"]
         .replace("underperform",0)
         .replace("outperform",1)
         .values.tolist())

    X = preprocessing.scale(X)

    Z = np.array(data_df[["stock_p_change","sp500_p_change"]])


    return X,y,Z


def Analysis(request):

    test_size = 1

    invest_amount = 10000
    
    total_invests = 0

    
    if_market = 0
    if_strat = 0



    
    X, y, Z = Build_Data_Set()
    #print(len(X))

    
    clf = svm.SVC(kernel="linear", C= 1.0)
    clf.fit(X[:-test_size],y[:-test_size])
    
    #w = clf.coef_[0]
    #a = -w[0] / w[1]
    #xx = np.linspace(min(X[:, 0]), max(X[:, 0]))
    #yy = a * xx - clf.intercept_[0] / w[1]

    #plt.plot(xx,yy, "k-", label="non weighted")

    #plt.scatter(X[:, 0],X[:, 1],c=y)
    #plt.ylabel("Duration")
    #plt.xlabel("Interest")
    #plt.legend()

    #plt.show()
    

    correct_count = 0

    for x in range(1, test_size+1):
        if clf.predict(X[-x])[0] == y[-x]:
            correct_count += 1

        if clf.predict(X[-x])[0] == 1:
            invest_return = invest_amount + (invest_amount * (Z[-x][0]/100))
            market_return = invest_amount + (invest_amount * (Z[-x][1]/100))
            total_invests += 1
            if_market += market_return
            if_strat += invest_return
            


    data_df = pd.DataFrame.from_csv("key_stats_acc_perf_NO.csv")

    data_df = data_df.replace("N/A",0).replace("NaN",0)

    X = np.array(data_df[FEATURES].values)

    X = preprocessing.scale(X)

    Z = data_df["Ticker"].values.tolist()
    plan=[]
    
    all_plans = name.objects.all()

    invest_list = []


    for i in range(len(X)):
        p = clf.predict(X[i])[0]
        if p == 1:
            #print(Z[i])
            Z[i] = Z[i].upper()
           #auth_tok = "CaTQH3eRNMg6F4DFeP9x"
            #stock = "AAPL"
            
            #data_df = quandl.get("WIKI/"+Z[i], trim_start = "2000-12-12", authtoken=auth_tok)
            
           # data_df[['Adj. Close']].plot()
            #plt.show()
            if Z[i] != 'CAH':
                invest_list.append(Z[i])
            
    #print(len(invest_list))
    #print(invest_list)
    invest_list.append("TSLA")
    invest_list.append("THYROCARE.BO")
   
    #return invest_list
    return render(request, 'stockmarket/stock market.html',{'plan':all_plans,'invest':invest_list})



#final_list = []

#loops = 1

#for x in range(loops):
#    stock_list = Analysis()
 #   for e in stock_list:
#        final_list.append(e)

#x = Counter(final_list)

#print(15*"_")
#for each in x:
#    if x[each] > loops - (loops/3):
#        print(each)


# Create your views here.
