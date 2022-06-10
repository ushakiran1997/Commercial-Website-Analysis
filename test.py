import pandas as pd 
import numpy as np
import seaborn as sns
from dash import Dash, dcc, html
import plotly.express as px
import matplotlib.pyplot as plt
import plotly
import missingno as msno

from base64 import b64encode
import io
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import plotly.graph_objects as go
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
import os

if not os.path.exists("images"):
    os.mkdir("images")

DFReview=pd.read_csv("F:/Data_Analyst/Project/yoshop/DFReview.csv")
print(DFReview.head())
dforder=pd.read_csv("F:/Data_Analyst/Project/yoshop/dforder.csv")
print(dforder.head())
dforder.groupby('Day_time')['LineItem Qty'].count().sort_values(ascending=False).plot.bar().set(title='Analysis Of Items Per Part of Day!')
plt.savefig("images/partday.pdf")
plt.show()
def yearana(a): 
    global viewtype
    dforder[dforder.year==a].groupby('months')['LineItem Qty'].count().sort_values(ascending=False).plot.barh()
    plt.show()
    print("Enter year for Analysis of data according to year:\nEnter 2020 for Analysis Data  according to year 2020:\nEnter 2019 for Analysis Data  according to year 2019:\nEnter 2018 for Analysis Data  according to year 2018:\nEnter 2017 for Analysis Data  according to year 2017:\nEnter 2016 for Analysis Data  according to year 2016:\n Exit enter x or X")
    year1 = input("Input Value for genrate Graph chart:")
    if year1=="x" or year1=="X":
        print("Enter 1 to see the analysis of Reviews given by Customers !\nEnter 2 to see the analysis of different payment methods used by the Customers ! \nEnter 3 to see the analysis of Top Consumer States of India ! \nEnter 4 to see the analysis of Top Consumer Cities of India ! \nEnter 5 to see the analysis of Top Selling Product Categories ! \nEnter 6 to see the analysis of Reviews for All Product Categories ! \nEnter 7 to see the analysis of Number of Orders Per Month Per Year  ! \nEnter 8 to see the analysis of Number of Orders Across Parts of a Day ! \nEnter 9 to see the Full Report Press X to exit : ! \n")
        viewtype = input("Input Value for genrate Graph chart:")
def daypart(a): 
    print("Analysis Of Items Per Part of Day!")
    plt.figure(figsize=(20,30))
    dforder[dforder.Day_time==a].groupby('ex')['LineItem Qty'].count().sort_values(ascending=False).plot.bar()
    plt.show()
    plt.savefig("images/part.pdf")
    print("Enter Day for Analysis of data according to Part of day:\nEnter Mid Night for Analysis Data  according Part of day i.e Mid Night:\nEnter Early Morning for Analysis Data  according to Part of day i.e.  Early Morning:\nEnter Afternoon for Analysis Data  according to Part of day i.e. Afternoon:\nEnter Evening for Analysis Data  according to Part of day i.e. Evening:\nEnter Night for Analysis Data  according to Part of day i.e. Night:\nExit enter 0")
    Daytype = input("Input Value for genrate Graph chart:")
    if Daytype==0:
        print("Enter 1 to see the analysis of Reviews given by Customers !\nEnter 2 to see the analysis of different payment methods used by the Customers ! \nEnter 3 to see the analysis of Top Consumer States of India ! \nEnter 4 to see the analysis of Top Consumer Cities of India ! \nEnter 5 to see the analysis of Top Selling Product Categories ! \nEnter 6 to see the analysis of Reviews for All Product Categories ! \nEnter 7 to see the analysis of Number of Orders Per Month Per Year  ! \nEnter 8 to see the analysis of Number of Orders Across Parts of a Day ! \nEnter 9 to see the Full Report Press X to exit : ! \n")
        viewtype = input("Input Value for genrate Graph chart:")
while True :
    print("Enter 1 to see the analysis of Reviews given by Customers !\nEnter 2 to see the analysis of different payment methods used by the Customers ! \nEnter 3 to see the analysis of Top Consumer States of India ! \nEnter 4 to see the analysis of Top Consumer Cities of India ! \nEnter 5 to see the analysis of Top Selling Product Categories ! \nEnter 6 to see the analysis of Reviews for All Product Categories ! \nEnter 7 to see the analysis of Number of Orders Per Month Per Year  ! \nEnter 8 to see the analysis of Number of Orders Across Parts of a Day ! \nEnter 9 to see the Full Report Press X to exit : ! \n")
    viewtype = input("Input Value for genrate Graph chart:")
    if viewtype == "1":
        print("Analysis of Reviews given by Customers")
        fig = px.bar(DFReview,x="stars",title="Analysis of Reviews given by Customers",color="status")
        fig.show()
        fig.write_html("images/task11.html")
       
    elif viewtype == '2':
        print("Analysis of Payment Method")
        fig = px.pie(dforder,names='Payment Method', title="Analysis of Payment Method")
        fig.show()
        fig.write_html("images/task12.html")
       
    elif viewtype == '3':
        print(" Top Consumer States of India")
         
        plt.figure(figsize=(20,10))
        sns.countplot(dforder['Billing State']).set(title='Analysis of Top Consumer States of India')
        plt.show()
        plt.savefig("images/partbill.pdf")
    elif viewtype == '4':
        
        dforder['Billing City'].value_counts()[0:3].sort_values(ascending=False).plot.barh().set(title='Analysis of Top Three Consumer  City  of India')
        plt.show()
        plt.savefig("images/partbillcity.pdf")
    elif viewtype == '5':
        
        DFReview['category'].value_counts()[0:3].sort_values(ascending=False).plot.barh().set(title='Analysis of Top Three category of sale')
        plt.show()
        plt.savefig("images/parcat.pdf")
    elif viewtype == '6':
        
        fig = px.bar(DFReview,x="category",y="stars",title="Analysis of  Reviews for All Product Categories",color="status")
        fig.show()
        fig.write_html("images/task13.html")
    elif viewtype == '7':
            print("Analysis of Items According to year !")
            dforder.groupby('year')['LineItem Qty'].count().sort_values(ascending=False).plot.barh().set(title='Analysis of Items According to year ')
            plt.show()
            print("Enter year for Analysis of data according to year:\nEnter 2020 for Analysis Data  according to year 2020:\nEnter 2019 for Analysis Data  according to year 2019:\nEnter 2018 for Analysis Data  according to year 2018:\nEnter 2017 for Analysis Data  according to year 2017:\nEnter 2016 for Analysis Data  according to year 2016:\n")
            year1 = input("Input Value for genrate Graph chart:")
            yearana(year1)
        
       
    elif viewtype == '8':
        
            print("Enter Day for Analysis of data according to Part of day:\nEnter Mid Night for Analysis Data  according Part of day i.e Mid Night:\nEnter Early Morning for Analysis Data  according to Part of day i.e.  Early Morning:\nEnter Afternoon for Analysis Data  according to Part of day i.e. Afternoon:\nEnter Evening for Analysis Data  according to Part of day i.e. Evening:\nEnter Night for Analysis Data  according to Part of day i.e. Night:\n")
            print("Analysis Of Items Per Part of Day!")
            plt.figure(figsize=(20,30))
            dforder.groupby('Day_time')['LineItem Qty'].count().sort_values(ascending=False).plot.bar()
            plt.show()
            plt.savefig("image/part.pdf")
            Daytype = input("Input Value for genrate Graph chart:")
            daypart(Daytype)
    elif viewtype == '9':
        print("Analysis of Reviews given by Customers")
        fig = px.bar(DFReview,x="category",y="stars",title="Analysis of Reviews given by Customers",color="stars")
        fig.write_html("images/task111.html")
        fig.show()
        print("Analysis of Payment Method")
        sns.countplot(dforder['Payment Method'])
        fig = px.bar(dforder,x='Payment Method',title="Analysis of Payment Method")
        fig.show()
        print(" Top Consumer States of India")
        plt.figure(figsize=(20,10))
        sns.countplot(dforder['Billing State'])
        plt.show()
        print("Top Consumer City of India").set(title='Top Consumer States of India')
        dforder['Billing City'].value_counts()[0:3].sort_values(ascending=False).plot.barh().set(title='Top Consumer City of India')
        plt.show()
        plt.savefig("images/billing.pdf")
        print("Top category of Product")
        DFReview['category'].value_counts()[0:3].sort_values(ascending=False).plot.barh().set(title='Top category of Product')
        
        fig = px.bar(DFReview,x="category",y="stars",title="Analysis of  Reviews for All Product Categories",color="status")
        fig.show()
       
        print("Analysis Of Items Per year!")
        dforder.groupby('year')['LineItem Qty'].count().sort_values(ascending=False).plot.barh().set(title='Analysis Of Items Per year')
        
        print("Analysis Of Items Per Part of Day!")
        plt.figure(figsize=(20,30))
        dforder.groupby('Day_time')['LineItem Qty'].count().sort_values(ascending=False).plot.bar().set(title='Analysis Of Items Per Part of Day!')
        plt.savefig("images/partday.pdf")
        plt.show()
       
        
    
    elif viewtype == 'X' or viewtype=="x" :
        break