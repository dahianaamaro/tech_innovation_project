# -*- coding: utf-8 -*-
"""
Created on Fri May  9 22:57:27 2025

@author: Dahiana
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns
from functions_file import func_scatter
from functions_file import func_line
#%%
#Importing data and cleaning it 
loc = "C:\\Users\\Dahiana\\Downloads\\"
file= "innovation_and_development1.xls"
df=pd.read_excel("C:\\Users\\Dahiana\\Downloads\\innovation_and_development1.xls", sheet_name = 'Sheet1')

df = pd.DataFrame(df)
df = df.dropna() #cleans data
list(df)        #gives list of all variables from data

#%%
#Gives stats of all data variables
print(df.describe())

print(df["pat"].describe())
print(df["poptotal"].describe())

#%%
#Correlation between patent and population
pat = df["pat"]
poptotal = df["poptotal"]

print(np.corrcoef(df['pat'], df['poptotal'] ))

#%%
#Regression 
y = np.log(df["pat"][df["pat"] > 0])
X = np.log(df["poptotal"][df["pat"] > 0])
years = df["year"][df["pat"]>0]

X = sm.add_constant(X)
reg = sm.OLS(y, X, missing="drop")
results = reg.fit()
print(results.summary())

#%%
#graph for reg
sns.regplot(x='poptotal', y='pat', color='red', data=df)
plt.title("Innovation vs Population")
plt.show()

#%%
#Calling graph function (scatter graph)
x=df['poptotal']
y=df['pat']
xlabel =('Population')
ylabel= ('Patent')
title= "Innovation vs Population"

func_scatter(x, y,xlabel, ylabel, title)


#%%
#Calling grahp function (line graph)
x=df['poptotal']
y=df['pat']
xlabel =('Population')
ylabel= ('Patent')
title="Innovation vs Population"

func_line(x, y, xlabel, ylabel, title)

