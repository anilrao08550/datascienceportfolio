#Completed in Ipython Notebook- Logistic regression predicting graduate admissions 
import pandas as pd
import numpy as np
import pylab as pl
import statsmodels.api as sm
%pylab inline

df = pd.read_csv("http://www.ats.ucla.edu/stat/data/binary.csv")
#rename the columns 
df.columns = ["admit", "GRE", "GPA", "prestige"]

df.hist()
pl.show()

getdata = pd.get_dummies(df['prestige'], prefix='prestige')
print getdata.head()
cols_to_keep = ['admit', 'GRE', 'GPA']
data = df[cols_to_keep].join(getdata.ix[:, 'prestige_2':])
print data.head()

train_cols = data.columns[1:]
logit = sm.Logit(data['admit'], data[train_cols])
result = logit.fit()

data['admit_pred'] = result.predict(data[train_cols])

#predicts admissions with an 58% accuracy rate
